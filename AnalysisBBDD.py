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
dataDicc_repo = db["dataDicc_repos"]
dataDicc_commit = db["dataDicc_commit"]


# --------------------------      REPOSITORIES     ----------------------------

# check if the developer has a licence
def checkLicense(collection, developer):
    licenses = {}
    sin_license = 0
    for item in collection.find({"dataRepository.typeRepository": developer}):
        license_data = item['dataRepository']['license']
        if license_data != None:
            license_name = license_data['name']
            if license_name in licenses:
                licenses[license_name] += 1
            else:
                licenses[license_name] = 1
        else:
            sin_license += 1

    licenses['sin license'] = sin_license
    return licenses


def checkTypeDeveloper(collection, developer):
    typeDeveloper = {
        "User": 0,
        "Organization":0
    }
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['typeDeveloper'] == 'User'):
            typeDeveloper["User"] += 1
        elif(item['dataRepository']['typeDeveloper'] == 'Organization'):
            typeDeveloper["Organization"] += 1
    return typeDeveloper

# check if the number of Fork for repository
def checkNumFork(collection, developer):
    numFork = []
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['fork']):
           numFork.append(item['dataRepository']['fork'])
    return numFork

# check the size for repository
def checkNumSize(collection, developer):
    numSize = []
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['size']):
            numSize.append(item['dataRepository']['size'])
    return numSize

# check the number of commits for developer
def checkNumStars(collection, developer):
    numStars = []
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['stars']):
            numStars.append(item['dataRepository']['stars'])
    return numStars

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
        "Pascal": 0,
        "Swift": 0,
    }
    other_count = 0

    for item in collection.find({"dataRepository.typeRepository": developer}):
        language = item['dataRepository']['language']
        if language in languages:
            languages[language] += 1
        else:
            other_count += 1

    languages["sin license"] = other_count

    return languages

#     ###### COMPROBAAARR!!!!!
# elif  item['Language'] == "D, Perl, ColdFusion, CSS, Ruby, Batchfile, Pascal, Objective-C, Makefile":
        #     # repoMeatSimModel repoSE_Alberta, repoTDA593-MIRAR LENGUAGE


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
        # numRepos = collection.count_documents({"dataRepository.typeRepository": developer})
        numRepos = 400
        namesLicense = checkLicense(dataDicc_repo,developer)
        typeDevelopers = checkTypeDeveloper(dataDicc_repo, developer)
        numforks = checkNumFork(dataDicc_repo,developer)
        numSize = checkNumSize(dataDicc_repo,developer)
        numStars = checkNumStars(dataDicc_repo,developer)
        language = checkLanguage(dataDicc_repo,developer)
   
        numCommits = checkNumCommit(dataDicc_repo, developer)
        
        print("----------------------------------------------------------------------------------")
        num_doc = dataDicc_repo.count_documents({})
        print("NUMERO DE DOC: ",  num_doc)
       
        print("NUMERO DE REPOS " + developer +": ", numRepos)
        # print("D " + developer +": ",numRepos/num_doc)
        
        
     
        for license, count in namesLicense.items():
            print(license + ':', count)

        return license

        # UML ---->POR AHORA LOS D UML SON DESARROLLADORES DE TYPE USER
        # NOUML ---->POR AHORA LOS D NOUML SON DESARROLLADORES DE TYPE ORGANIZATION
        # print("----------------------------------------------------------------------------------")
        # print("D " + developer + " CON LICENCIA: ", getRoundPercentage(License["Con licencia"]/numRepos))
        # print("D "+ developer + " SIN LICENCIA: ", getRoundPercentage(License["Sin licencia"]/numRepos))
        # print("D " + developer + " TYPE USER : ", getRoundPercentage(typeDeveloper["Usuario"]/numRepos))
        # print("D " + developer + "  TYPE ORGANIZATION: ", getRoundPercentage(typeDeveloper["Organización"]/numRepos))
        # print("D " + developer + " NUM COMMITS: ", getRoundPercentage(numCommit["Commits"]/numRepos))
        print("D " + developer + " CON FORK: ", getRoundPercentage(fork/numRepos))
        # print("D " + developer + " SIN FORK: ", getRoundPercentage(fork["Sin Fork"]/numRepos))
        # print("D " + developer + " JavaScript: ", getRoundPercentage(language["JavaScript"]/numRepos))
        # print("D " + developer + " Java: ", getRoundPercentage(language["Java"]/numRepos))
        # print("D " + developer + " Python: ", getRoundPercentage(language["Python"]/numRepos))
        # print("D " + developer + " C: ", getRoundPercentage(language["C"]/numRepos))
        # print("D " + developer + " C++: ", getRoundPercentage(language["C++"]/numRepos))
        # print("D " + developer + " HTML: ", getRoundPercentage(language["HTML"]/numRepos))
        # print("D " + developer + " PHP: ", getRoundPercentage(language["PHP"]/numRepos))
        # print("D " + developer + " Ruby: ",  getRoundPercentage(language["Ruby"]/numRepos))
        # print("D " + developer + " Pascal: ", getRoundPercentage(language["Pascal"]/numRepos))
        # print("D " + developer + " Swift: ", getRoundPercentage(language["Swift"]/numRepos))
        # print("D " + developer + " Otros: ", getRoundPercentage(language["Otros"]/numRepos))
        # # print("D  " + developer + " D, CSS, PASCAL: ", getRoundPercentage(Ruby/numRepos))
        
     
getPercentage('UML')
getPercentage('NOUML')

# PASO 4:(Create-Read-Update-Delete)
# PASO FINAL: Cerrar la conexion
mongoClient.close()

