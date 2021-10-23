import json 
 
str_json = """
   {
     "nombre": "Juan Perez",
     "edad": 18,
     "pais": "Panama"
    }
""" 
 
json_dat = json.loads(str_json); 
 
print("Objeto tipo diccionario:", json_dat) 