"""
Primero comprendamos que son las nested functions
son funciones que estan jerarquizadas unas sobre otras
"""

def main():
    a = 1
    
    def nested():
        print(a)
    
    nested()

main() #devuelve 1

#que pasa si realizamos un pequeño cambio
def main():
    a = 1
    
    def nested():
        print(a)
    
    return nested

my_func = main()
my_func()   #devuelve 1

"""
Un closure se da cuando una variable que esta en un estado superior es recordada por un scope inferior 
veamos otro ejemplo
"""

def main():
    #se declara la variable a con valor 1
    a = 1
    #se define una funcion nested con parametro vacio
    def nested():
        #se imprime a
        print(a)
        #se define una funcion nested sin parametro
        def nested():
            #se imprime a
            print(a)
        #al final de la funcion nested se regresa el valor nested osea 1
        return nested

#la funcion es igual a main    
my_func = main()
#se imprime la funcion
my_func()

#el keyword del sirve para eliminar funciones o variables
del(main)

#luesgo se ejecuta la funcion y deberia de borrarse lo del main pero...
#la funcion nested sigue recordando una variable de un scope (alcance) superior
my_func() #esto regresa 1
          #             1

"""Reglas para encontrar un Closure
1- Debemos tener una nested function
2- La nested function debe referenciar un valor de un scope superior
3- la funcion que envuelve la nested function debe retornarla tambien
"""

def make_multiplier(x):
    
    def multiplier(n):      # Esta es la nested function
        return x * n        # aqui se utiliza la x referencia de un scope superior
    
    return multiplier       # la funcion envolvente devuelve el valor tambien

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))