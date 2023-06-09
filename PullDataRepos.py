import pymongo
from pymongo import MongoClient
import PullTypeFiles


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

# Get the names of all repositories 
def getDataRepo(repos):
  # for item in collection.find({"origin": repo}):
  for repo in repos:
    for item in collection_repo.find({"origin": repo[:-4]}):
      # print(item)
      dataRepository = {
        "url": repo,
        "typeRepository": PullTypeFiles.getTypeRepos(repo),
        "owner": item['search_fields']['owner'],
        "repo": item['search_fields']['repo'],
        "language": item['data']['language'],
        "license": item['data']['license'],
        "typeDeveloper": item['data']['owner']['type'],
        "fork": item['data']['forks'],
        "size": item['data']['size'],
        "stars": item['data']["stargazers_count"]
      }

      if len(dataRepositories) == 0:
        dataRepositories.append(dataRepository)
      else:
        if not any(dataRepository == diccionario for diccionario in dataRepositories):
          dataRepositories.append(dataRepository)
      # print(dataRepositories)
  return dataRepositories

# try:
#   # data_repos = getRepositories(collection_repo)
  # data_commits = getRepositories(collection_commit)
  # print("repoo")

  # # for repo in data_commits:
  # #   PullTypeFiles.getTypeRepos(repo)
  # # print(PullTypeFiles.ReposUML)

  # for repo in data_commits:
  # getDataRepo(data_commits)
  # print("repoofiin")



# except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
#   print("Tiempo exedido "+errorTiempo)
# except pymongo.errors.ConnectionFailure as errorConexion:
#   print("Fallo al conectarse a mongodb "+errorConexion)

# print(dataRepositories)
# print(len(dataRepositories))

