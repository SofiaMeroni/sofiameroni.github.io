#!/usr/bin/env python3
"""
Script para configurar la estructura de carpetas del proyecto.
"""

import os
import sys

def create_directory(directory):
    """
    Crea un directorio si no existe.
    
    Args:
        directory (str): Ruta del directorio a crear
    """
    if not os.path.exists(directory):
        print(f"Creando directorio: {directory}")
        os.makedirs(directory)
    else:
        print(f"El directorio ya existe: {directory}")

def create_file(file_path, content=""):
    """
    Crea un archivo si no existe.
    
    Args:
        file_path (str): Ruta del archivo a crear
        content (str): Contenido inicial del archivo
    """
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
    if not os.path.exists("src/index.md"):
        create_file("src/index.md", """---
layout: default
title: Inicio
---

# Bienvenido a mi portafolio

Soy un DevOps Engineer apasionado por la automatización y las buenas prácticas de desarrollo.
""")
    
    if not os.path.exists("src/contact.md"):
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
    
    # Crear archivo de test unitario mínimo
    create_file("tests/unit/__init__.py")
    create_file("tests/integration/__init__.py")
    
    # Crear un archivo de test básico si no existe ninguno
    if not os.path.exists("tests/unit/test_basic.py"):
        create_file("tests/unit/test_basic.py", """
def test_basic():
    \"\"\"Test básico que siempre pasa.\"\"\"
    assert True
""")
    
    # Verificar si el archivo serve.py existe
    if not os.path.exists("scripts/serve.py"):
        print("IMPORTANTE: Debes crear el archivo scripts/serve.py con el contenido proporcionado anteriormente.")
    
    print("\n¡Estructura básica del proyecto configurada!")
    print("Por favor, verifica que todos los archivos necesarios se hayan creado correctamente.")

if __name__ == "__main__":
    setup_project_structure()

"""
# Resumen del Script setup_structure.py

Este script automatiza la creación de la estructura de carpetas y archivos esenciales para el proyecto, 
asegurando un entorno de desarrollo organizado y funcional.

### Funcionalidades principales:
1. **Creación de Directorios**:  
   - Genera carpetas clave como `src/`, `tests/`, `scripts/` y `.github/workflows/`.
   - Asegura que las carpetas de assets y layouts de Jekyll existan en `src/`.

2. **Generación de Archivos Iniciales**:  
   - Crea archivos de contenido (`index.md`, `contact.md`) dentro de `src/` si no existen.
   - Agrega archivos vacíos `__init__.py` en `tests/unit/` y `tests/integration/` para estructurar los tests.
   - Genera un test unitario mínimo (`test_basic.py`) si no existe.

3. **Verificación del Servidor**:  
   - Comprueba si el archivo `scripts/serve.py` está presente y muestra un mensaje de advertencia si falta.

### Propósito:
Este script facilita la inicialización del proyecto al garantizar que todos los archivos y directorios 
necesarios estén listos antes del desarrollo y la implementación. Esto permite mantener un entorno ordenado 
y coherente sin necesidad de crear manualmente la estructura base.
"""
