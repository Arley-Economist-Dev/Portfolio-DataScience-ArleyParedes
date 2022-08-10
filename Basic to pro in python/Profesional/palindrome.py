#Esta funcion lo que hace es recibir un string convertirlo a booleano
def is_palindrome(string: str) -> bool:
    #esta linea crea una variable que se convierte en minuscula y que reemplaza los espacios por caracteres vacios
    string = string.replace(" ","").lower()
    #regres un string que es comparado con el mismo string pero usando slices para revertirlo
    return string == string[::-1]

#aqui se corre la funcion imprimiento el resultado de la funcion pero en este caso hay un error
def run():
    #el valor que la funcion espera es un string pero es un entero
    print(is_palindrome(1000))

    #El comando usado para ver el error de tipado es: mypy palindrome.py --check-untyped-defs

if __name__ == '__main__':
    run()