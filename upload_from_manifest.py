# Llamada: python3 upload_from_manifest.py 2020_06

import csv
import sys
import configparser

from panoptes_client import SubjectSet, Subject, Project, Panoptes

month = sys.argv[1]

try:
    config = configparser.ConfigParser()
    config.read('configuracion.properties')
    
    user = config.get('Credentials', 'username')
    passwd = config.get('Credentials', 'password')
    
    manifest_path = config.get('Directorios', 'manifest_path')
except:
    print('ERROR: No se ha podido leer el fichero de configuración.')
    sys.exit(1)


#  modify path and file name as needed:
manifest_images_file = manifest_path + "manifest_images_" + month +".csv"
manifest_sounds_file = manifest_path + "manifest_sounds_" + month +".csv"

image_set_name = 'image_set_' + month
audio_set_name = 'audio_set_' + month

# Conexión con Panoptes
Panoptes.connect(username=user, password=passwd)

#  El proyecto "Sky Sounds" tiene asociado el identificador 13586.
project = Project('13586')

# ------- Subject set de imágenes -------
# Conexión con el subject set correspondiente o creación de uno nuevo en caso
# de que este no exista.
try:
    # Comprueba si existe el subject set.
    subject_set = SubjectSet.where(project_id=project.id, display_name=image_set_name).next()
except StopIteration:
    # Crea un nuevo subject set para los nuevos datos y lo asocia al proyecto.
    subject_set = SubjectSet()
    subject_set.links.project = project
    subject_set.display_name = image_set_name
    subject_set.save()


# Adicción de las muestras al subject set.
with open(manifest_images_file, 'r') as mani_file:
    print('Uploading image_set')
    r = csv.DictReader(mani_file)
    for line in r:
        subject = Subject()
        subject.links.project = project
        
        subject.add_location(line['lc'])
        subject.add_location(line['sp'])
        subject.metadata['subject_id'] = line['id']
        subject.save()
        subject_set.add(subject.id)
        
        
# ------- Subject set de sonidos -------    
# Conexión con el subject set correspondiente o creación de uno nuevo en caso
# de que este no exista.
try:
    # Comprueba si existe el subject set.
    subject_set = SubjectSet.where(project_id=project.id, display_name=audio_set_name).next()
except StopIteration:
    # Crea un nuevo subject set para los nuevos datos y lo asocia al proyecto.
    subject_set = SubjectSet()
    subject_set.links.project = project
    subject_set.display_name = audio_set_name
    subject_set.save()


# Adicción de las muestras al subject set.with open(manifest_sounds_file, 'r') as mani_file:
with open(manifest_images_file, 'r') as mani_file:
    print('Uploading audio_set')
    r = csv.DictReader(mani_file)
    for line in r:
        subject = Subject()
        subject.links.project = project
        
        subject.add_location(line['snd'])
        subject.add_location(line['pic'])
        subject.metadata['subject_id'] = line['id']
        subject.save()
        subject_set.add(subject.id)
