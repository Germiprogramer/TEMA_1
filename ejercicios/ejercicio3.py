lista = []

def ejercicio3(inicio,salto,limite):   
    
    
    if inicio < limite:
        lista.append(inicio+salto)
        inicio = inicio + salto
        ejercicio3(inicio,salto,limite)
    else:
        print(lista)

ejercicio3(1,2,10)
    