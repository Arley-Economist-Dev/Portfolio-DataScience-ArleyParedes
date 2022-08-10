"""Un decorador es una funcion que recibe como parametro
otra funcion, le añade cosas y retorna un funcion diferente"""

def decorador(func):
    def envoltura():
        print('esto se añade a mi funcion original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')

saludo()
#Output: ¡Hola!

saludo = decorador(saludo)
saludo()
#output, esto se añade a mi funcion original
#¡Hola!

#mas ejemplos
def decorador(func):
    def envoltura():
        print('esto se añade a mi funcion original')
        func()
    return envoltura

def saludo():
    print('¡Hola!')
saludo = decorador(saludo)

saludo()

#Ahora el ejemplo de arriba con azucar sintaxica "Sintaxic sugar"

def decorador(func):
    def envoltura():
        print('esto se añade a mi funcion original')
        func()
    return envoltura

@decorador
def saludo():
    print('¡Hola!')

saludo()

#Ejemplo practico

def mayusculas(func):   #la funcion contiene como parametro otra funcion
    def envoltura(texto):      #contiene un nested function
        return func(texto).upper() #hace referencia a un scope superior
    return envoltura    #regresa la nested function

@mayusculas     #
def mensaje(nombre):
    return f'{nombre}, recibiste un mensaje'

print(mensaje('Cesar'))