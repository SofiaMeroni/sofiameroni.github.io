# Usamos una imagen base que ya incluye Ruby y Bundler
FROM ruby:2.7-slim as builder

# Instalar dependencias necesarias para Jekyll
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar primero solo Gemfile para mejor uso de caché
COPY Gemfile* ./

# Instalar gemas de Jekyll
RUN bundle install --verbose

# Copiar el resto de los archivos del proyecto
COPY . .

# Construir sitio estático
RUN bundle exec jekyll build

# Segunda etapa - servidor web
FROM python:3.10-slim

# Metadatos
LABEL org.opencontainers.image.title="Portafolio Personal"
LABEL org.opencontainers.image.description="Sitio web personal con prácticas DevOps"
LABEL org.opencontainers.image.authors="Sofia Meroni"
LABEL org.opencontainers.image.source="https://github.com/SofiaMeroni/sofiameroni.github.io"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar solo las dependencias necesarias para el servidor
COPY requirements.txt .
RUN pip install --no-cache-dir flask gunicorn

# Copiar sitio estático desde la etapa de construcción
COPY --from=builder /app/_site /app/_site

# Copiar script para servir el sitio
COPY scripts/serve.py ./

# Puerto en el que se ejecutará la aplicación
EXPOSE 8080

# Ejecutar el servidor
CMD ["python", "serve.py"]