def run():
    #SE CREA UNA VARIABLE QUE CONTIENE EL NOMBRE Y LO RECIBE DEL USUARIO
    nombre = input("Escribe tu nombre: ")
    # ESTE CICLO FOR PARA CADA LETRA EN EL NOMBRE IMPRIME CADA LETRA
    for letra in nombre:
        print(letra)

    # SE RECIBE LA ENTRADA DE UN TEXTO EN LA VARIABLE FRASE
    frase = input("Escribe una frase: ")
    # PARA CADA CARACTER EN LA FRASE SE IMPRIME LA LETRA EN MAYUSCULA
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()