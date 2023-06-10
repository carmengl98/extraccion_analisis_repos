import numpy as np
import matplotlib.pyplot as plt
import AnalysisBBDD
import pymongo
from pymongo import MongoClient

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

commitUML = AnalysisBBDD.checkNumCommit(dataDicc_commit,'UML')
commitNOUML = AnalysisBBDD.checkNumCommit(dataDicc_commit,'NOUML')
contributorsUML = AnalysisBBDD.checkNumContributors(dataDicc_commit ,'UML')
contributorsNOUML = AnalysisBBDD.checkNumContributors(dataDicc_commit ,'NOUML')
forkUML = AnalysisBBDD.checkNumFork(dataDicc_repo ,'UML')
forkNOUML = AnalysisBBDD.checkNumFork(dataDicc_repo ,'NOUML')
sizeUML = AnalysisBBDD.checkNumSize(dataDicc_repo ,'UML')
sizeNOUML = AnalysisBBDD.checkNumSize(dataDicc_repo ,'NOUML')
starsUML = AnalysisBBDD.checkNumStars(dataDicc_repo ,'UML')
starsNOUML = AnalysisBBDD.checkNumStars(dataDicc_repo ,'NOUML')

print(forkUML)
print(forkNOUML)
print(' ')
print(sizeUML)
print(sizeNOUML)
print(' ')
print(starsUML)
print(starsNOUML)

def setBoxplot(data, label, limit):
    # Prepara los datos para el diagrama de caja.
    plt.boxplot(data, whis=1)
    plt.ylim(bottom=0,top=limit) # Establecer el límite máximo en el eje y

    plt.xlabel('Datos')
    plt.ylabel('Valores')
    plt.title(label)
    plt.show()


setBoxplot(commitUML, 'Diagrama de Caja del número de commits UML',limit=1000)
setBoxplot(commitNOUML, 'Diagrama de Caja del número de commits NOUML',limit=8000)
setBoxplot(contributorsUML,'Diagrama de Caja del número de colaboradores UML', limit=100)
setBoxplot(contributorsNOUML,'Diagrama de Caja del número de colaboradores NOUML', limit=250)
setBoxplot(forkUML,'Diagrama de Caja del número de fork por repositorios UML', limit=200)
setBoxplot(forkNOUML,'Diagrama de Caja del número de fork por repositorios NOUML', limit=200)
setBoxplot(sizeUML,'Diagrama de Caja del tamaño de los repositorios  UML', limit=500)
setBoxplot(sizeNOUML,'Diagrama de Caja del tamaño de los repositorios NOUML', limit=500)
setBoxplot(starsUML,'Diagrama de Caja del número de stars UML', limit=500)
setBoxplot(starsNOUML,'Diagrama de Caja del número de stars NOUML', limit=8050)


