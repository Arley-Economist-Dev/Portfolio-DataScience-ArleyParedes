def run():
    #defino una variable constante que vale 1 millon 
    LIMITE = 1000000
    
    #creo una variable que empieza en 0
    contador = 0
    #creo otra que va a ser igual a 2 elevado a la potencia de la variable contador
    potencia_2 = 2**contador
    #mientras la potencia sea menor a la variable constante
    while potencia_2 < LIMITE:
        # se imprime un string + la variable contador convertida a string 
        # + mas un string y la variable potencia convertida a string
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        #la variable contador va siendo sumada en cada interaccion 
        # que se cumple la condicion añadiendo un numero
        contador = contador + 1
        """la variable potencia tambien va siendo elevada a la cantidad de contador en cada iteracion"""
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()