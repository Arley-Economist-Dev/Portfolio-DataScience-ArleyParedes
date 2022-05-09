def run():
    #ESTA FUNCION CREA UN DICCIONARIO DE 3 ELEMENTOS
    mi_diccionario = {
        'llave1': 1, 
        'llave2': 2,
        'llave3': 3,
    }
    
    #CON ESTO SE IMPRIMEN LA LLAVE QUE ES EL ID DE EL DICCIONARIO
    print (mi_diccionario['llave1'])
    print (mi_diccionario['llave2'])
    print (mi_diccionario['llave3'])

    #SE CREA UN DICCIONARIO CON LA POBLACION INVENTADA DE 3 PAISES DEL MUNDO
    poblacion_paises = {
        'Argentina': 44038912,
        'Brasil': 298217287172,
        'Colombia': 2182716271,
    }
    
    #SE IMPRIME LA POBLACION DE ARGENTINA UN ELEMENTO DEL DICT
    print(poblacion_paises['Argentina'])
    
    # Este es un ciclo que para cada pais de la variable de poblacion
    for pais in poblacion_paises.keys():
        #imprime el elemento
        print(pais)
    
    # para cada pais en la poblacion de de su valores
    for pais in poblacion_paises.values():
        #imprima la cantidad del pais
        print(pais)
    
    #se usa un ciclo for para cada elemento y su id de los elementos del dict
    for pais, poblacion in poblacion_paises.items():
        #se imprime el pais, un str , un str con la poblacion y el string habitantes
        print(pais + ' tiene ' + str(poblacion) + ' Habitantes')

if __name__ == '__main__':
    run()