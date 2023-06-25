from pathlib import Path
import subprocess

jsonsRepository = "./archivos/repository"


for files in Path(jsonsRepository).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Repositories","--file", str(files.absolute())
     ]
    subprocess.Popen(cmd)


    