from pymongo import MongoClient

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017

mongoClient = MongoClient(mongoHost, mongoPort, serverSelectionTimeoutMS=1000)

# Conexión a la base de datos
db = mongoClient["tfg_project"]
collection = db["dataDicc_commit"]

# Cambiar el nombre del campo en todos los documentos
# collection.update_many({}, {'$rename': {'dataRepository': 'dataCommit'}})
collection.delete_many({"dataCommit.url": "https://github.com/c00ler/transfer-service.git"})



