#Este codigo sirve de ejemplo para considerar los casos en los que python
#encuentra erroes de tipado de variables
#Se trata de un programa que pide numeros de telefono y los regresa en pantalla
def run():
    FALLBACK_PHONE = '+e80080088'
    
    def get_phone():
        phone = input('give me your phone: ')
        if not phone:
            return FALLBACK_PHONE.round()
        return int(phone)
    
    def run():
        my_phone = get_phone()
        print(f'Your phone is: {my_phone}')

if __name__ == '__main__':
    run()

#Sintaxis para conocer python de forma estatica

a: int = 5
print(a)    #5 

b: str = 'Hola'
print(b)    #Hola

c: bool = True
print(c)    #True

#sintaxis estatica para el caso de las funciones
def suma(a: int, b: int) -> int:
    return a + b

print(suma(1,2)) #3
print(suma('1','2')) #retornara 12  porque estas sumando strings

#Ahora el tipado estatico con estructuras de datos
from typing import Dict, List

positives: List[int] = [1,2,3,4,5]

users: Dict[str, int] = {
    'Argentina': 1,
    'Mexico': 34,
    'Colombia': 45
}

#para los diccionarios
countries: List[Dict[str, str]] = [
    {
        'name': 'Argentina',
        'people':'450800',
    },
    {
        'name': 'México',
        'people':'900800',
    },
    {
        'name': 'Colombia',
        'people':'99999999999999',
    }
]

#para la clase tupla
from typing import Tuple

numbers: Tuple[int, float, int] = (1, 0.5, 1)

#casos combinados
from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {
        'coord1': (1, 2)
        'coord2': (3, 5)
    },
    {
        'coord1': (0, 1)
        'coord2': (2, 5)
    },
]