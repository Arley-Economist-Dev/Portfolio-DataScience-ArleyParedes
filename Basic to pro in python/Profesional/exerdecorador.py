from unittest import result

"""
el siguiente decorador define las siguientes cosas:
1- imprime el nombre de la funcion y los valores de su argumento
2- corre la funcion con los argumentos
3- imprime el resultado
4- regresa la funcion modificada para usarse
"""
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
    return new_function

@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)