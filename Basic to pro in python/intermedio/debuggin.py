from multiprocessing.sharedctypes import Value


def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

#se usan las excepciones try and except para hacer que el programa funcione mejor
def run():
    try:
        num = int(input("Ingresa un numero y devolveré sus divisores: "))
        print(divisor(num))
        print('Termino mi programa')
    except ValueError:
        print('Debes ingresar un número')


if __name__ == '__main__':
    run()