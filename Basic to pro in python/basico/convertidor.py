def convertidor(tipo_moneda, valor_dolar):
    u_monetaria = float(input("¿Cuantos "+ tipo_moneda + " tienes?: "))
    dolares = u_monetaria / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes " + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas a dolares 💵💴💶💷

1- Cordobas a dolares
2- Euros a dolares
3- Yuanes a dolares

Elige una opcion: """

opcion = int(input(menu))

if  opcion == 1:
    convertidor("Cordobas", 35.67)
elif opcion == 2:
    convertidor("Euros", 1.09)
elif opcion == 3:
    convertidor("Yuanes", 0.16)
else:
    print(f'ingresa una opcion correcta por favor')

#Ahora vamos a hacer lo mismo con funciones











