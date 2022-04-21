def run():
    #esto sirve para conocer las listas y diccionarios
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Arley", "lastname": "Paredes"}
    
    super_list = [
        {"firstname": "Arley", "lastname": "Paredes"},
        {"firstname": "Dario", "lastname": "Torres"},
        {"firstname": "Merchel", "lastname": "Zapata"},
        {"firstname": "Ervin", "lastname": "Cardenas"}
    ]
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

    for i in super_list:
	    print(i.items())


if __name__ == '__main__':
    run()