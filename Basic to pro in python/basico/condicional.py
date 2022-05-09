# defino una variable edad que es recibida desde el usuario
# la variable es la edad del usuario
edad = int(input("Escribe tu edad: "))
#si la edad es mayor que dieciseis
if edad > 17:
    # se imprime que el es mayor de edad
    print(f'eres mayor de edad')
#si no se cumple la condicion entonces el es menor de edad
else:
    print(f'eres menor de edad')

#declaro una variable numero que recibe un numero    
numero = int(input('Escribe un numero: '))

# si el numero es menor a 5
if numero > 5:
    #se imprime es mayor a 5
    print(f'Es mayor a 5')
# si tambien el numero es igual a 5 
elif numero == 5:
    # se imprime es igual a 5
    print(f'Es igual a 5')
# y si no a las dos anteriores se imprime es menor a 5
else:
    print(f'Es menor a 5')

