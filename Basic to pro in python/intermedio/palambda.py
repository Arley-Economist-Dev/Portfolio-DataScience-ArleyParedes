#Definimos primero una funcion princial
def run():
    #A continuacion se usa una funcion lambda que es substita de la funcion def
    #la estructura es: lambda + argumentos que recibe la funcion + expresion o condicion
    # en este caso se genera un string que se compara consigo mismo al derecho y al reves
    palindrome = lambda string: string == string[::-1]
    
    #se imprime el resultado de la funcion palindromo
    print(palindrome('ana'))
    #regresa un valor True o False

#entry point
if __name__ == '__main__':
    run()