def divisor(num):
    divisor = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

#aca vamos a usar assert + condicion + mensaje
def run():
    num = input("Ingresa un numero y devolveré sus divisores: ")
    assert num.isnumeric(), "Ingresa un numero: "
    print(divisor(int(num)))
    print('Termino mi programa')
    
#con esta parte del codigo podes generar una restriccion sobre los numeros y que sean positivos
def run():
    num = input("Ingresa un numero y devolveré sus divisores: ")
    assert num.isnumeric() & int(num)>0, "Ingresa un numero positivo"
    print(divisor(int(num)))
    print('Termino mi programa')


if __name__ == '__main__':
    run()