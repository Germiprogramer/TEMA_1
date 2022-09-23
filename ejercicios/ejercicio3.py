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

if __name__ == "__main__":
    lista=[]
    ejercicio3(0,1,11)
    ejercicio3(-10, 1, 1)
    ejercicio3(0, 21, 2)
    ejercicio3(-19, 0, 2)
    ejercicio3(0, 51, 5)