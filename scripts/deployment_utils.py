#!/usr/bin/env python3
"""
Utilidades de despliegue para el portafolio personal.
Este script proporciona herramientas para validar y preparar el sitio para su despliegue.
"""

import os
import sys
import subprocess
import logging
import re
from datetime import datetime

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("deployment.log")
    ]
)
logger = logging.getLogger("deployment-utils")

def validate_jekyll_config():
    """
    Valida el archivo _config.yml para asegurar que tiene todas las configuraciones necesarias.
    
    Returns:
        bool: True si el archivo es válido, False en caso contrario.
    """
    logger.info("Validando configuración de Jekyll...")
    
    try:
        if not os.path.exists("_config.yml"):
            logger.error("Error: No se encontró el archivo _config.yml")
            return False
            
        # Validación básica del contenido del archivo
        with open("_config.yml", "r") as config_file:
            content = config_file.read()
            
        # Verificar configuraciones esenciales
        required_settings = ["title", "url", "baseurl"]
        for setting in required_settings:
            if not re.search(rf"{setting}:", content):
                logger.error(f"Error: Falta la configuración '{setting}' en _config.yml")
                return False
                
        logger.info("Configuración de Jekyll validada correctamente.")
        return True
        
    except Exception as e:
        logger.error(f"Error al validar _config.yml: {e}")
        return False

def build_jekyll_site():
    """
    Construye el sitio Jekyll usando bundle exec jekyll build.
    
    Returns:
        bool: True si la construcción tiene éxito, False en caso contrario.
    """
    logger.info("Construyendo el sitio Jekyll...")
    
    try:
        result = subprocess.run(
            ["bundle", "exec", "jekyll", "build"], 
            capture_output=True,
            text=True,
            check=True
        )
        logger.info("Sitio construido exitosamente.")
        logger.debug(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al construir el sitio: {e}")
        logger.error(e.stderr)
        return False

def validate_html_files(directory="_site"):
    """
    Valida los archivos HTML generados en el directorio especificado.
    
    Args:
        directory (str): El directorio donde se encuentran los archivos HTML.
        
    Returns:
        bool: True si todos los archivos son válidos, False en caso contrario.
    """
    logger.info(f"Validando archivos HTML en '{directory}'...")
    
    try:
        # Esta es una validación simplificada - en un entorno real usaríamos una librería de validación HTML
        if not os.path.exists(directory):
            logger.error(f"Error: El directorio '{directory}' no existe.")
            return False
            
        html_files = [f for f in os.listdir(directory) if f.endswith(".html")]
        
        if not html_files:
            logger.error(f"No se encontraron archivos HTML en '{directory}'.")
            return False
            
        logger.info(f"Se encontraron {len(html_files)} archivos HTML.")
        
        # Validación básica - verificar que cada archivo tenga elementos HTML esenciales
        valid_files = 0
        for html_file in html_files:
            file_path = os.path.join(directory, html_file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            if all(tag in content.lower() for tag in ["<!doctype html>", "<html", "<head", "<body"]):
                valid_files += 1
            else:
                logger.warning(f"Advertencia: El archivo '{html_file}' podría no ser HTML válido.")
        
        logger.info(f"{valid_files} de {len(html_files)} archivos HTML parecen válidos.")
        return valid_files == len(html_files)
        
    except Exception as e:
        logger.error(f"Error al validar archivos HTML: {e}")
        return False

def create_deployment_report():
    """
    Crea un informe de despliegue con información del momento.
    
    Returns:
        str: Ruta al archivo de informe generado.
    """
    logger.info("Creando informe de despliegue...")
    
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = f"deployment_report_{timestamp}.txt"
        
        # Obtener información del sistema y del repositorio
        git_branch = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        
        git_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True, text=True, check=True
        ).stdout.strip()
        
        # Crear informe
        with open(report_path, "w") as report_file:
            report_file.write("INFORME DE DESPLIEGUE\n")
            report_file.write("====================\n\n")
            report_file.write(f"Fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report_file.write(f"Rama: {git_branch}\n")
            report_file.write(f"Commit: {git_commit}\n\n")
            report_file.write("Configuración validada: " + 
                             ("Sí" if validate_jekyll_config() else "No") + "\n")
            
            build_success = build_jekyll_site()
            report_file.write("Construcción exitosa: " + 
                             ("Sí" if build_success else "No") + "\n")
            
            if build_success:
                html_valid = validate_html_files()
                report_file.write("HTML válido: " + 
                                 ("Sí" if html_valid else "No") + "\n")
            
        logger.info(f"Informe de despliegue creado en '{report_path}'.")
        return report_path
        
    except Exception as e:
        logger.error(f"Error al crear informe de despliegue: {e}")
        return None

def main():
    """Función principal que ejecuta el proceso de validación de despliegue."""
    logger.info("Iniciando utilidades de despliegue...")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--validate-only":
        # Solo ejecutar validación
        config_valid = validate_jekyll_config()
        print(f"Configuración válida: {'✅' if config_valid else '❌'}")
        
    elif len(sys.argv) > 1 and sys.argv[1] == "--build-only":
        # Solo construir el sitio
        build_result = build_jekyll_site()
        print(f"Construcción exitosa: {'✅' if build_result else '❌'}")
        
    else:
        # Ejecutar flujo completo y generar informe
        report_path = create_deployment_report()
        if report_path:
            print(f"Proceso completado. Informe disponible en: {report_path}")
        else:
            print("Error al generar informe de despliegue.")
            sys.exit(1)
    
    logger.info("Proceso de utilidades de despliegue finalizado.")

if __name__ == "__main__":
    main()

"""
# Resumen del Script deployment_utils.py

Este script proporciona herramientas para validar y preparar el sitio Jekyll antes del despliegue.
Las funciones principales incluyen:

1. **Validación de Configuración (_config.yml)**:  
   - Verifica que el archivo `_config.yml` contenga las configuraciones esenciales para Jekyll.

2. **Construcción del Sitio Jekyll**:  
   - Ejecuta `bundle exec jekyll build` para generar la versión estática del sitio.

3. **Validación de Archivos HTML**:  
   - Revisa los archivos generados en `_site/` para verificar que tengan estructura HTML válida.

4. **Generación de Informe de Despliegue**:  
   - Crea un archivo de informe con detalles como la fecha, la rama actual, el commit y los resultados de las validaciones.

5. **Modo de Ejecución**:  
   - Si el script se ejecuta con `--validate-only`, solo valida `_config.yml`.  
   - Con `--build-only`, solo construye el sitio.  
   - Sin argumentos, ejecuta todo el flujo y genera el informe de despliegue.

Este script ayuda a asegurar que el sitio Jekyll esté listo para ser publicado sin errores, facilitando la automatización del despliegue.
"""
