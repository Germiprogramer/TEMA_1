def tabla():
    arg_1= int(input("Elige un número del 1 al 9"))
    arg_2= int(input("Elige un número del 1 al 9 por segunda vez"))

    if arg_1 <1 or arg_1>9:
        print("Esto está mal, se deben seguir las indicaciones necesarias")
        if arg_2 <1 or arg_2>9:
            print("Esto está mal, se deben seguir las indicaciones necesarias")
        
    for i in range(arg_1):
        print()
        for j in range(arg_2):
            print("*", end="")

tabla()