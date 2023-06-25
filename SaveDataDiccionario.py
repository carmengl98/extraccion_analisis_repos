import pymongo
from pymongo import MongoClient
from tqdm import tqdm
# import PullDataRepos
# # import PullDataCommits


# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017

mongoClient = MongoClient(mongoHost, mongoPort, serverSelectionTimeoutMS=1000)

# PASO 2: Conexión a la base de datos
# PASO 3: Obtenemos una coleccion para trabajar con ella
mydb=mongoClient["tfg_project"]
collection = mydb["data_repo"]

collection_data = {}


def insertData():
    # PASO 2: Conexión a la base de datos
    # PASO 3: Obtenemos una coleccion para intoducir los datos
    collection_data=mydb["data_analysis"]
    
    total_repositories = collection.count_documents({})
    for item in tqdm(collection.find({}), total=total_repositories):
        collection_data.insert_one({
            "dataRepository" : {
            "url": item['origin'],
            "has_UML": item['uml'],
            "owner":item['search_fields']['owner'],
            "repo": item['search_fields']['repo'],
            "language": item['data']['language'],
            "license": item['data']['license'],
            "typeDeveloper": item['data']['owner']['type'],
            "fork": item['data']['forks'],
            "size": item['data']['size'],
            "stars": item['data']["stargazers_count"]
            },
            "dataCommits" : {
                "url": item['origin'],
                "has_UML": item['uml'],
                "contributors": item['num_contributors'],
                "commit": item['num_commits'],
            }
        })

        
   
try:
    print("Start the process")
    insertData()
   
    print("Finish the process")


    # PASO 4:(Create-Read-Update-Delete)
    # PASO FINAL: Cerrar la conexion
    mongoClient.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)

