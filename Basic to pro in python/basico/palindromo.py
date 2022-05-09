# se crea una funcion llamada palindro que recibe una palabra
def palindromo(palabra):
    #todos los espacios entre la palabra son removido
    palabra = palabra.replace(" ", "")
    #la palabra se convierte a minuscula
    palabra = palabra.lower()
    #se crea una variable que contiene la palabra recibida al reves
    palabra_invertida = palabra[::-1]
    # si la palabra es igual a la palabra repedita entonces es true sino false
    if palabra == palabra_invertida:
        return True
    else:
        return False

# se crea una variable que recibe un input de palabra
# la palabra es palindro es igual a la funcion declarada arriba
# si la funcion retorna true entonces se imprime si es palindromo
# si es false se imprime que no es palindromo
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()

