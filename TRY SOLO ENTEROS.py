while True:
    try:
        edad=int(input('escribe tu edad:  '))
        break
    except ValueError:
        print('debes de ingresar un numero')    
if edad>=18:
    print('eres un adulto')
else:
    print('aun no eres un adulto')