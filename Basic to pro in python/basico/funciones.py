#Creamos una funcion que imprimer 4 cadenas caracteres
def mensaje_inicial():
  print("Hola")
  print("Bienvenido a este convertidor de monedas")
  print("Tienes que seleccionar")
  print("Adios")

#aqui se ejecuta la funcion que declaramos anteriormente
mensaje_inicial()

#se define una funcion que se llama conversacion que tiene un paratro llamado opcion
def conversacion(opcion):
    """COn un mensaje se le dice al usuario la opcion que escogio"""
    print('Hola')
    print('Como estas')
    print('Elegiste la opcion: ' + str(opcion))
    print('Adios')

#se crea una variable llamada opcion que es el parametro que va a llevar la funcion
opcion = int(input('Ingrese una opcion (1, 2, 3): '))

#si la opcion es igual a 1 
if opcion == 1:
    #la opcion que se mostrara es la 1
    conversacion(opcion)
elif opcion == 2:
    #la opcion que se mostrara es la 2
    conversacion(opcion)
elif opcion == 3:
    #la opcion que se mostrara es la 3
    conversacion(opcion)
else:
    #sino se le pedira un valor valido
    print("Inserta un valor valido")











