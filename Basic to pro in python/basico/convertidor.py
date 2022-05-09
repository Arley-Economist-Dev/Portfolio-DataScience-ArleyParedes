"""
DEFINO UNA FUNCION QUE RECIBE LOS VALORES DE TIPO DE MONEDA Y EL VALOR DEL DOLAR
SE DEFINE LA VARIABLE MONEDA QUE ES UN FLOAT QUE SE LE PIDE AL USUARIO DEPENDIENDO DEL PARAMETRO TIPO DE MONEDA
SE CREA UNA VARIABLE DOLARES QUE SE DIVIDE ENTRE LA UNIDAD MONETARIA ANTERIOR QUE ES EL CAMBIO
EL TIPO DE CAMBIO SE REDONDEA A 2 DIGITOS
SE CONVIERTE A UN CARACTER
Y SE IMPRIME LA CANTIDAD
"""
def convertidor(tipo_moneda, valor_dolar):
    u_monetaria = float(input("¿Cuantos "+ tipo_moneda + " tienes?: "))
    dolares = u_monetaria / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes " + dolares + " dolares")

#ESTE ES UN MENU LO QUE CONTIENE UNA VARIABLE QUE ES UNA CADENA DE CARACTERES Y ME ACABA DE DAR UNA GRA IDEA

menu = """
Bienvenido al conversor de monedas a dolares 💵💴💶💷

1- Cordobas a dolares
2- Euros a dolares
3- Yuanes a dolares

Elige una opcion: """

# ESTO ES UNA VARIABLE QUE RECIBE LA OPCION QUE EL USUARIO ELIGEN EN EL MENU
opcion = int(input(menu))

# SI LA OPCION ES IGUAL A 1
if  opcion == 1:
    #EL CONVERTIDOR ES LA FUNCION QUE DEFINIMOS DE PRIMERO, 
    # SI ELIGE 1 SERA EN CORDOBAS Y DEVOLVERA EL VALOR EN CORDOBAS
    convertidor("Cordobas", 35.67)
# SI LA OPCION ES 2 ENTONCES SERA EN EUROS
elif opcion == 2:
    convertidor("Euros", 1.09)
# SI LA OPCION ES 3 ENTONCES EL VALOR SERA EN YUANES
elif opcion == 3:
    convertidor("Yuanes", 0.16)
# DE NO CUMPLIRSE NINGUNA ANTERIOR SE LE PIDE AL USUARIO QUE INGRESE UN VALOR CORRECTO
else:
    print(f'ingresa una opcion correcta por favor')

#Ahora vamos a hacer lo mismo con funciones











