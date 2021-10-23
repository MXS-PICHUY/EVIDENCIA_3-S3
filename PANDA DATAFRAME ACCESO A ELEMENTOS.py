import pandas as pd
import random
SEPARADOR=('*'*20)+'\n'

diccionario_notas_aleatorias={\
    'crescencio':[random.randrange(60,101) for x in range(3)],\
    'domitila':[80,100,57], 'rutilio':[80,70,57], 'panfilo':[20,100,100],\
    'ludoviko':[100,100,100]}
notas_diccionario=pd.DataFrame(diccionario_notas_aleatorias)
notas_diccionario.index=['programacion','base de datos','contabilidad']

print(notas_diccionario['domitila'])
print()
print(notas_diccionario.domitila)
print(SEPARADOR)

print(notas_diccionario.loc['programacion'])
print()
print(notas_diccionario.loc['bases de datos'])
print()
print(notas_diccionario.loc['contabilidad'])
