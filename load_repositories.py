import os
import json
from pymongo import MongoClient
from tqdm import tqdm


# Inicializamos el cliente
mongoHost= "localhost"
mongoPort=27017

mongoClient = MongoClient(mongoHost, mongoPort, serverSelectionTimeoutMS=1000)

repoDb = mongoClient["tfg_project"]

collection_repo = repoDb["prueba"]
collection_commit = repoDb["Commits"]

print("INICIANDO CARGA DE REPOSITORIOS")

# Directorio que contiene los archivos JSON
repos_directorio = 'archivos/repository'

# Obtener la lista de archivos en el directorio
archivos_json = os.listdir(repos_directorio)

# Iterar sobre los archivos json
for archivo in tqdm(archivos_json):
    # Verificar si el archivo es un archivo JSON
    if archivo.endswith('.json'):
        # Construir la ruta completa al archivo
        ruta_archivo = os.path.join(repos_directorio, archivo)
        
        # Leer el archivo JSON
        with open(ruta_archivo, 'r') as f:
            contenido = json.load(f)
            contenido['commits'] = []
            contenido['uml'] = False
            contenido['num_commits'] = 0
            contenido['contributors'] = []
            contenido['num_contributors'] = 0
            collection_repo.insert_one(contenido)

print("TERMINADA LA CARGA DE REPOSITORIOS")

print("INICIANDO CARGA DE COMMITS")

# Arreglo con patrones de ficheros UML
filesUML=['.uml','uml/','/uml', '_uml', 'uml_','-uml','uml-', '/UML','UML/','UML.', '.UML','-UML','UML-', '_UML', 'UML_']

total_commits = collection_commit.count_documents({})

ReposUML = set()
for commit in tqdm(collection_commit.find({}), total=total_commits):
    origin = commit['origin'].replace('www.', '').replace('.git', '')
    for fileName in commit['data']['files']:
        for umlPattern in filesUML:
            if umlPattern in fileName['file']: 
                ReposUML.add(origin)

    repo = collection_repo.find_one({'origin': origin})

    if repo:
        if origin in ReposUML:
            repo['uml'] = True
        else:
            repo['uml'] = False
        repo['num_commits'] = repo['num_commits'] + 1
        conjuntoCommits = [repo['commits']]

        if not(repo['commits']) in conjuntoCommits:
            conjuntoCommits.append(commit)  
        conjuntoContributors = set(repo['contributors'])
        conjuntoContributors.add(commit['data']['Author'])
        repo['contributors'] = list(conjuntoContributors)
        repo['num_contributors'] = len(repo['contributors'])
        collection_repo.replace_one({'origin': origin}, repo)
            
print("TERMINADA LA CARGA DE COMMITS")
print(len(ReposUML))

mongoClient.close()


