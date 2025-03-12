#!/usr/bin/env python3
"""
Script para configurar la estructura de carpetas del proyecto.
"""

import os
import sys
import shutil

def create_directory(directory):
    """
    Crea un directorio si no existe.
    
    Args:
        directory (str): Ruta del directorio a crear
    """
    if not os.path.exists(directory):
        print(f"Creando directorio: {directory}")
        os.makedirs(directory, exist_ok=True)
    else:
        print(f"El directorio ya existe: {directory}")

def create_file(file_path, content=""):
    """
    Crea un archivo si no existe.
    
    Args:
        file_path (str): Ruta del archivo a crear
        content (str): Contenido inicial del archivo
    """
    # Asegurarse de que el directorio padre existe
    parent_dir = os.path.dirname(file_path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
        
    if not os.path.exists(file_path):
        print(f"Creando archivo: {file_path}")
        with open(file_path, "w") as f:
            f.write(content)
    else:
        print(f"El archivo ya existe: {file_path}")

def setup_project_structure():
    """
    Configura la estructura de carpetas del proyecto.
    """
    # Crear directorios principales
    directories = [
        "src",
        "src/_layouts",
        "src/assets",
        "src/assets/css",
        "src/assets/images",
        "tests",
        "tests/unit",
        "tests/integration",
        "scripts",
        ".github/workflows"
    ]
    
    for directory in directories:
        create_directory(directory)
    
    # Crear archivos iniciales si no existen
    create_file("src/index.md", """---
layout: default
title: Inicio
---

# Bienvenido a mi portafolio

Soy un DevOps Engineer apasionado por la automatización y las buenas prácticas de desarrollo.
""")
    
    create_file("src/contact.md", """---
layout: default
title: Contacto
---

# Contacto

Puedes contactarme a través de:

- Email: ejemplo@dominio.com
- LinkedIn: [Mi perfil](https://linkedin.com/in/tu-perfil)
- GitHub: [Mi GitHub](https://github.com/SofiaMeroni)
""")
    
    # Crear archivos básicos de Jekyll si no existen
    if not os.path.exists("_config.yml"):
        create_file("_config.yml", """# Configuración básica del sitio
title: Portafolio Personal
email: ejemplo@dominio.com
description: >-
  Portafolio personal con prácticas DevOps implementadas.
baseurl: "" # la subpath de tu sitio, e.g. /blog
url: "https://sofiameroni.github.io" # la URL base de tu sitio

# Configuración de build
source: src
destination: _site
plugins:
  - jekyll-feed
  - jekyll-seo-tag
""")
    
    # Crear archivo de test unitario mínimo
    create_file("tests/unit/__init__.py")
    create_file("tests/integration/__init__.py")
    
    # Crear un archivo de test básico si no existe ninguno
    create_file("tests/unit/test_basic.py", """
def test_basic():
    \"\"\"Test básico que siempre pasa.\"\"\"
    assert True
""")
    
    # Crear script básico de servidor
    create_file("scripts/serve.py", """
import os
from flask import Flask, send_from_directory

# Crear aplicación Flask
app = Flask(__name__)

# Configurar la ruta base para servir archivos estáticos
SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../_site')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    \"\"\"Sirve archivos estáticos desde el directorio _site.\"\"\"
    if path == "" or path == "/":
        return send_from_directory(SITE_DIR, 'index.html')
    
    # Si el path existe como archivo, servirlo
    if os.path.exists(os.path.join(SITE_DIR, path)):
        return send_from_directory(SITE_DIR, path)
    
    # Si existe como directorio, servir index.html de ese directorio
    if os.path.exists(os.path.join(SITE_DIR, path, 'index.html')):
        return send_from_directory(os.path.join(SITE_DIR, path), 'index.html')
    
    # Fallback a 404.html si existe
    if os.path.exists(os.path.join(SITE_DIR, '404.html')):
        return send_from_directory(SITE_DIR, '404.html'), 404
    else:
        return "File not found", 404

@app.route('/health')
def health_check():
    \"\"\"Endpoint para health checks.\"\"\"
    return "OK", 200

if __name__ == '__main__':
    # Obtener puerto del entorno o usar 8080 por defecto
    port = int(os.environ.get('PORT', 8080))
    
    # Ejecutar el servidor
    app.run(host='0.0.0.0', port=port)
""")
    
    # Crear Gemfile si no existe
    create_file("Gemfile", """source "https://rubygems.org"

gem "jekyll", "~> 4.2.0"
gem "minima", "~> 2.5"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag", "~> 2.7"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Lock to this version for ARM compatibility
gem "http_parser.rb", "~> 0.6.0"
""")
    
    create_file(".gitignore", """# Ignorar archivos generados por Jekyll
_site/
.sass-cache/
.jekyll-cache/
.jekyll-metadata
vendor/

# Ignorar configuraciones locales
.bundle/
.env

# Ignorar archivos de Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Ignorar archivos de coverage
.coverage
htmlcov/
coverage.xml
*.cover

# Ignorar archivos de VSCode
.vscode/

# Ignorar archivos de sistema
.DS_Store
Thumbs.db
""")
    
    print("\n¡Estructura básica del proyecto configurada!")
    print("Por favor, verifica que todos los archivos necesarios se hayan creado correctamente.")

if __name__ == "__main__":
    setup_project_structure()

"""
# Resumen del Script serve.py

Este script configura la estructura base del proyecto asegurando que todos los directorios y archivos esenciales 
estén presentes antes del desarrollo y despliegue. 

### Funcionalidades principales:
1. **Creación de Directorios y Archivos**:  
   - Genera carpetas clave como `src/`, `tests/`, `scripts/` y `.github/workflows/`.
   - Crea archivos básicos de configuración y contenido (`_config.yml`, `Gemfile`, `index.md`, `contact.md`, etc.).
   - Asegura la existencia de archivos esenciales para pruebas en `tests/unit/` y `tests/integration/`.

2. **Inicialización de un Servidor Local (Flask)**:  
   - Configura un servidor para servir archivos estáticos desde `_site/` (carpeta de salida de Jekyll).
   - Implementa un endpoint `/health` para comprobar el estado del servidor.
   - Soporta rutas dinámicas para servir archivos HTML y otros recursos estáticos.

3. **Generación de Archivos de Configuración y Exclusión**:  
   - Crea un `Gemfile` con las dependencias necesarias para Jekyll.
   - Configura un archivo `.gitignore` para excluir archivos innecesarios del repositorio.

### Propósito:
Este script facilita la inicialización del proyecto automatizando la creación de la estructura necesaria, lo que 
permite mantener un entorno de desarrollo ordenado y coherente. También proporciona un servidor básico para 
probar el sitio localmente antes del despliegue.
"""
