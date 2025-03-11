"""
Tests unitarios para validar la estructura del sitio web.
"""

import os
import pytest
import yaml
import re

def test_config_file_exists():
    """Verifica que el archivo _config.yml existe."""
    assert os.path.exists("_config.yml"), "El archivo _config.yml no existe"

def test_config_file_valid():
    """Verifica que el archivo _config.yml tiene formato YAML válido."""
    try:
        with open("_config.yml", "r") as file:
            yaml.safe_load(file)
        assert True
    except yaml.YAMLError as e:
        assert False, f"El archivo _config.yml no tiene un formato YAML válido: {e}"

def test_required_directories():
    """Verifica que las carpetas necesarias existen."""
    required_dirs = ["src", "src/_layouts", "src/assets", "src/assets/css", "src/assets/images"]
    for directory in required_dirs:
        assert os.path.isdir(directory), f"El directorio {directory} no existe"

def test_index_file_exists():
    """Verifica que existe un archivo index.md."""
    assert os.path.exists("src/index.md"), "El archivo index.md no existe en src/"

def test_contact_file_exists():
    """Verifica que existe un archivo contact.md."""
    assert os.path.exists("src/contact.md"), "El archivo contact.md no existe en src/"

def test_layout_front_matter():
    """Verifica que los archivos Markdown tienen front matter válido."""
    markdown_files = ["src/index.md", "src/contact.md"]
    
    for filename in markdown_files:
        with open(filename, "r") as file:
            content = file.read()
            # Verificar que hay front matter (contenido entre ---)
            assert re.match(r"^---\n(.*?)\n---", content, re.DOTALL), \
                   f"El archivo {filename} no tiene front matter válido"

def test_dockerfile_exists():
    """Verifica que existe un Dockerfile."""
    assert os.path.exists("Dockerfile"), "El archivo Dockerfile no existe"

def test_docker_compose_exists():
    """Verifica que existe un archivo docker-compose.yml."""
    assert os.path.exists("docker-compose.yml"), "El archivo docker-compose.yml no existe"

def test_github_workflows_directory():
    """Verifica que existe el directorio .github/workflows."""
    assert os.path.isdir(".github/workflows"), "El directorio .github/workflows no existe"