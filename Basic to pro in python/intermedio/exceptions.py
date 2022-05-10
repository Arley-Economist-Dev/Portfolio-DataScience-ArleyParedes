# Funcion principal
def run():
    #se usa try and except para corregir un valor que no corresponde
    
    #definimos una funcion para encontrar si la palabra es palindromo
    def palindromo(string):
        return string == string[::-1]
    #prueba
    try:
        #se imprime la funcion palindromo con el valor str de 1
        print(palindromo(1))
    #ocurre una excepcion de tipo error
    except TypeError:
        #se imprime un mensaje de error en consola
        print(f'Solamente se pueden ingresar texto, no numeros')

    #Aqui se utiliza la exception Raise para evitar valores vacios
    #se define la misma funcion palindromo
    def palindromo(string):
        #prueba
        try:
            #si la longitud del string es igual a 0 es decir el argumento esta vacio
            if len(string) == 0:
                #se eleva un value error con un mensaje
                raise ValueError("No se puede ingresar una cadena vacia")
            #sino se regresa el str invertido
            return string == string[::-1]
        #ocurre una excepcion de value error con el apodo de ve
        except ValueError as ve:
            #se imprime ve
            print(ve)
            #se retorna un false
            return False
    
    #prueba        
    try:
        #se imprime la funcion con un caracter vacio
        print(palindromo(""))
    #ocurre una excepcion de error de tipo
    except TypeError:
        #se imprime solamente se puede ingresar str
        print(f'Solamente se pueden ingresar texto, no numeros')

    #Aqui se utiliza finally para detener el archivo o programa al saltar un error
    #prueba
    try:
        #la variable f abre el archivo.txt
        f = open('archivo.txt')
        #hacer cualquier cosa con nuestro archivo
    #finalmente
    finally:
        #cierra la variable con el metodo close
        f.close()
        
#entry point
if __name__ == '__main__':
    run()