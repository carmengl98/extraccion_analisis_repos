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
           
# def insertCommitData(repos):
#     # PASO 2: Conexión a la base de datos
#     # PASO 3: Obtenemos una coleccion para trabajar con ella
#     collection_commit=mydb["dataDicc_commit"]
#     print(len(repos))
#     for i in range(len(repos)):
#             collection_commit.insert_one({
#                  "dataCommit": PullDataCommits.getDataCommit(repos)[i],
#                 })


def insertRepoData(repos):
    # PASO 2: Conexión a la base de datos
    # PASO 3: Obtenemos una coleccion para trabajar con ella
    collection_repo=mydb["dataDicc_repo"]
    print(len(repos))
    for i in range(400):
        collection_repo.insert_one({
                "dataRepository": PullDataRepos.getDataRepo(repos)[i],
            })
   
try:
    print("fh")
    repos = PullDataRepos.Repositories
    insertRepoData(repos)
    # insertCommitData(repos)
    print("finish2")


    # PASO 4:(Create-Read-Update-Delete)
    # PASO FINAL: Cerrar la conexion
    mongoClient.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)

