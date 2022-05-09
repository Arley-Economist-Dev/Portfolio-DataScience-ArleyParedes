"""
DEFINIMOS UNA FUNCION QUE RECIBE UN PARAMETRO NUMERICO

CREAMOS UN CONTADOR QUE EMPIEZA EN 0

CREAMOS UN CICLO PARA CADA ELEMENTO EN EL RANGO DE 1 Y EL NUMERO + UNO

SI ELEMENTO ES IGUAL A 1 O EL ELEMENTO ES IGUAL AL NUMERO EL CICLO CONTINUA

SI EL RESIDUO DEL NUMERO ENTRE LOS VALORES DEL NUMERO SON IGUALES A 0 EL CONTADOR INCREMENTA UNA UNIDAD

SI EL CONTADOR ES IGUAL A 0 REGRESA TRUE SINO REGRESA FALSE
"""
def es_primo(numero):
    contador = 0
    
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


"""
lA FUNCION QUE CORRE EL PROGRAMA RECIBE EL NUMERO PIDIENDOLO AL USUARIO
SI LA VARIABLE ES NUMERO ES IGUAL A LA CONDICION DE LA FUNCION TRUE
ENTONCES IMPRIME ES PRIMO 
SI NO ES FALSE Y SE IMPRIME NO ES PRIMO
"""
def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero) == True:
        print(f'Es primo')
    else:
        print(f'No es primo')



if __name__ == '__main__':
    run()