def run():
    #este ciclo recorre la variable contador en un rango de 1000
    for contador in range(1000):
        #si se cumple la condicion que el residuo de su division entre dos es diferente de 0
        #entonces continua y se imprime una lista de numeros pares hasta el 1000
        if contador % 2 != 0:
            continue
        print(contador)
    
    #en este ciclo para un rango de 10 mil, se imprimen los numeros si
    # el numero es igual hasta 6578 al llegar ahi se frena
    for i in range(10000):
        print(i)
        if i == 6578:
            break

    #esta variable recibe una entrada del usuario de texto
    texto = input('Escribe un texto: ')
    #este ciclo de cada letra en el texto, si la letra es igual a 'o' 
    # entonces se frena y se imprime la letra
    for letra in texto:
        if letra == 'o':
            break
        print(letra)
    

if __name__ == '__main__':
    run()