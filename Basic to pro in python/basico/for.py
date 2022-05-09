# Se genera una variable contador que empieza en 1
contador = 1
# se imprime el contador
print(contador)
# mientra el contador sea menor a mil
while contador < 1000:
    #el contador se ira sumando cada elemento en cada iteracion
    contador += 1   # +mas igual es un incremento automatico
    #se imprimira el contador mientras tanto
    print(contador)
    
#de esta forma se haria en un ciclo for esto es mas simple
# para cada Valor de contador en un rango de 1 a 1000
for contador in range(1, 1001):
    #se imprimira el contador
    print(contador)
    
#para cada elemento en el rango a 10
for i in range(10):
    # se imprime 11 multiplicado por el elemento
    print(11 * i)