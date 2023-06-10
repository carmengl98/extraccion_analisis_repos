from pathlib import Path
import subprocess

jsonsRepository_UML = "./extraccion_analisis_repos/archivos_json/Repositorios_UML/repository"
jsonsRepository_NOUML = "./extraccion_analisis_repos/archivos_json/Repositorios_NOUML/repository"


for file_uml in Path(jsonsRepository_UML).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Repositories","--file", str(file_uml.absolute())
     ]
    subprocess.Popen(cmd)

for file_nouml in Path(jsonsRepository_NOUML).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Repositories","--file", str(file_nouml.absolute())
    ] 
    subprocess.Popen(cmd)
    
    