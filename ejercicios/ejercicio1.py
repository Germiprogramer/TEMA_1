def matrix(matriz,i):
    i=i+1
    (matriz[i])[len(matriz[i])-1] = sum(matriz[i])-(matriz[i])[len(matriz[i])-1]
    try:
        matrix()
    except:
        print(matriz)
    return matriz

if __name__ == "__main__":
    
    matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
    ]

    matrix(matriz,0)