from fileinput import close
import pymongo
from pymongo import MongoClient

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017
#mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
mongoClient = MongoClient(mongoHost,mongoPort,serverSelectionTimeoutMS=1000)

# PASO 2: Conexión a la base de datos
db = mongoClient["tfg_project"]
#NOTA: dentro de la base de datos se encuentran las colecciones.

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db["Commits"]


Repositories = []
dataCommits = []


# Get the number of commits by repository
def getNumCommit(repo):
    num = 0
    for item in collection.find({"origin": repo}):
      if repo == item['origin']:
        num += 1 
    return num

    
# Get the names of the repositories with UML files and without UML files. 
def getTypeRepos(repo):
  filesUML=['.uml','uml/','/uml', '_uml', 'uml_','-uml','uml-' '/UML','UML/','UML.', '.UML','-UML','UML-', '_UML', 'UML_']
  for item in collection.find({"origin": repo}):
    for files in item['data']['files']:
      typefile = files['file']
      for f in filesUML:
        if (repo == item['origin']) and (f in typefile):
          return "UML"
  
  for item in collection.find({"origin": repo}):
      for files in item['data']['files']:
        typefile = files['file']
        for f in filesUML:
          if (repo == item['origin']) and (f not in typefile):
            return "NOUML" 


# Get the names of all contributors
def getContributors(repo):
  contributors = set()
  for item in collection.find({"origin": repo}): 
    contributors.add(item['data']['Author'])
  return len(contributors)
 

# Get the names of all repositories 
def getRepositories(collection):
  for item in collection.find({}):
    if not(item['origin']) in Repositories:
      Repositories.append(item['origin'])
  return Repositories


def getDataCommit(repo):
    # print('commit')
    dataAllCommits = {
      "url": repo,
      "typeRepository": getTypeRepos(repo),
      "contributors": getContributors(repo),
      "commit": getNumCommit(repo)
    }
    dataCommits.append(dataAllCommits)
    return dataCommits



try:
  repos = getRepositories(collection)
  for repo in repos:
    getDataCommit(repo)

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
  print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
  print("Fallo al conectarse a mongodb "+errorConexion)

# print(dataCommits)
# print(len(dataCommits))




