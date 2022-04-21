"""Este programa lo que hace es poner a prueba la conjetura de collatz"""

# se toma un integer positivo n
# se divide por 2
# si el numero que regresa es par se vuelve a dividir por 2
# si el numeor que regresa es impar se aplica 3*n + 1
# esto se hace en un ciclo

import time 

class CollatzIter():
    
    def __iter__(self):
        self.n = int(input("Ingresa un numero positivo: "))
        return self
    
    def __next__(self):
        num_seq = [self.n]
        if self.n < 1:
            print("el numero debe ser positivo")
        while self.n > 1:
            if self.n % 2 == 0:
                self.n = self.n / 2
            else:
                self.n = 3 * self.n  + 1
        return self.n

if __name__ == '__main__':
    collatz = CollatzIter()
    for element in collatz:
        print(element)
        time.sleep(0.5)    


# def collatz_sequense(x):
#     num_seq = [x]
#     if x < 1:
#         return[]
#     while x > 1:
#         if x % 2 == 0:
#             x = x / 2
#         else:
#             x = 3 * x + 1
            
#         num_seq.append(x)
#     return num_seq

# print(collatz_sequense(12))

# print(collatz_sequense(19))

   