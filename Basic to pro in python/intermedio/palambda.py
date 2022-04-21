def run():
    #Aqui utilizamos una funcion lamba para resolver el problema del palindromo
    #la estructura es: lambda + argumentos asignados a la funcion + expresion o condicion
    palindrome = lambda string: string == string[::-1]
    
    print(palindrome('ana'))
    #regresa un valor True o False


if __name__ == '__main__':
    run()