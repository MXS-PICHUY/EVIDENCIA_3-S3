import pandas as pd
import random
SEPARADOR =("*"*20)+"\n"

diccionario_notas_aleatorias={\
    'crescencio':[random.randrange(60,101) for x in range(3)],\
    'domitila':[80,100,57], 'rutilio':[80,70,57], 'panfilo':[20,100,100],\
    'ludoviko':[100,100,100]}
notas=pd.DataFrame(diccionario_notas_aleatorias)
notas.index=['programacion','base de datos','contabilidad']

print('todas las asignaturas,todos los estudiantes')
subConjunto=notas.loc['Base de Datos':'Contabilidad']
print(subConjunto)
print(SEPARADOR)

print('subconjunto,solamente las notas de rutilio y ludoviko para dos asignaturas')
subConjunto=notas.loc['programacion':'base de datos',['rutilio','ludoviko']]
print(subConjunto)
print(SEPARADOR)

print('solamente calificaciones aprobatorias')
aprobados=notas[notas>=70]
print(aprobados)
print(SEPARADOR)

print('solamente calificaciones aprobotorias entre 70 y 80')
aprobados=notas[(notas>=70) & (notas<=80)]
print(aprobados)
print(SEPARADOR)

print('solamente calificaciones NO aprobatorias que sean pares')
reprobados_pares=notas[(notas<=70) & (notas%2==0)]
print(reprobados_pares)
print(SEPARADOR)

print("la calicifacion de 'panfilo' en 'programacion'")
notas_panfiloprogramacion=notas.at['programacion','panfilo']
print(notas_panfiloprogramacion)
print(SEPARADOR)

print('modificaremos las notas de panfilo en programacion')
notas.at['programacion','panfilo']=80
notas_panfiloprogramacion=notas.at['programacion','panfilo']
print(notas)