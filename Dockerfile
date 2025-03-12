# Etapa 1: Construcción con Ruby y Jekyll
FROM ruby:3.4-slim as builder

# Instalar dependencias necesarias para Jekyll
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Establecer directorio de trabajo
WORKDIR /app

# Copiar Gemfile y Gemfile.lock primero para mejor uso de caché
COPY Gemfile Gemfile.lock ./

# Instalar Bundler y las gemas del proyecto
RUN gem install bundler:2.6.5 && bundle install --verbose

# Copiar el resto de los archivos del proyecto
COPY . .

# Construir sitio estático con Jekyll
RUN bundle exec jekyll build

# Etapa 2: Servidor web con Python
FROM python:3.10-slim

# Metadatos del contenedor
LABEL org.opencontainers.image.title="Portafolio Personal"
LABEL org.opencontainers.image.description="Sitio web personal con prácticas DevOps"
LABEL org.opencontainers.image.authors="Sofia Meroni"
LABEL org.opencontainers.image.source="https://github.com/SofiaMeroni/sofiameroni.github.io"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias de Python necesarias para servir el sitio
RUN pip install --no-cache-dir flask gunicorn

# Copiar sitio estático generado desde la etapa de construcción
COPY --from=builder /app/_site /app/_site

# Copiar script para servir el sitio
COPY scripts/serve.py ./

# Exponer puerto para la aplicación
EXPOSE 8080

# Ejecutar el servidor Flask
CMD ["python", "serve.py"]
