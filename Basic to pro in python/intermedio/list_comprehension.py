#funcion principal
def run():
    #Esto es una forma de hacerlo sin list comprehension
    #genero una variable con lista vacia
    squares = []
    #por cada elemento en un rango de 1 a 100
    for i in range(1, 101):
        #se añaden a la lista vacia el elemento elevado al cuadrado
        squares.append(i**2)
    
    #se imprimen los numeros al cuadrado
    print(squares)

    #generas una variable 2 con otra lista vacia
    squares2 = []
    # por cada elemento del 1 al 100
    for i in range(1, 101):
        #si el residuo de cada valor entre 3 es diferente de 0
        if i % 3 != 0:
            #entonces añade solo a la lista los valores que cumplen la condicion
            squares2.append(i**2)
            
    #esta es la estructura de una list comprehension: valor + ciclo for + condicion (obligatoria)
    #para esta list comprehension tiene la siguiente estructura
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    #se imprime los numeros de la lista
    print(squares)
    
    #con esta siguiente lis comprehension se obtienen solo los numeros que son multiplos de:
    # cuatro, seis y nueve
    multiplos = [i for i in range(1,10000) if i%4==0 and i%6==0 and i%9==0]        
    #se imprime los numeros multiplos
    print(multiplos)
    
#entry point
if __name__ == '__main__':
    run()