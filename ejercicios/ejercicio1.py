def matrix(matriz,i):
    i=i+1
    (matriz[i])[len(matriz[i])-1] = sum(matriz[i])-(matriz[i])[len(matriz[i])-1]
    try:
        matrix()
    except:
        print(matriz)
    return matriz