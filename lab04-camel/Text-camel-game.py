import random
import arcade
class jugadores:
    def __init__(self, millas, sed, cansancio, botella):
        self.millas = millas
        self.sed = sed
        self.cansancio = cansancio
        self.botella = botella

jugador = jugadores(0, 0, 0, 3)
cobalto = jugadores(-50, 0, 0, 6)

#def enemigos():
#    if cobalto.botella <= 0:
#        cobalto.botella = 0
    
#    else: 
#        cobalto.millas += random.randint(7, 14)
#        cobalto.botella -= 1


def main ():
    done = False
    print("Bienvenido a Escorpión")
    print("Has robado la montura más preciada del emperador, el escorpión ojos claros")
    print("Te persigue la guardia de cobalto personal a través del desierto")
    print("Sobrevive, escapa y continua tu vida como ladrón")

    while not done:
        print("A. Beber de tu botella")
        print("E. Hacia delante a velocidad moderada")
        print("I. Adelante full velocidad")
        print("O. Descansar por la noche")
        print("U. Pasar")
        print("Q. Salir")

        opcion = input("Elija: ")

        if opcion == "q":
            done = True

        elif opcion == "a":
            if jugador.botella <= 0:
                print("Intentas beber pero te desesperas en el intento, pierdes un día")
                cobalto.millas += random.randint(7, 14)
            else:
                print("Te sientes revitalizado")
                jugador.botella -= 1
                jugador.sed = 0
                cobalto.millas += random.randint(7, 14)

        elif opcion == "e":
            desplazamiento = random.randint(5, 12)
            jugador.millas += desplazamiento
            print("Te mueves ", desplazamiento, " millas, llevas en total unas ", jugador.millas, " millas recorridas")
            cobalto.millas += random.randint(7, 14)
            jugador.sed += 1
            jugador.cansancio += 1

        elif opcion == "i":
            desplazamiento = random.randint(10, 20)
            jugador.millas += desplazamiento
            print("Te mueves ", desplazamiento, " millas, llevas en total unas ", jugador.millas,
                  " millas recorridas")
            cobalto.millas += random.randint(7, 14)
            jugador.sed += random.randint(1, 2)
            jugador.cansancio += random.randint(1, 3)

        elif opcion == "o":
            jugador.cansancio = 0
            print("Descansais alegremente, os sentiís mucho mejor")
            cobalto.millas += random.randint(7, 14)

        if jugador.sed >= 3 and jugador.sed < 5:
            print("Tenéis bastante sed")

        elif jugador.sed >= 5:
            print("No podés aguantar más, moriís en medio del desierto")
            done = True
            break

        if jugador.cansancio >= 5 and jugador.cansancio < 8:
            print("Tu grupo empieza a estar cansado")

        elif jugador.cansancio >=8:
            print("No podeis más, con peso en vuestros cuerpos os desmallais, moriís por falta de sueño")
            done = True
            break

        if cobalto.millas >= jugador.millas:
            print("Os han pillado, no podeis hacer nada, os ejecutan a golpe de lanza")
            done = True
            break

        elif jugador.millas - cobalto.millas <= 15:
            print("Unas siluetas armadas aparecen en el horizonte")

        if jugador.millas >= 200:
            print("Lo conseguisteis, habéis ganado")
            done = True

main()
