from pathlib import Path
import subprocess


jsonsCommit_UML = "./extraccion_analisis_repos/archivos_json/Repositorios_UML/commit"
jsonsCommit_NOUML = "./extraccion_analisis_repos/archivos_json/Repositorios_NOUML/commit"


for file_uml in Path(jsonsCommit_UML).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Commits", str(file_uml.absolute())
     ]
    subprocess.Popen(cmd)


for file_nouml in Path(jsonsCommit_NOUML).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Commits", str(file_nouml.absolute())
    ] 
    subprocess.Popen(cmd)

