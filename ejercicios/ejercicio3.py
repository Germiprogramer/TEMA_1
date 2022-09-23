lista = []
def ejercicio3(inicio,salto,limite):   
    try:
        if inicio not in lista:
            lista.append(inicio)
    except:
        pass
    
    
    if inicio < limite:
        lista.append(inicio+salto)
        inicio = inicio + salto
        ejercicio3(inicio,salto,limite)
    else:
        print(lista)

    