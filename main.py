from ejercicios.ejercicio1 import *
from ejercicios.ejercicio2 import *
from ejercicios.ejercicio3 import *
from ejercicios.tabla import *

def main():
    if __name__ == "__main__":
        ejercicio = int(input("Introduzca el número del ejercicio:   "))

        if ejercicio ==1:
            matriz = [
            [1, 1, 1, 3],
            [2, 2, 2, 7],
            [3, 3, 3, 9],
            [4, 4, 4, 13]
            ]

            matrix(matriz,0)
        if ejercicio ==2:
            cadena()

        if ejercicio ==3:
            lista=[]
            ejercicio3(0,1,11)
            ejercicio3(-10, 1, 1)
            ejercicio3(0, 21, 2)
            ejercicio3(-19, 0, 2)
            ejercicio3(0, 51, 5)

        if ejercicio ==4:
            tabla()

main()