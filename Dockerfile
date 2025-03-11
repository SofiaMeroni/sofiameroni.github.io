# Dockerfile multi-etapa para construir y servir un sitio Jekyll
# Utiliza una etapa de compilación separada para reducir el tamaño final

# ===== ETAPA DE COMPILACIÓN =====
FROM ruby:3.1-slim AS builder

# Establecer variables de entorno y directorio de trabajo
ENV JEKYLL_ENV=production
WORKDIR /app

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo los archivos necesarios para instalar dependencias primero
# Esto mejora el uso de la caché de Docker
COPY Gemfile Gemfile.lock* ./

# Instalar dependencias de Ruby
RUN bundle install --jobs=4 --retry=3

# Copiar el resto del código fuente
COPY . .

# Construir el sitio estático
RUN bundle exec jekyll build

# ===== ETAPA FINAL =====
FROM python:3.11-slim

# Metadatos según OCI Image Format
LABEL org.opencontainers.image.title="Portafolio Personal"
LABEL org.opencontainers.image.description="Sitio web personal con prácticas DevOps"
LABEL org.opencontainers.image.authors="Sofia Meroni"
LABEL org.opencontainers.image.source="https://github.com/SofiaMeroni/sofiameroni.github.io"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar servidor web ligero
RUN pip install --no-cache-dir flask gunicorn

# Copiar solo los archivos estáticos generados
COPY --from=builder /app/_site /app/_site

# Copiar script para servir el sitio
COPY scripts/serve.py ./

# Puerto en el que se ejecutará la aplicación
EXPOSE 8080

# Definir un usuario no privilegiado
RUN useradd -m appuser
RUN chown -R appuser:appuser /app
USER appuser

# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "serve:app"]

# Script de HEALTHCHECK
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8080/ || exit 1