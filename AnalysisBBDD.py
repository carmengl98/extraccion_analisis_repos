import pymongo
from pymongo import MongoClient
import numpy as np
# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoHost= "localhost"
mongoPort=27017
mongoClient = MongoClient(mongoHost,mongoPort,serverSelectionTimeoutMS=1000)

# PASO 2: Conexión a la base de datos
db = mongoClient["tfg_project"]
#NOTA: dentro de la base de datos se encuentran las colecciones.

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection_analysis = db["data_analysis"]


# check if the developer has a licence
def checkNumLicense(has_UML):
    hasLicense = {
        "Con license": 0,
        "Sin license": 0
    }
    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):  
        if type(item['dataRepository']['license']) is not dict:
            hasLicense["Con license"] += 1
        else:
            hasLicense["Sin license"] += 1
    return hasLicense

# check the type of owner for repository
def checkTypeDeveloper(has_UML):
    typeDeveloper = {
        "User": 0,
        "Organization":0
    }
    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):      
        if (item['dataRepository']['typeDeveloper'] == 'User'):
            typeDeveloper["User"] += 1
        elif(item['dataRepository']['typeDeveloper'] == 'Organization'):
            typeDeveloper["Organization"] += 1
    return typeDeveloper

# check if the number of Fork for repository
def checkNumFork(has_UML):
    hasFork = {
        "Con Fork": 0,
        "Sin Fork":0
    }
    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):      
        if (item['dataRepository']['fork'] != 0):
            hasFork["Con Fork"] += 1
        else:
            hasFork["Sin Fork"] += 1
    return hasFork

# check the size for repository
def checkNumSize(has_UML):
    numSize = []
    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):  
        if (item['dataRepository']['size']):
            numSize.append(item['dataRepository']['size'])
        else:
            numSize.append(0)
    return numSize

# check the number of commits for repository
def checkNumStars(has_UML):
    hasStars = {
        "Con Stars": 0,
        "Sin Stars":0
    }
    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):      
        if (item['dataRepository']['stars'] != 0):
            hasStars["Con Stars"] += 1
        else:
            hasStars["Sin Stars"] += 1
    return hasStars

# Check the repository's language
def checkLanguage(has_UML):
    languages = {
        "JavaScript": 0,
        "Java": 0,
        "Python": 0,
        "C": 0,
        "C++": 0,
        "HTML": 0,
        "PHP": 0,
        "Ruby": 0,
        "TypeScript": 0,
        "Swift": 0,
    }
    other_languages = 0

    for item in collection_analysis.find({'dataRepository.has_UML': has_UML}):
        language = item['dataRepository']['language']
        if language in languages:
            languages[language] += 1
        else:
            other_languages += 1

    languages["Otros"] = other_languages

    return languages


# ----------------------------     COMMITS   ------------------------------

# check the number of commits for repository
def checkNumCommit(has_UML):
    numCommit = []
    for item in collection_analysis.find({"dataCommits.has_UML": has_UML}):   
        if (item['dataCommits']['commit']):
            numCommit.append(item['dataCommits']['commit'])
    return numCommit

# check the number of colaborators for repository
def checkNumContributors(has_UML):
    numContributors = []
    for item in collection_analysis.find({"dataCommits.has_UML": has_UML}):     
        if (item['dataCommits']['contributors']):
            numContributors.append(item['dataCommits']['contributors'])
    return numContributors


def getNumRepos(has_UML):    
   return {"Número de repositorios":collection_analysis.count_documents({"dataRepository.has_UML": has_UML})}

def getRoundPercentage(porcentaje):
    porcentaje_multi = porcentaje * 100
    porcentaje_redondeado = round(porcentaje_multi, 2)
    return "{:.2f}%".format(porcentaje_redondeado)

def getPercentage(has_UML):
        numRepos = collection_analysis.count_documents({"dataRepository.has_UML": has_UML})
        
        numLicense = checkNumLicense(has_UML)
        namesLanguage = checkLanguage(has_UML)
        typeDevelopers = checkTypeDeveloper(has_UML)
        numforks = checkNumFork(has_UML)
        numSize = checkNumSize(has_UML)
        numStars = checkNumStars(has_UML)
        numCommits = checkNumCommit(has_UML)
        numContributors = checkNumContributors(has_UML)
        # print("*****************************************************************")
        # num_doc = collection_analysis.count_documents({})
        # print("NUMERO DE DOC: ",  num_doc)
       
        # print("NUMERO DE REPOS "  ": ", numRepos)
        
        # print("*****************************************************************")

        # for language, count in namesLanguage.items():
        #         print(language + ':', count , '-->', getRoundPercentage(count/numRepos))

        # print("Con License: ", numLicense['Con license'] , '-->', getRoundPercentage( numLicense['Con license']/numRepos))
        # print("Sin License: ", numLicense['Sin license'] , '-->', getRoundPercentage( numLicense['Sin license']/numRepos))
        # print("User: ", typeDevelopers['User'] , '-->', getRoundPercentage( typeDevelopers['User']/numRepos))
        # print("Organization: ", typeDevelopers['Organization'] , '-->', getRoundPercentage( typeDevelopers['Organization']/numRepos))
        # print("Con Fork: ", numforks['Con Fork'] , '-->', getRoundPercentage( numforks['Con Fork']/numRepos))
        # print("Sin Fork: ", numforks['Sin Fork'] , '-->', getRoundPercentage( numforks['Sin Fork']/numRepos))
        # print("Con Stars: ", numStars['Con Stars'] , '-->', getRoundPercentage( numStars['Con Stars']/numRepos))
        # print("Sin Stars: ", numStars['Sin Stars'] , '-->', getRoundPercentage( numStars['Sin Stars']/numRepos))
    

        # print("numSize: ", len(numSize), '-->', np.mean(numSize))
        # print("numCommits: ", len(numCommits), '-->', np.mean(numCommits))
        # print("numContributors: ", len(numContributors), '-->', np.mean(numContributors))

     
getPercentage(True)
# print("*****************************************************************")
getPercentage(False)

# PASO 4:(Create-Read-Update-Delete)
# PASO FINAL: Cerrar la conexion
# mongoClient.close()

