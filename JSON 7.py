import json 
 
datos = {
    'nombre' : 'Juan Perez',
    'edad'   : 18,
    'pais'   : 'Panama'
} 
 
json_str = json.dumps(datos) 
 
print('Datos en formato JSON:', json_str) 