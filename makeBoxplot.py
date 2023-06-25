import numpy as np
import matplotlib.pyplot as plt
import AnalysisBBDD
# from pymongo import MongoClient

# # PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
# mongoHost= "localhost"
# mongoPort=27017

# mongoClient = MongoClient(mongoHost,mongoPort,serverSelectionTimeoutMS=1000)

# # PASO 2: Conexión a la base de datos
# db = mongoClient["tfg_project"]
# #NOTA: dentro de la base de datos se encuentran las colecciones.


commitUML = AnalysisBBDD.checkNumCommit(True)
commitNOUML = AnalysisBBDD.checkNumCommit(False)
contributorsUML = AnalysisBBDD.checkNumContributors(True)
contributorsNOUML = AnalysisBBDD.checkNumContributors(False)
sizeUML = AnalysisBBDD.checkNumSize(True)
sizeNOUML = AnalysisBBDD.checkNumSize(False)


def setBoxplot(data, label, xlabel, ylabel, limit):
    # Prepara los datos para el diagrama de caja.
    plt.boxplot(data, whis=1)
    plt.ylim(bottom=0,top=limit) # Establecer el límite máximo en el eje y

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(label)
    plt.show()


setBoxplot(commitUML, 'Diagrama de Caja del número de commits UML', 'Repositorios','Número de commits', limit=4000)
setBoxplot(commitNOUML, 'Diagrama de Caja del número de commits NOUML','Repositorios','Número de commits', limit=4000)
setBoxplot(contributorsUML,'Diagrama de Caja del número de colaboradores UML','Repositorios', 'Número de colaboradores', limit=100)
setBoxplot(contributorsNOUML,'Diagrama de Caja del número de colaboradores NOUML', 'Repositorios', 'Número de colaboradores', limit=100)
setBoxplot(sizeUML,'Diagrama de Caja del tamaño de los repositorios  UML','Repositorios','Tamaño del repositorio', limit=140000)
setBoxplot(sizeNOUML,'Diagrama de Caja del tamaño de los repositorios NOUML', 'Repositorios', 'Tamaño del repositorio', limit=140000)


