#dependencia
from multiprocessing.sharedctypes import Value

#se define la funcion divisor que recibe el parametro num
def divisor(num):
    #el divisor es una lista vacia
    divisor = []
    #para cada elemento en el rango de 1 hasta el numero mas uno
    for i in range(1, num + 1):
        #si el residuo del numero entre el elemento del rango es igual a 0
        if num % i == 0:
            #entonces es divisor y se llena en la lista
            divisor.append(i)
    #la funcion retorna la variable divisor
    return divisor

#se usan las excepciones try and except para hacer que el programa funcione mejor
def run():
    #prueba
    try:
        #si el numero recibido es convertido a entero
        num = int(input("Ingresa un numero y devolveré sus divisores: "))
        #se imprime el resultado de la funcion definida arriba
        print(divisor(num))
        print('Termino mi programa')
    #si no sale un error
    except ValueError:
        print('Debes ingresar un número')

#entry point
if __name__ == '__main__':
    run()