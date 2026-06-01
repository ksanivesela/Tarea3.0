# Tarea 3.0 - Automatización de CI/CD con GitHub Actions y Docker

## Nombre de la aplicación

**ejercicio:3.0.0**

## Descripción

Este proyecto contiene una aplicación sencilla desarrollada en Python. La aplicación funciona como una calculadora básica que permite realizar operaciones como suma, resta, multiplicación y división.

Además, el proyecto incluye pruebas automatizadas con `pytest`, un archivo `Dockerfile` para construir una imagen Docker y un workflow de GitHub Actions para automatizar el proceso de CI/CD.

## Tecnologías utilizadas

* Python
* Pytest
* Docker
* GitHub Actions
* GitHub Container Registry

## Ejecución local

Para ejecutar la aplicación:

```bash
python app.py
```

## Ejecutar pruebas

Para ejecutar las pruebas automatizadas:

```bash
pytest
```

## Construir imagen Docker

```bash
docker build -t ejercicio:3.0.0 .
```

## Ejecutar contenedor Docker

```bash
docker run ejercicio:3.0.0
```

## Imagen en GitHub Container Registry

La imagen se publica con la siguiente nomenclatura:

```bash
ghcr.io/usuario/ejercicio:3.0.0
```

## CI/CD

El workflow `python-application.yml` realiza las siguientes acciones:

1. Descarga el código fuente.
2. Configura Python.
3. Instala dependencias.
4. Ejecuta pruebas automatizadas.
5. Ejecuta la aplicación.
6. Simula una fase de despliegue.
7. Construye la imagen Docker.
8. Se autentica en GitHub Container Registry.
9. Publica la imagen generada.
