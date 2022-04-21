"""El scope es el alcance que tienen las variables para su uso dentro o fuera
de una funcion, existe alcancen locales y globales, a continuación unos ejemplos"""

# Local Scope

def my_func():
    y = 5
    print(y)
    #la variable solo puede ser utilizada en este ambito local

my_func()

# global scope

#esta variable se declara globalmente y 
# la podemos utilizar dentro de todas las funciones 

y = 5

def my_func():
    print(y)

def my_other_func():
    print(y)
    
my_func()
my_other_func()