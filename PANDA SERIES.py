import numpy as np
import pandas as pd

SEPARADOR =("*"*20)+"\n"

notas=pd.Series([87,100,85,60,78])
print(type(notas))
print(notas)
print(SEPARADOR)

iguales=pd.Series(100,range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)

print('notas:')
print(f'{notas}')
print(f'cantidad={notas.count()}')
print(f'media={notas.mean()}')
print(f'minimo={notas.min()}')
print(f'maximo={notas.max()}')
print(f'desviacion standard={notas.std()}')
print('Sumarizacion descriptiva:')
print(notas.describe())
print(SEPARADOR)

print('series con indices personalizados')
notas_asignadas=pd.Series([87,100,85,60,70],index=['crescencio','domitila','rutilio','panfilo','ludoviko'])

print(notas_asignadas)
print(SEPARADOR)

print('serie generada a partir de un diccionario')
notas_asignadas_dict=pd.Series({'cresencio':87,'domitila':100,'rutilio':85,'panfilo':60,'ludoviko':78})

print(notas_asignadas_dict)
print(SEPARADOR)

print(f"la calificacion de rutilio es{notas_asignadas_dict['rutilio']}")
print(f'la calificacion de rutilio es{notas_asignadas_dict.rutilio}')





















