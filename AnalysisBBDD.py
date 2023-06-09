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
dataDicc_commit = db["dataDicc_commit"]



# check if the developer has a licence
def checkLicense(collection, developer):
    conlicense = 0
    sinlicense = 0
    for item in collection.find({"Desarrollador": developer}):
        if (item['License'] != None):
            conlicense += 1
        if (item['License'] == None):
            sinlicense += 1
    return {"Con licencia":conlicense,"Sin licencia": sinlicense}


def checkTypeDeveloper(collection, developer):
    user = 0
    organization = 0
    for item in collection.find({"Desarrollador": developer}):      
        if (item['TypeDeveloper'] == 'User'):
            user += 1
        elif(item['TypeDeveloper'] == 'Organization'):
            organization += 1
    return {"Usuario": user,"Organización": organization}

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

# check the size for repository
def checkNumSize(collection, developer):
    numSize = []
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['size']):
            numSize.append(item['dataRepository']['size'])
    return numSize


# check the number of commits for developer
def checkNumSitars(collection, developer):
    numStars = []
    for item in collection.find({"dataRepository.typeRepository": developer}):      
        if (item['dataRepository']['stars']):
            numStars.append(item['dataRepository']['stars'])
    return numStars

# check if the developer has a Fork
def checkFork(collection, developer):
    conFork = 0
    sinFork = 0
    for item in collection.find({"Desarrollador": developer}):      
        if (item['Fork'] != 0):
            conFork += 1
        else:
            sinFork += 1
    return {"Con Fork": conFork,"Sin Fork": sinFork}

# Check the developer's language
def checkLanguage(collection, developer):
    Javascript = 0
    Python = 0
    C = 0
    Cpp = 0
    Java = 0
    Php = 0
    Ruby = 0
    Pascal = 0
    Html = 0
    Swift = 0
    Otros = 0
    for item in collection.find({"Desarrollador": developer}):  
        # print(item['Language'] ) 
        if item['Language'] == "JavaScript":
            Javascript += 1
        elif  item['Language'] == "Java":
            Java += 1
        elif item['Language'] == "Python":
            Python += 1
        elif  item['Language'] == "C":
            C += 1
        elif  item['Language'] == "C++":
            Cpp += 1
        elif item['Language'] == "HTML":
            Html += 1
        elif item['Language'] == "PHP":
            Php += 1
        elif item['Language'] == "Ruby":
            Ruby += 1
        elif item['Language'] == "Pascal":
            Pascal += 1
        elif item['Language'] == "Swift":
            Swift += 1
        elif ((item['Language']!= "JavaScript") and (item['Language']!="Python") and (item['Language']!="Java") and (item['Language']!="PHP")
        and (item['Language']!="Ruby") and (item['Language']!="C") and (item['Language']!="C++") and (item['Language']!="HTML")and (item['Language']!="Swift")):
            Otros += 1
    return {
        "JavaScript": Javascript, 
        "Java": Java, 
        "Python": Python, 
        "C": C, 
        "C++": Cpp, 
        "HTML": Html, 
        "PHP": Php, 
        "Ruby": Ruby, 
        "Pascal": Pascal, 
        "Swift": Swift, 
        "Otros": Otros
    }
#     ###### COMPROBAAARR!!!!!
# elif  item['Language'] == "D, Perl, ColdFusion, CSS, Ruby, Batchfile, Pascal, Objective-C, Makefile":
        #     # repoMeatSimModel repoSE_Alberta, repoTDA593-MIRAR LENGUAGE

def getNumRepos(collection, developer):    
   return {"Número de repositorios":collection.count_documents({"Desarrollador": developer})}

def getRoundPercentage(porcentaje):
    porcentaje_multi = porcentaje * 100
    porcentaje_redondeado = round(porcentaje_multi, 2)
    return "{:.2f}%".format(porcentaje_redondeado)

def getPercentage(developer):
        # numRepos = collection.count_documents({"Desarrollador": developer})
        numRepos = 400
        License = checkLicense(dataDicc_repo,developer)
        typeDeveloper = checkTypeDeveloper(dataDicc_repo, developer)
        numCommit = checkNumCommit(dataDicc_repo, developer)
        fork = checkFork(dataDicc_repo,developer)
        language = checkLanguage(dataDicc_repo,developer)
   
        
        print("----------------------------------------------------------------------------------")
        num_doc = dataDicc_repo.count_documents({})
        print("NUMERO DE DOC: ",  num_doc)
       
        print("NUMERO DE REPOS " + developer +": ", numRepos)
        # print("D " + developer +": ",numRepos/num_doc)
        

         # print(np.mean(License["Con licencia"]) * 100)

        # # #UML ---->POR AHORA LOS D UML SON DESARROLLADORES DE TYPE USER
        # # #NOUML ---->POR AHORA LOS D NOUML SON DESARROLLADORES DE TYPE ORGANIZATION
        # print("----------------------------------------------------------------------------------")
        # print("D " + developer + " CON LICENCIA: ", getRoundPercentage(License["Con licencia"]/numRepos))
        # print("D "+ developer + " SIN LICENCIA: ", getRoundPercentage(License["Sin licencia"]/numRepos))
        # print("D " + developer + " TYPE USER : ", getRoundPercentage(typeDeveloper["Usuario"]/numRepos))
        # print("D " + developer + "  TYPE ORGANIZATION: ", getRoundPercentage(typeDeveloper["Organización"]/numRepos))
        # print("D " + developer + " NUM COMMITS: ", getRoundPercentage(numCommit["Commits"]/numRepos))
        # print("D " + developer + " CON FORK: ", getRoundPercentage(fork["Con Fork"]/numRepos))
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

