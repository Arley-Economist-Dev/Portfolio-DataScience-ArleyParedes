def run():
    mi_diccionario = {
        'llave1': 1, 
        'llave2': 2,
        'llave3': 3,
    }
    
    # print (mi_diccionario['llave1'])
    # print (mi_diccionario['llave2'])
    # print (mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44038912,
        'Brasil': 298217287172,
        'Colombia': 2182716271,
    }
    
    # print(poblacion_paises['Argentina'])
    
    # for pais in poblacion_paises.keys():
    #     print(pais)
        
    # for pais in poblacion_paises.values():
    #     print(pais)
    
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' Habitantes')

if __name__ == '__main__':
    run()