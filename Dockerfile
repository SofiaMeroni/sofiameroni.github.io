# Imagen base para Jekyll
FROM jekyll/jekyll:4.2.2 as builder

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios para bundle install
COPY Gemfile* .

# Instalar dependencias
RUN bundle install

# Copiar el resto del sitio
COPY . .

# Construir el sitio
RUN jekyll build

# Segunda etapa - servidor web
FROM python:3.10-slim

# Metadatos
LABEL org.opencontainers.image.title="Portafolio Personal"
LABEL org.opencontainers.image.description="Sitio web personal con prácticas DevOps"
LABEL org.opencontainers.image.authors="Sofia Meroni"
LABEL org.opencontainers.image.source="https://github.com/SofiaMeroni/sofiameroni.github.io"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar sitio estático desde la etapa de construcción
COPY --from=builder /app/_site /app/_site

# Copiar script para servir el sitio
COPY scripts/serve.py ./

# Puerto en el que se ejecutará la aplicación
EXPOSE 8080

# Ejecutar el servidor
CMD ["python", "serve.py"]