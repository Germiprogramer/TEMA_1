def cadena():
    try:
        cadena = str(input("Elige una cadena de texto: "))
    except:
        print("Elige una cadena de txt")
    
    if len(cadena)>=3 and len(cadena)<10:
        print(True)
    else:
        print(False)