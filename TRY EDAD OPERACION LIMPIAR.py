while True:
    try:
        x=int(input('introduce el numero entero: '))
    except ValueError:
        print('no es un dato valido...intente de nuevo...')
    else:
        print('divide entre 50/',x,'el resultado es: ',50/x)
    finally:
        print('finalizacion de un programa')