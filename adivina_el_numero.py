lista = """"
Bienvenido al juego de adivinar el número, escoja un nivel de dificultad:

1) Simple (0,100)
2) Intermedio (0,1.000)
3) Avanzado (0,1.000.000)
4) Experto (0,1.000.000.000.000)
"""""
def juego():

    print (lista)

    opcion = input("Eliga una de las cuatro opciones: ")
    print(opcion)


    if opcion == "1":
        adivina(0,100, numero = numerorandom(0,100))

    elif opcion == "2":
        adivina(0,1000, numero = numerorandom(0,1000))

    elif opcion == "3":
        adivina(0,1000000, numero = numerorandom(0,1000000))
    elif opcion == "4":
        adivina(0,1000000000000, numero = numerorandom(0,1000000000000))
    else:
        return juego()

def numerorandom(minimo,maximo):
    import random
    numero = random.randint(minimo,maximo)
    return numero

def adivina(minimo,maximo,numero):
    pista = 0
    intento = input("Introduzca el númeoro entre " + str(minimo) + " y " + str(maximo) + " : ")
    intento = int(intento)
    print(intento)
    while True:
        if intento < numero:
            print("Es demasiado pequeño.")
            pista+=1
            if pista == 6:
                ayuda(minimo,maximo,numero)
        elif intento > numero:
            print("Es demasiado grande.")
            pista+=1
            if pista == 6:
                ayuda(minimo,maximo,numero)
        elif intento == numero:
            print("Felicidades, has acertado.")
        else:
            return adivina(minimo,maximo,numero)

def ayuda(minimo,maximo,numero):
    resolucion = input("¿Quieres una pista? ")
    print(resolucion)
    if resolucion == "si":
        print("Está entre", minimo, " y ",maximo)
        adivina(minimo,maximo,numero)
    elif resolucion == "no":
        print("Sin pista")
        return adivina()
    else:
        return ayuda()



juego()
