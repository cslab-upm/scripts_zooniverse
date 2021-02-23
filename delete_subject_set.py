# Llamada: python3 delete_subject_set.py 92169
# El último número es el id del subject set que se desea eliminar. Se puede ver
# en Zooniverse

from panoptes_client import SubjectSet, Subject, Project, Panoptes
import configparser
import sys

try:
    config = configparser.ConfigParser()
    config.read('configuracion.properties')
    
    user = config.get('Credentials', 'username')
    passwd = config.get('Credentials', 'password')
except:
    print('ERROR: No se ha podido leer el fichero de configuración.')
    sys.exit(1)

Panoptes.connect(username=user, password=passwd)

project = Project('13586')

subject_set_id = str(sys.argv[1])

subject_set = SubjectSet.find(subject_set_id)

print("Eliminando subjects.")
for subject in subject_set.subjects:
    subject_set.remove(subject.id)

print("Eliminando Subject Set.")
project.links.subject_sets.remove(subject_set_id)

