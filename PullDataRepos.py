import pymongo
from pymongo import MongoClient
# import PullTypeFiles


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017
mongoClient = MongoClient(mongoHost, mongoPort, serverSelectionTimeoutMS=1000)

# PASO 2: Conexión a la base de datos
db = mongoClient["tfg_project"]
#NOTA: dentro de la base de datos se encuentran las colecciones.

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection_repo = db["Repositories"]
collection_commit = db["Commits"]

Repositories = []
dataRepositories = []

# Get the names of the repositories with UML files and without UML files. 
def getTypeRepos(repo):
  filesUML=['.uml','uml/','/uml', '_uml', 'uml_','-uml','uml-' '/UML','UML/','UML.', '.UML','-UML','UML-', '_UML', 'UML_']
  for item in collection_commit.find({"origin": repo}):
    for files in item['data']['files']:
      typefile = files['file']
      for f in filesUML:
        if (repo == item['origin']) and (f in typefile):
            return "UML"

  for item in collection_commit.find({"origin": repo}):
    for files in item['data']['files']:
      typefile = files['file']
      for f in filesUML:
        if (repo == item['origin']) and (f not in typefile):
          return "NOUML"

# Get the names of all repositories 
def getRepositories(collection):
  for data in collection.find({}):
    if not(data['origin']) in Repositories:
      Repositories.append(data['origin'])  
  return Repositories

def getOwner(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['search_fields']['owner']
  
def getRepo(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['search_fields']['repo']

def getLanguage(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']['language']

def getLicense(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']['license']

def getTypeDeveloper(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']['owner']['type']

def getFork(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']['forks']

def getSize(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']['size']

def getStars(repo):
  for item in collection_repo.find({"origin": repo[:-4]}):
    return item['data']["stargazers_count"]


# Get the names of all repositories 
def getDataRepo(repo):
  dataRepository = {
    "url": repo,
    "typeRepository": getTypeRepos(repo),
    "owner": getOwner(repo),
    "repo": getRepo(repo),
    "language": getLanguage(repo),
    "license": getLicense(repo),
    "typeDeveloper": getTypeDeveloper(repo),
    "fork": getFork(repo),
    "size": getSize(repo),
    "stars": getStars(repo)
  }

    # if len(dataRepositories) == 0:
    #     dataRepositories.append(dataRepository)
    # else:
    #   if not any(dataRepository == diccionario for diccionario in dataRepositories):
  dataRepositories.append(dataRepository)
    # print(dataRepositories)
  return dataRepositories

try:
  # data_repos = getRepositories(collection_repo)
  repo_commits = getRepositories(collection_commit)
  print(len(repo_commits))
  for repo in repo_commits:
    getDataRepo(repo)
  # print("repoofiin")



except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
  print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
  print("Fallo al conectarse a mongodb "+errorConexion)

# print(dataRepositories)
# print(len(dataRepositories))

