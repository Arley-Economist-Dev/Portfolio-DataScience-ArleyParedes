def es_primo(numero: int) -> bool:
    #La solucion de este la realize con recursividad
    for n in range(2, numero):
        if numero % n == 0:
            print("no es primo", n, "es divisor")
            return False
    print("Es primo")
    return False    


def run():
    es_primo(7)
    

if __name__ == '__main__':
    run()