#funcion divisor recibe un numero como parametro
def divisor(num):
    #creo una variable que almacena los divisores en una lista vacia
    divisor = []
    #por cada elemento en un rango de 1 mas el numero mas uno
    for i in range(1, num + 1):
        #si el residuo del numero entre los elementos del rango es igual a 0
        #entonces es divisor y se añade a la lista
        if num % i == 0:
            divisor.append(i)
    #regresa la variable divisor
    return divisor

#aca vamos a usar assert + condicion + mensaje
def run():
    #el numero se recibe desde el usuario
    num = input("Ingresa un numero y devolveré sus divisores: ")
    #assert prueba si el numero no es un str, si no se cumple la condicion se lanza un mensaje
    assert num.isnumeric(), "Ingresa un numero: "
    #se imprime el resultado de la funcion divisor
    print(divisor(int(num)))
    #se imprime el mensaje de programa terminado
    print('Termino mi programa')
    
#con esta parte del codigo podes generar una restriccion sobre los numeros y que sean positivos
def run():
    #se genera una variable llamada divisor que recibe el numero del usuario
    num = input("Ingresa un numero y devolveré sus divisores: ")
    #se prueba si el valor es numero ademas de si el valor es mayor que 0
    #si no se cumple la condicion se lanza un mensaje
    assert num.isnumeric() & int(num)>0, "Ingresa un numero positivo"
    #se imprime el resultado de la funcion divisor convertido a int
    print(divisor(int(num)))
    #se imprime se acabo el programa
    print('Termino mi programa')

#entry point
if __name__ == '__main__':
    run()