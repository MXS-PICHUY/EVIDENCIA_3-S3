def solicitar_edad():
    try:
        return int(input('escribe tu edad: '))
    except ValueError:
        return solicitar_edad()
    
edad= solicitar_edad()