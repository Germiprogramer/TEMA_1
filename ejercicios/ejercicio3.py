lista = []
def ejercicio3(inicio,salto,limite):   
    if inicio not in lista:
        lista.append(inicio)
    
    if inicio < limite:
        lista.append(inicio+salto)
        inicio = inicio + salto
        ejercicio3(inicio,salto,limite)
    else:
        print(lista)

    