# si al programa le ingreso (hola,3) -> holaholahola

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi"))

"""EJERCICIO DE CLOSURES AHORA PARA EL CASO DE LA DIVISION"""

def make_division_by(n):
    """este closure regresa una funcion que retorna una
    division de un numero x por un numero y"""
    def divisor(x):
        return x / n
    return divisor

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) #Se espera 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) #se espera 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) #se espera 3

if __name__ == '__main__':
    run()