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
dataDicc_repo = db["dataDicc_repo"]
data_commit = db["data_commit"]


# --------------------------      REPOSITORIES     ----------------------------

# check if the developer has a licence
# def checkLicense(collection, developer):
#     licenses = {}
#     sin_license = 0
#     for item in collection.find({}):
#         license_data = item['dataRepository']['license']
#         if license_data != None:
#             license_name = license_data['name']
#             if license_name in licenses:
#                 licenses[license_name] += 1
#             else:
#                 licenses[license_name] = 1
#         else:
#             sin_license += 1

#     licenses['sin license'] = sin_license
#     return licenses

# check if the developer has a licence
def checkLicense(collection, developer):
    hasLicense = {
        "Con license": 0,
        "Sin license": 0
    }
    for item in collection.find({}):  
        if type(item['dataRepository']['license']) is not dict:
            hasLicense["Con license"] += 1
        else:
            hasLicense["Sin license"] += 1
    return hasLicense

# check the type of owner for repository
def checkTypeDeveloper(collection, developer):
    typeDeveloper = {
        "User": 0,
        "Organization":0
    }
    for item in collection.find({}):      
        if (item['dataRepository']['typeDeveloper'] == 'User'):
            typeDeveloper["User"] += 1
        elif(item['dataRepository']['typeDeveloper'] == 'Organization'):
            typeDeveloper["Organization"] += 1
    return typeDeveloper

# check if the number of Fork for repository
def checkNumFork(collection, developer):
    # numFork = []
    hasFork = {
        "Con Fork": 0,
        "Sin Fork":0
    }
    for item in collection.find({}):      
        if (item['dataRepository']['fork'] != 0):
        #    numFork.append(item['dataRepository']['fork'])
            hasFork["Con Fork"] += 1
        else:
            # numFork.append(0)
            hasFork["Sin Fork"] += 1
    return hasFork

# check the size for repository
def checkNumSize(collection, developer):
    numSize = []
    for item in collection.find({}):      
        if (item['dataRepository']['size']):
            numSize.append(item['dataRepository']['size'])
        else:
            numSize.append(0)
    return numSize

# check the number of commits for developer
def checkNumStars(collection, developer):
    numStars = []
    hasStars = {
        "Con Stars": 0,
        "Sin Stars":0
    }
    for item in collection.find({}):      
        if (item['dataRepository']['stars'] != 0):
            # numStars.append(item['dataRepository']['stars'])
            hasStars["Con Stars"] += 1
        else:
            hasStars["Sin Stars"] += 1
    return hasStars

# Check the developer's language
def checkLanguage(collection, developer):
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

    for item in collection.find({}):
        language = item['dataRepository']['language']
        if language in languages:
            languages[language] += 1
        else:
            other_languages += 1

    languages["Otros"] = other_languages

    return languages


# ----------------------------     COMMITS   ------------------------------

# check the number of commits for developer
def checkNumCommit(collection, developer):
    numCommit = []
    for item in collection.find({"dataCommit.typeRepository": developer}):      
        if (item['dataCommit']['commit']):
            numCommit.append(item['dataCommit']['commit'])
    return numCommit

# check the number of colaborators for repository
def checkNumContributors(collection, developer):
    numContributors = []
    for item in collection.find({"dataCommit.typeRepository": developer}):     
        if (item['dataCommit']['contributors']):
            numContributors.append(item['dataCommit']['contributors'])
    return numContributors


def getNumRepos(collection, developer):    
   return {"Número de repositorios":collection.count_documents({"dataRepository.typeRepository": developer})}

def getRoundPercentage(porcentaje):
    porcentaje_multi = porcentaje * 100
    porcentaje_redondeado = round(porcentaje_multi, 2)
    return "{:.2f}%".format(porcentaje_redondeado)

def getPercentage(developer):
        numRepos = dataDicc_repo.count_documents({"dataRepository.typeRepository": developer})
        
        namesLicense = checkLicense(dataDicc_repo,developer)
        namesLanguage = checkLanguage(dataDicc_repo,developer)
        typeDevelopers = checkTypeDeveloper(dataDicc_repo, developer)
        numforks = checkNumFork(dataDicc_repo,developer)
        numSize = checkNumSize(dataDicc_repo,developer)
        numStars = checkNumStars(dataDicc_repo,developer)
        numCommits = checkNumCommit(dataDicc_repo, developer)
        
        # print("*****************************************************************")
        # num_doc = dataDicc_repo.count_documents({})
        # print("NUMERO DE DOC: ",  num_doc)
       
        # print("NUMERO DE REPOS " + developer +": ", numRepos)
        
        # print("*****************************************************************")
        
     
        # for license, count in namesLicense.items():
        #     print(license + ':', count , '-->', getRoundPercentage(count/numRepos))

        # print("---------------------------------------")

        # for language, count in namesLanguage.items():
        #         print(language + ':', count , '-->', getRoundPercentage(count/numRepos))

       
        # print("numforks: ", len(numforks), '-->', np.mean(numforks))
        # print("numSize: ", len(numSize), '-->', np.mean(numSize))
        # print("numStars: ", len(numStars), '-->', np.mean(numStars))
        # print("numCommits: ", len(numCommits), '-->', np.mean(numCommits))

        # print("User: ", typeDevelopers['User'] , '-->', getRoundPercentage( typeDevelopers['User']/numRepos))
        # print("Organization: ", typeDevelopers['Organization'] , '-->', getRoundPercentage( typeDevelopers['Organization']/numRepos))
        
        # # print("D " + developer + " CON LICENCIA: ", getRoundPercentage(License["Con licencia"]/numRepos))
        # # print("D "+ developer + " SIN LICENCIA: ", getRoundPercentage(License["Sin licencia"]/numRepos))
        
        
     
getPercentage('UML')
getPercentage('NOUML')

# PASO 4:(Create-Read-Update-Delete)
# PASO FINAL: Cerrar la conexion
mongoClient.close()

