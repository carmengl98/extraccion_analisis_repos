from pathlib import Path
import PullTypeFiles

jsonsCommit_UML = "./archivos_json/Repositorios_UML/commit"
jsonsCommit_NOUML = "./archivos_json/Repositorios_NOUML/commit"
array1 = []
array2 = []
array3 = []
array4 = []

for file1_uml in Path(jsonsCommit_UML).glob("*.json"):
    if not(file1_uml) in PullTypeFiles.ReposUML:
        array1.append(file1_uml)
print (len(array1))

for file1_nouml in Path(jsonsCommit_NOUML).glob("*.json"):
    if not(file1_nouml) in PullTypeFiles.ReposNOUML:
        array2.append(file1_nouml)
print (len(array2))

jsonsRepository_UML = "./archivos_json/Repositorios_UML/repository"
jsonsRepository_NOUML = "./archivos_json/Repositorios_NOUML/repository"

for file_uml in Path(jsonsRepository_UML).glob("*.json"):
    if not(file_uml) in PullTypeFiles.ReposUML:
        array3.append(file_uml)
print (len(array3))

for file_nouml in Path(jsonsRepository_NOUML).glob("*.json"):
    if not(file_nouml) in PullTypeFiles.ReposNOUML:
       array4.append(file_nouml)
print (len(array4))
