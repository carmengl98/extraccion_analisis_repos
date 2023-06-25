from pathlib import Path
import subprocess


jsonsCommit = "./archivos/commit"


for files in Path(jsonsCommit).glob("*.json"):
    cmd = [
        "mongoimport", "--db", "tfg_project", "--collection", "Commits", str(files.absolute())
     ]
    subprocess.Popen(cmd)


