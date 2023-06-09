import collections
from fileinput import close
import pymongo
from pymongo import MongoClient
from datetime import datetime

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
#client = pymongo.MongoClient("mongodb://localhost:27017/")
mongoClient = MongoClient('localhost',27017)

# PASO 2: Conexión a la base de datos
db = mongoClient["tfg_project"]

# PASO 3: Obtenemos una coleccion para trabajar con ella
collection = db["repositories"]
collection2 = db["commits"]

###########################   EJEMPLOS  ###########################

# PASO 4:(Create-Read-Update-Delete)

#num_doc = collection2.count_documents({})
#print("NUMERO DE DOC: ",  num_doc)

def suma(type, lines):
  total = 0
  for num in range(len(lines)):
    if (lines[num] != "-" or lines == 'None'):
      if(type =='added'):
        total = total + int(lines)
      elif(type =='removed'): 
        total = total + int(lines)
  
  return total
  

for data in collection.find({"category": "commit"}):
  num_change =len(data['data']['files'])
  print(" ------------>  Num Commit: ", num_change)
  
  for i in range(num_change):
    #print(data['data']['files'][i]['file'])
    typefile = data['data']['files'][i]['file'].split(".")
    if typefile[1] == 'uml':
      
      #print(data['origin'])
      #if not(data['data']['Author'] in UML): 
      UML = {
          'author_name': data['data']['Author'],
          'author_email': data['data']['Author'],
          'commit': data['data']['commit'],
          'commit_date': data['data']['CommitDate'], 
          'message': data['data']['message'], 
        }
      UML['added'] = suma('added', data['data']['files'][i]['added']) 
      UML['removed'] = suma('removed', data['data']['files'][i]['removed'])
      print("----> UML added: ", data['data']['files'][i]['added'])
      print("----> UML removed: ", data['data']['files'][i]['removed'])

    else:
      #if not(data['data']['Author'] in noUML): 
      noUML = {
        'author_name': data['data']['Author'],
        'author_email': data['data']['Author'],
        'commit': data['data']['commit'],
        'commit_date': data['data']['CommitDate'],
        'message': data['data']['message'], 
                        
        }

      noUML['added'] = suma('added', data['data']['files'][i]['added']) 
      noUML['removed'] = suma('removed', data['data']['files'][i]['removed'])
  
      print("noUML added: ", data['data']['files'][i]['added'])
      #print("noUML removed: ", data['data']['files'][i]['removed'])

    #data.append({data['data']['files'][i]['file']})

print("*****  CON FICHEROS UML  *****")
print("DATOS UML:", UML)
print(" ")
print("*****  SIN FICHEROS UML  *****")
print("DATOS noUML:", noUML)


#print(UML.get('commit'))

# PASO FINAL: Cerrar la conexion
mongoClient.close()




