"""
Servidor web simple para servir el sitio estático generado por Jekyll.
"""

import os
from flask import Flask, send_from_directory

# Crear aplicación Flask
app = Flask(__name__)

# Configurar la ruta base para servir archivos estáticos
SITE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_site')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static(path):
    """
    Sirve archivos estáticos desde el directorio _site.
    
    Args:
        path (str): La ruta del archivo solicitado
        
    Returns:
        Response: El archivo solicitado o index.html
    """
    if path == "" or path == "/":
        return send_from_directory(SITE_DIR, 'index.html')
    
    # Si el path es un directorio, servir index.html de ese directorio
    if os.path.isdir(os.path.join(SITE_DIR, path)):
        return send_from_directory(os.path.join(SITE_DIR, path), 'index.html')
    
    # Intentar servir el archivo directamente
    try:
        return send_from_directory(SITE_DIR, path)
    except:
        # Fallback a 404.html si existe
        if os.path.exists(os.path.join(SITE_DIR, '404.html')):
            return send_from_directory(SITE_DIR, '404.html'), 404
        else:
            return "File not found", 404

@app.route('/health')
def health_check():
    """
    Endpoint para health checks.
    
    Returns:
        str: Mensaje de estado OK
    """
    return "OK", 200

if __name__ == '__main__':
    # Obtener puerto del entorno o usar 8080 por defecto
    port = int(os.environ.get('PORT', 8080))
    
    # Ejecutar el servidor en modo de desarrollo
    app.run(host='0.0.0.0', port=port, debug=False)