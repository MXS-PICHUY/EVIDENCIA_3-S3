import pandas as pd
import random

SEPARADOR=('*'*20)+'\n'

diccionario_notas={'crescencio':[87,100,None],'domitilia':[80,None,57],\
                   'rutilio':[80,70,57],'panfilo':[20,100,100],'ludoviko':[100,100,100]}

notas_diccionario=pd.DataFrame(diccionario_notas)
print(notas_diccionario)
print(SEPARADOR)

diccionario_notas_aleatorias={\
    'crescencio':[random.randrange(60,101) for x in range(3)],\
    'domitila':[80,100,57], 'rutilio':[80,70,57], 'panfilo':[20,100,100],\
    'ludoviko':[100,100,100]}

notas_diccionario=pd.DataFrame(diccionario_notas_aleatorias)
print(notas_diccionario)
print(SEPARADOR)

notas_diccionario.index=['programacion','base de datos','contabilidad']
print(notas_diccionario)
print(SEPARADOR)