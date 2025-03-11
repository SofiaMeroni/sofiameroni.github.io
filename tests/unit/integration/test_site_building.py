"""
Tests de integración para verificar que el sitio se construye correctamente.
"""

import os
import subprocess
import pytest

@pytest.fixture(scope="module")
def build_site():
    """Construye el sitio Jekyll antes de ejecutar los tests."""
    if os.path.exists("_site"):
        subprocess.run(["rm", "-rf", "_site"], check=True)
    
    # Asumimos que Jekyll y Bundle están instalados
    result = subprocess.run(
        ["bundle", "exec", "jekyll", "build"],
        capture_output=True,
        text=True
    )
    
    yield result
    
def test_build_successful(build_site):
    """Verifica que la construcción del sitio fue exitosa."""
    assert build_site.returncode == 0, \
        f"La construcción falló con el error: {build_site.stderr}"

def test_site_directory_created(build_site):
    """Verifica que el directorio _site se creó."""
    assert os.path.isdir("_site"), "El directorio _site no se creó"

def test_html_files_generated(build_site):
    """Verifica que se generaron archivos HTML."""
    assert os.path.exists("_site/index.html"), "No se generó el archivo index.html"
    assert os.path.exists("_site/contact.html"), "No se generó el archivo contact.html"

def test_css_files_copied(build_site):
    """Verifica que los archivos CSS se copiaron al directorio _site."""
    assert os.path.isdir("_site/assets/css"), "El directorio assets/css no existe en _site"
    
    # Verificar que hay al menos un archivo CSS
    css_files = [f for f in os.listdir("_site/assets/css") if f.endswith(".css")]
    assert len(css_files) > 0, "No se encontraron archivos CSS en _site/assets/css"

def test_images_copied(build_site):
    """Verifica que las imágenes se copiaron al directorio _site."""
    assert os.path.isdir("_site/assets/images"), "El directorio assets/images no existe en _site"

def test_html_contains_expected_elements():
    """Verifica que el HTML generado contiene los elementos esperados."""
    with open("_site/index.html", "r") as file:
        content = file.read()
        
    assert "<html" in content, "El archivo index.html no contiene la etiqueta <html>"
    assert "<head" in content, "El archivo index.html no contiene la etiqueta <head>"
    assert "<body" in content, "El archivo index.html no contiene la etiqueta <body>"
    assert "</html>" in content, "El archivo index.html no contiene la etiqueta de cierre </html>"