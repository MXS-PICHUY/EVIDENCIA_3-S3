#USO DEL EJERCICIO 4 EXAM PA JLCH
#JSON 7
import csv
import json 

myData = [["MATEMATICAS"],
          ['FISICA']]

myData2 = [["JUAN"],
          ['PEPE'],
          ['ALVERTO'],
          ['MAURICIO'],
          ['CARLOS']]
myFile = open('PROMEDIOS_MATEyFISICA.csv','w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myData)
    
print("MATERIAS LISTAS")

print('MATEMATICAS',input('que secastes  '))
print('FISICA',input('que secastes  '))