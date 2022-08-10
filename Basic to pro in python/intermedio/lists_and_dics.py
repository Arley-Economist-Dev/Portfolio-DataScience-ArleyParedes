#funcion principal
def run():
    #Definimos una lista
    my_list = [1, "hello", True, 4.5]
    #definimos un dict
    my_dict = {"firstname": "Arley", "lastname": "Paredes"}
    
    #creamos una lista que contiene diccionarios
    super_list = [
        {"firstname": "Arley", "lastname": "Paredes"},
        {"firstname": "Dario", "lastname": "Torres"},
        {"firstname": "Merchel", "lastname": "Zapata"},
        {"firstname": "Ervin", "lastname": "Cardenas"}
    ]
    
    #creamos un diccionario que contiene listas como elementos
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    # para cada kay y valor en el super dict de cada item
    for key, value in super_dict.items():
        #imprime el key + - + el valor
        print(key, "-", value)
    
    #por cada valor en la super lista
    for values in super_list:
        #por cada llave y valor in los valores por cada item
        for key, value in values.items():
            #imprime la llave - el valor
            print(f'{key} - {value}')

    #por cada elemente en la super lista
    for i in super_list:
        #imprime el elemento por cada item
	    print(i.items())

#entry point
if __name__ == '__main__':
    run()