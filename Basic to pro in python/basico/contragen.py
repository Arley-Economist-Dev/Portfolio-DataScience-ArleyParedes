#Dependencias
import random

#Se genera una funcion vacia que genera una contraseña
def generar_contrasena():
    """
    DENTRO DE ESTA PARTE DE LA FUNCION ESTAN LAS LISTAS DE MAYUSCULAS
    DE LAS MINUSCULAS, LOS NUMEROS DEL 0 AL 9 
    Y UN CONJUNTO DE CARACTERES ESPECIALES
    """
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    """
    SE CREA UNA VARIABLE LLAMADA CARACTERES QUE SUMA LAS LISTAS ANTERIORES UNIENDOLAS
    """
    caracteres = MAYUS + MINUS + NUMS + CHARS
    
    #SE GENERA UNA VARIABLE LLAMADA CONTRASEÑA QUE ES UNA LISTA VACIA
    contrasena = []
    
    #CON ESTE CICLO CADA ELEMENTO EN UN RANGO DE 15 ITERACIONES
    for i in range(15):
        #GENERA UNA VARIABLE QUE COJE UN CARACTER RANDOM DE LA VARIABLE CARACTERES QUE CONTIENE LOS CONJUNTOS SUMADOS
        caracter_random = random.choice(caracteres)
        #SE AÑADE A LA LISTA VACIA EN CONTRASEÑA CON EL APPEND UN CARACTER RANDOM ANTERIORMENTE DEFINIDO
        contrasena.append(caracter_random)
    
    #LA VARIABLE CONTRASEÑA BORRANDO LOS CARACTERES VACIOS PARA UNIRLA EN LA VARIABLE CONTRASEÑA
    contrasena = ''.join(contrasena)
    # LA FUNCION REGRESA LA VARIABLE CONTRASEÑA
    return contrasena

# SE CREA UNA FUNCION QUE VA A CORRER LA ANTERIOR
def run():
    # LA VARIABLE CONTRASEÑA VA A SER INGUAL A LA FUNCION DEFINIDA ARRIBA
    contrasena = generar_contrasena()
    #SE VA A IMPRIMIR EL RESULTADO DE CONTRASEÑA JUNTO A UN STRING
    print('Tu nueva contraseña es: ' +  contrasena)


if __name__ == '__main__':
    run()