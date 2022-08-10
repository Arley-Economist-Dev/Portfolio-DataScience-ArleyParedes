#creo una funcion principal
def run():
    
    #resolviendo para seleccionar solo numeros primos con list comprehension
    #creo una lista con los numeros siguiente
    my_list = [1,4,5,6,9,13,19,21]
    
    #genero una variable que contiene la siguiente list comprehension
    #esta es la estructura de una list comprehension: valor + ciclo for + condicion (obligatoria)
    odd = [i for i in my_list if i % 2 != 0]
    
    #luego imprime los valores en odd
    print(odd)
    
    """resolviendo utilizando el metodo de filter"""
    my_list = [1,4,5,6,9,13,19,21]
    
    #el metodo filter tiene la siguiente sintaxis
    #filter(lambda + valor + condicion, variable_a_filtrar)
    #list() convierte toda estructura en una lista
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    
    #se imprime la lista odd    
    print(odd)
    

    """haciendo que los valores de una lista retornen su cuadrado"""
    
    #creamos una lista
    my_list = [1,2,3,4,5]
    #la lista es igual al list comprehesion siguiente
    my_list = [i**2 for i in my_list]
    #esta es otra forma de hacerlo con el list comprehension
    my_list = [i**2 for i in range(1,6)]
    #se imprime la lista
    print(my_list)
    
    #resolviendo lo anterior usando map
    my_list = [1,2,3,4,5]
    
    #el metodo map tiene la siguiente sintaxis
    #map(lambda + valor + condicion, variable_a_modificar)
    #list() convierte toda estructura en una lista
    squares = list(map(lambda x: x**2, my_list))
    print(squares)
    
    """sumando los valores de una lista con un ciclo for"""
    
    #creamos una lista con esta caracteristica
    my_list = [2,2,2,2,2]
    #creamos una variable que vale 1
    all_multiplied = 1
    
    #por cada elemento en la lista
    for i in my_list:
        #la variable que vale 1 sera multiplicada por los elementos de la lista
        all_multiplied = all_multiplied * i
    #se imprime los item de la variable all_multiplied        
    print(all_multiplied)
    
    """resolviendo esto con la funcion reduce"""
    
    #dependencia
    from functools import reduce
    
    #creamos una lista igual 
    my_list = [2,2,2,2,2]
    #la variable all_multiplied, tiene el metodo reduce que funciona asi
    # reduce(lambda + valor a, valor b: valor a * valor b, variable_a_reducir)
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    #imprimir todos los resultados del metodo reduce
    print(all_multiplied)
    
#entry point
if __name__ == '__main__':
    run()