"""Dependencias"""
import random

#Declarando la funcion de entrada
def run():
    #genero una variable de un array del 1 al 99 de numeros de forma aleatoria
    numero_aleatorio = random.randint(1, 100)
    #para conocer el numero se pide al usuario dar un numero
    numero_usuario = int(input("¡Advina el numero entre el 1 y el 100!: "))
    #usando un ciclo while de compara el numero del usuario y el generado aleatoriamente
    while numero_usuario != numero_aleatorio:
        #si el numero de usuario es menor al numero aleatorio se da una pista,
        #se pide que se ingrese un numero mayor
        if numero_usuario < numero_aleatorio:
            print("Busca un número mas grande")
        #si la condicion no se cumple se le dice que ingrese uno menor
        else:
            print("Busca un numero mas pequeño")
        #el numero de usuario se vuelve a cambiar con esta señal
        numero_usuario = int(input("Elige otro numero: "))
    # de no cumplirse la condicion del loop while entonces se gana el juego
    print("¡GANASTE!")

# Este es el entry point del juego
if __name__ == '__main__':
    run()