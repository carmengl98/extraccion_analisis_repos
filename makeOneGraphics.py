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


# Data pull from the repositories
reposUML = AnalysisBBDD.getNumRepos(True)
reposNOUML = AnalysisBBDD.getNumRepos(False)
licenseUML = AnalysisBBDD.checkNumLicense(True)
licenseNOUML = AnalysisBBDD.checkNumLicense(False)
developerUML = AnalysisBBDD.checkTypeDeveloper( True)
developerNOUML = AnalysisBBDD.checkTypeDeveloper(False)
forkUML = AnalysisBBDD.checkNumFork(True)
forkNOUML = AnalysisBBDD.checkNumFork(False)
languagesUML = AnalysisBBDD.checkLanguage(True)
languagesNOUML = AnalysisBBDD.checkLanguage(False)
starsUML = AnalysisBBDD.checkNumStars(True)
starsNOUML = AnalysisBBDD.checkNumStars(False)

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
setGraphics(developerUML, developerNOUML, 'Usurios individuales vs Organización')
setGraphics(languagesUML, languagesNOUML, 'Lenguajes principales')
setGraphics(forkUML, forkNOUML, 'Con fork vs Sin fork')
setGraphics(starsUML, starsNOUML, 'Con stars vs Sin stars')

