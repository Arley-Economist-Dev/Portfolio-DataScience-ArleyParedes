#creando iterador
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

#iterando un iterador

print(next(my_iter))

#cuando no quedan datos la excepcion StopIteration es elevada

#creando un itereador que recorra una lista larga
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

#iterando un iterador
while True: #asignar la condicion True convierte a este ciclo en un bucle infinito
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
    
#un iterador en sugar sintaxis es un ciclo for

for element in my_list:
    print(element)


#Construccion de un iterador con clases

class EvenNumbers:
    """
    clase que implementa un iterador de todos los numeros pares o los numeros
    pares o los numeros pares hasta un máximo."""
    
    def __init__(self, max=None): #se crea un constructor
        self.max = max

    def __iter__(self):     #se genera un iterador
        self.num = 0
        return self
    
    def __next__(self):     #se crea una funcion next para iterar
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration

