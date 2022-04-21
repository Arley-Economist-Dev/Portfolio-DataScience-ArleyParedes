import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input("¡Advina el numero entre el 1 y el 100!: "))
    while numero_usuario != numero_aleatorio:
        if numero_usuario < numero_aleatorio:
            print("Busca un número mas grande")
        else:
            print("Busca un numero mas pequeño")
        numero_usuario = int(input("Elige otro numero: "))
    print("¡GANASTE!")





if __name__ == '__main__':
    run()