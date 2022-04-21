def run():
    #se usa try and except para corregir un valor que no corresponde
    def palindromo(string):
        return string == string[::-1]

    try:
        print(palindromo(1))
    except TypeError:
        print(f'Solamente se pueden ingresar texto, no numeros')

    #Aqui se utiliza la exception Raise para evitar valores vacios
    def palindromo(string):
        try:
            if len(string) == 0:
                raise ValueError("No se puede ingresar una cadena vacia")
            return string == string[::-1]
        except ValueError as ve:
            print(ve)
            return False
        
    try:
        print(palindromo(""))
    except TypeError:
        print(f'Solamente se pueden ingresar texto, no numeros')

    #Aqui se utiliza finally para detener el archivo o programa al saltar un error
    try:
        f = open('archivo.txt')
        #hacer cualquier cosa con nuestro archivo
    finally:
        f.close()
        

if __name__ == '__main__':
    run()