## ❀ Hola ❀
<div style="line-height: 2.0;">
Mi experiencia en calidad y automatización de pruebas me permite abordar los desafíos del software con un enfoque riguroso y técnico. Desde la creación de pruebas manuales hasta la implementación de soluciones automatizadas, mi objetivo es optimizar la calidad del software y asegurar una experiencia de usuario superior. Estoy orientada a resultados y busco continuamente mejorar los procesos para alcanzar la excelencia en cada proyecto
</div>




## 🛠️ Tecnologías Utilizadas modificar

| DevOps & Infra | Desarrollo | Pruebas |
|---------------|------------|---------|
| GitHub Actions | Python (Flask) | PyTest |
| Docker & Docker Compose | Jekyll | YAML Validation |
| CI/CD Pipelines | HTML/CSS | Selenium |

## 🔄 Automatización con CI/CD

El flujo de trabajo de integración y despliegue continuo (CI/CD) en este repositorio incluye:

1. **CI con GitHub Actions:**
   - Se ejecutan pruebas unitarias con `pytest`.
   - Se valida la estructura del sitio y los archivos YAML.
   - Se construye la imagen Docker.

2. **CD con GitHub Actions:**
   - Se despliega automáticamente la última versión del sitio web.
   - Se actualiza la imagen en Docker Hub.

## 🐳 Despliegue con Docker

Este proyecto utiliza contenedores para construir y servir el sitio web. 

- **Dockerfile:** Se divide en dos etapas:
  1. **Builder:** Usa Ruby y Jekyll para generar el sitio estático.
  2. **Servidor:** Utiliza Flask y Gunicorn para servir el sitio en `8080`.

- **docker-compose.yml:**
  - Un servicio `jekyll` que construye el sitio.
  - Un servicio `website` que lo sirve en un contenedor Python.

### 🚀 Para probarlo localmente:
```bash
docker-compose up --build
```
Luego accede a `http://localhost:8080`.

## ✅ Pruebas Automatizadas

Se implementaron pruebas unitarias en `tests/test_site_structure.py` para validar:
- Existencia de archivos clave (`_config.yml`, `index.md`, `contact.md`).
- Integridad de la estructura del proyecto.
- Validación de YAML y front matter en archivos Markdown.

## 🎯 Objetivo del Proyecto

Este repositorio no es solo un portafolio personal, sino también una muestra de mis habilidades en DevOps, automatización y desarrollo de software. Aquí demuestro cómo:
- Construir y desplegar un sitio web con Jekyll.
- Implementar CI/CD con GitHub Actions.
- Orquestar contenedores con Docker.
- Automatizar validaciones y pruebas.

### Mi stack hasta ahora

| Lenguajes    | Tecnologías Web | RDBMS         | Automatización de Pruebas | Herramientas de Pruebas | Control de Versiones |
| :----------: |:---------------:|:-------------:| :-----------------------:| :---------------------:| :-------------------:| 
| `Python`     | `HTML`          | `PostgreSQL`  | `Selenium`               | `Postman API`          | `Git`                |
| `SQL`        | `CSS`           | `MySQL`       | `JMeter`                 | `VS Code`              |                      |
|              | `JavaScript`    | `SQLite`      | `PyTest`                 |                        |                      |


Puedes contactarme en: [LinkedIn](www.linkedin.com/in/sofiameroni)


<img src="images/floral-design.png" alt="Ícono de Flaticon" width="150" height="150">