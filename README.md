# Programa

Estos dos programas se encargan de la gestión de los subject set de Zooniverse para subir o eliminar las muestras utilizadas

## Instalación

Para la correcta ejecución del software, es necesario instalar **python3** y ciertas librerías de python:

**Python**

    sudo apt-get install python3.7
    
**panoptes_client**

    pip3 install panoptes_client
    
## upload_from_manifest

Este script se encarga de añadir las muestras seleccionadas por el script ramdon_selection en un subject set de Zooniverse.

La sintaxis para ejecutar el script es la siguiente:

    python3 upload_from_manifest.py nombre_directorio
    
El nombre del directorio será la misma que en el programa anterior.

Ejemplo de ejecución:

	python3 upload_from_manifest.py 2020_06
	
## delete_subject_set

Este script elimina un subject set de Zooniverse.

La sintaxis para ejecutar el script es la siguiente:

	python3 delete_subject_set.py #id_subject_set

Ejemplo de ejecución:

	python3 delete_subject_set.py 92576
