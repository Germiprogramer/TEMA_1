

if __name__ == "__main__":
    matriz = [
    #ejercicio1
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
    ]
    
    for i in range(len(matriz)):
        (matriz[i])[len(matriz[i])-1] = sum(matriz[i])-(matriz[i])[len(matriz[i])-1]

    print(matriz)
    