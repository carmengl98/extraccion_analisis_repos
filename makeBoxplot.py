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
data_commit = db["dataDicc_commit"]

commitUML = AnalysisBBDD.checkNumCommit(data_commit,'UML')
commitNOUML = AnalysisBBDD.checkNumCommit(data_commit,'NOUML')
contributorsUML = AnalysisBBDD.checkNumContributors(data_commit ,'UML')
contributorsNOUML = AnalysisBBDD.checkNumContributors(data_commit ,'NOUML')
forkUML = AnalysisBBDD.checkNumFork(dataDicc_repo ,'UML')
forkNOUML = AnalysisBBDD.checkNumFork(dataDicc_repo ,'NOUML')
sizeUML = AnalysisBBDD.checkNumSize(dataDicc_repo ,'UML')
sizeNOUML = AnalysisBBDD.checkNumSize(dataDicc_repo ,'NOUML')
starsUML = AnalysisBBDD.checkNumStars(dataDicc_repo ,'UML')
starsNOUML = AnalysisBBDD.checkNumStars(dataDicc_repo ,'NOUML')

print(sizeUML)
print(sizeNOUML)
def setBoxplot(data, label, xlabel, ylabel, limit):
    # Prepara los datos para el diagrama de caja.
    plt.boxplot(data, whis=1)
    plt.ylim(bottom=0,top=limit) # Establecer el límite máximo en el eje y

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(label)
    plt.show()


# setBoxplot(commitUML, 'Diagrama de Caja del número de commits UML', 'Repositorios','Número de commits', limit=4000)
# setBoxplot(commitNOUML, 'Diagrama de Caja del número de commits NOUML','Repositorios','Número de commits', limit=4000)
# setBoxplot(contributorsUML,'Diagrama de Caja del número de colaboradores UML','Repositorios', 'Número de colaboradores', limit=100)
# setBoxplot(contributorsNOUML,'Diagrama de Caja del número de colaboradores NOUML', 'Repositorios', 'Número de colaboradores', limit=100)
setBoxplot(sizeUML,'Diagrama de Caja del tamaño de los repositorios  UML','Repositorios','Tamaño del repositorio', limit=140000)
setBoxplot(sizeNOUML,'Diagrama de Caja del tamaño de los repositorios NOUML', 'Repositorios', 'Tamaño del repositorio', limit=140000)


