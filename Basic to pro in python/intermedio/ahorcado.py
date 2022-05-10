#dependencias
from random import randint
from os import system

#funcion leer
def read():
    #aqui se abre un archivo de data en txt
    # with open(ruta del archivo, "solo lectura", encoding= 'utf-8') as apodo
    with open("./archivos/data.txt", "r", encoding='utf-8') as f:
        #las variable palabra contiene la lista
        #de cada elemento replazado con un \n y un espacio vacio para cada elemento en el archivo
        #esto es list comprehension
        words = [i.replace('\n','') for i in f]
    #regresa la variable
    return(words)

#funcion comparacion recibe los parametros word y lineas
def comparison(word, lineas):
    # estas variables almacenan en listas los parametros
    w=list(word)
    l=list(lineas)
    #el usuario contiene un str vacio
    usuario = ''
    
    #mientra w sea diferente a la palabra l o el usuario sea igual a dedo
    while w != l or usuario == 'dedo':
        #el usuario podra ingresar una letra
        usuario = input('ingrese una letra: ')
        #se prueba con un assert si la distancia es mayor a 1, se arroja el mensaje de error
        assert len(usuario) == 1, '!!!Presionaste mas de una letra¡¡¡'
        #system limpia el terminal
        system('clear')
        #para cada elemento en el rango de cero a la distancia de w
        for i in range(0, len(w)):
            #si el valor de w es igual al usuario
            if w[i] == usuario:
                #entonces se comparan los valores de l y w
                l[i] == w[i]
        #se imprime un espacio vacio donde une a los elementos de l con letras mayusculas
        print(' '.join(l).upper())
        #se imprime \n
        print('\n')
    
    #Se imprime un mensaje de victoria
    print('!Ganaste la palabra era¡ ' + word.upper())

#se define la funcion run
def run():
    #las palabras seran el resultado de read
    words = read()
    #el index sera un valor aleatorio entre 0 y la distancia de la palabra
    index = randint(0, len(words))
    #word sera igual a words en cada elemento
    word = words[index]
    #las lineas seran igual a un guion con la longitud de la palabra
    lines = '-'*len(word)
    
    #se imprime el mensaje
    print('!Adivina la palabra¡')
    #se imprime el vacio con la union de las lineas
    print(' '.join(lines))
    #se imprime el resultado de \n
    print('\n')
    
    #se comparan con la funcion la palabra y las lineas    
    comparison(word, lines)

#entry point
if __name__ == '__main__':
    run()