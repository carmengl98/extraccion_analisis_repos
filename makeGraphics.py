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

# Data pull from the repositories
reposUML = AnalysisBBDD.getNumRepos(dataDicc_repo ,'UML')
reposNOUML = AnalysisBBDD.getNumRepos(dataDicc_repo ,'NOUML')
licenseUML = AnalysisBBDD.checkLicense(dataDicc_repo ,'UML')
licenseNOUML = AnalysisBBDD.checkLicense(dataDicc_repo ,'NOUML')
developerUML = AnalysisBBDD.checkTypeDeveloper(dataDicc_repo , 'UML')
developerNOUML = AnalysisBBDD.checkTypeDeveloper(dataDicc_repo, 'NOUML')
forkUML = AnalysisBBDD.checkFork(dataDicc_repo ,'UML')
forkNOUML = AnalysisBBDD.checkFork(dataDicc_repo ,'NOUML')
languagesUML = AnalysisBBDD.checkLanguage(dataDicc_repo ,'UML')
languagesNOUML = AnalysisBBDD.checkLanguage(dataDicc_repo ,'NOUML')



numUML= reposUML['Número de repositorios']
numNOUML= reposNOUML['Número de repositorios']
print(numUML)
print(numNOUML)


def setGraphics(datosUML, datosNOUML, title):
    
    # Ajustar la posición de las barras
    bar_width = 0.35

    # Obtener las etiquetas y los valores a partir del diccionario
    etiquetas = list(datosUML.keys())
    valoresUML = list(datosUML.values())
    valoresNOUML = list(datosNOUML.values())

    # Crear una lista de índices para la posición de las barras
    index = np.arange(len(etiquetas))

    # Crear gráfico de barras separadas
    plt.bar(index, valoresUML, bar_width, label='UML', color='green')
    plt.bar(index + bar_width, valoresNOUML, bar_width, label='NO UML', color='blue')
    
    # Personalizar el gráfico
    if (etiquetas != ["Commits"]):
        # Establecer el rango del eje y
        plt.ylim(0, 200)

    plt.title(title)
    # plt.xlabel('Categorías')
    plt.ylabel('Repositorios')
    plt.xticks(index + bar_width/2, etiquetas)
    plt.legend()

    # Ajustar el espaciado entre las barras
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

setGraphics(licenseUML, licenseNOUML, 'Con licencia vs Sin licencia')
setGraphics(developerUML, developerNOUML, 'Usurios vs Organización')
setGraphics(forkUML, forkNOUML, 'Con fork vs Sin fork')
setGraphics(languagesUML, languagesNOUML, 'Lenguajes principales')
setGraphics(forkUML, forkNOUML, 'Con fork vs Sin fork')