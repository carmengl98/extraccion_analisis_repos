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
data_repoUML = db["data_repoUML"]
data_repoNOUML = db["data_repoNOUML"]
data_commit = db["data_commit"]

# Data pull from the repositories
reposUML = AnalysisBBDD.getNumRepos(data_repoUML ,'UML')
reposNOUML = AnalysisBBDD.getNumRepos(data_repoNOUML ,'NOUML')
licenseUML = AnalysisBBDD.checkLicense(data_repoUML ,'UML')
licenseNOUML = AnalysisBBDD.checkLicense(data_repoNOUML ,'NOUML')
developerUML = AnalysisBBDD.checkTypeDeveloper(data_repoUML , 'UML')
developerNOUML = AnalysisBBDD.checkTypeDeveloper(data_repoNOUML, 'NOUML')
forkUML = AnalysisBBDD.checkNumFork(data_repoUML ,'UML')
forkNOUML = AnalysisBBDD.checkNumFork(data_repoNOUML ,'NOUML')
languagesUML = AnalysisBBDD.checkLanguage(data_repoUML ,'UML')
languagesNOUML = AnalysisBBDD.checkLanguage(data_repoNOUML ,'NOUML')
starsUML = AnalysisBBDD.checkNumStars(data_repoUML ,'UML')
starsNOUML = AnalysisBBDD.checkNumStars(data_repoNOUML ,'NOUML')


numUML= reposUML['Número de repositorios']
numNOUML= reposNOUML['Número de repositorios']

print(licenseUML)
print(licenseNOUML)
# print(developerUML)
# print(developerNOUML)
print(forkUML)
print(forkNOUML)
# print(languagesUML)
# print(languagesNOUML)

def setGraphics(datosUML, datosNOUML, title):
    
    # Ajustar la posición de las barras
    bar_width = 0.35

    # Obtener las etiquetas y los valores a partir del diccionario
    etiquetas = list(datosUML.keys())
    valoresUML = list(datosUML.values())
    valoresNOUML = list(datosNOUML.values())
    
    total = sum(valoresUML+ valoresNOUML)
    porcentajes_UML = [valor/total* 100 for valor in valoresUML]
    porcentajes_NOUML = [valor/total * 100 for valor in valoresNOUML]
    print(porcentajes_UML)
    print(porcentajes_NOUML)
    # Crear una lista de índices para la posición de las barras
    index = np.arange(len(etiquetas))

    # Crear gráfico de barras juntas
    plt.bar(index, porcentajes_UML, bar_width, bottom=porcentajes_NOUML, label='UML', color='#3366FF')
    plt.bar(index, porcentajes_NOUML, bar_width, label='NO UML', color='#87CEFA')
    
    plt.title(title)
    plt.ylabel('Repositorios')
    
    # Aplicar el formateador al eje y
    plt.gca().set_yticklabels(['{:.0f}%'.format(valor) for valor in plt.gca().get_yticks()])
    # Crear gráfico de barras juntas
    plt.xticks(index, etiquetas)

    plt.legend()

    # Ajustar el espaciado entre las barras
    plt.tight_layout()

    # Mostrar el gráfico
    plt.show()

setGraphics(licenseUML, licenseNOUML, 'Con licencia vs Sin licencia')
# setGraphics(developerUML, developerNOUML, 'Usurios individuales vs Organización')
# setGraphics(languagesUML, languagesNOUML, 'Lenguajes principales')
# setGraphics(forkUML, forkNOUML, 'Con fork vs Sin fork')
# setGraphics(starsUML, starsNOUML, 'Con stars vs Sin stars')
