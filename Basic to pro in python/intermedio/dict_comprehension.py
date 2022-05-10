#funcion principal
def run():
    """forma de hacerlo sin dict comprehension"""
    
    #creamos un diccionario vacio
    my_dict = {}
    #para cada elemento en un rango de 1 a 100
    for i in range(1,101):
        #cada indice del diccionario tendra el rango
        # y el mismo indice elevado al cubo
        my_dict[i] = i**3
    
    #creamos un diccionario vacio
    my_dict = {}
    #para cada elemento en el mismo rango
    for i in range(1, 101):
        #si el residuo del elemento es diferente de 0,
        #no es multiplo de 3
        if i % 3 != 0:
            # el diccionario recibe el indice del rango
            # y el cubo del indice elevado al cubo
            my_dict[i] = i**3
    
    #la estructura del dict comprehension es: {id: elemento + un ciclo for + condicion (opcional)}
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0 }
    
    my_dict = {i: pow(i, 1/2) for i in range(1,1001)}
    
    #se imprime el dict
    print(my_dict)


if __name__ == '__main__':
    run()