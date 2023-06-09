import pymongo
from pymongo import MongoClient
import PullDataRepos
# import PullDataCommits


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017

mongoClient = MongoClient(mongoHost, mongoPort, serverSelectionTimeoutMS=1000)
# PASO 2: Conexión a la base de datos
# PASO 3: Obtenemos una coleccion para trabajar con ella
mydb=mongoClient["tfg_project"]
collection=mydb["Commits"]


collection_commit = {}
collection_repo = {}
Repositories = []
Repos = []

# Get the names of all repositories 
def getRepositories(collection):
#   print("hola")
  for item in collection.find({}):
    if not(item['origin']) in Repositories:
      Repositories.append(item['origin'])
  return Repositories

           
# def insertCommitData(repos):
#     # PASO 2: Conexión a la base de datos
#     # PASO 3: Obtenemos una coleccion para trabajar con ella
#     collection_commit=mydb["dataDicc_commit"]
    
#     for item in range(len(repos)):
#             collection_commit.insert_one({
#                  "dataCommit": PullDataCommits.getDataCommit(repos)[item],
#                 })


def insertRepoData(repos):
    # PASO 2: Conexión a la base de datos
    # PASO 3: Obtenemos una coleccion para trabajar con ella
    collection_repo=mydb["dataDicc_repos"]
    
    for item in range(len(repos)):
        collection_repo.insert_one({
                "dataRepository": PullDataRepos.getDataRepo(repos)[item],
            })
   
try:
    print("fh")
    repos = getRepositories(collection)
   
    insertRepoData(repos)
    # insertCommitData(repos)
    print("finish2")

    # for data in collection.find({}):
    #     if not(data['origin']) in Repositories:
    #         Repositories.append(data['origin'])
    
    # for data in collection2.find({}):
    #     if not(data['origin']) in Repos:
    #         Repos.append(data['origin'])
  
    # print("Repos R--> ", len(Repositories))
    # print("Repos C--> ", len(Repos))
    # for r in Repos:
    #     if r not in Repositories:
    #         print (r)

    # PASO 4:(Create-Read-Update-Delete)
    # PASO FINAL: Cerrar la conexion
    mongoClient.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)

