"""Los sets son una estructura de datos que:
1- contienen datos que no se repiten
2- los elementos son inmutables"""

# Como se crean?

my_set = {3, 4, 5}
print("my_set = ", my_set)  #my_set = {3,4,5}

my_set2 = {"hola", 23.3, False, True}
print("my_set2= ", my_set2) #my_set2 = {false, true, 'hola', 23.3}

my_set3 = {3, 3, 2}
print("my_set3= ", my_set3) #my_set3 = {2,3}

my_set4 = {[1,2,3], 4}
print("my_set4= ", my_set4) #error

#se pueden crear set vacios

#this is a dictionary
empty_set = {}
print(type(empty_set))

#se usa la funcion building set
empty_set = set()
print(type(empty_set))

#ejemplos
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)

#modulos de los sets

my_set = {1,2,3}
print(my_set)

#añadir un elemento
my_set.add(4)
print(my_set)

#añadir multiples elementos
my_set.update([1,2,5])
print(my_set)

#añadir multiples elementos
my_set.update((1,7,2),{6,8})
print(my_set)

#modulos para borrar sets
my_set = {1,2,3,4,5,6,7}
print(my_set)

#Borrar un elemento existente
my_set.discard(1)
print(my_set)

#borrar un elemento existente
my_set.remove(2)
print(my_set)

#Borrar un elemento inexistente
my_set.discard(10)
print(my_set)

#Borrar un elemento inexistente
my_set.remove(12)
print(my_set)   #este arroja un error porque no se 
                #permite borrar elementos inexistentes con remove
                
#Otros modulos de set
my_set = {1,2,3,4,5,6,7}
print(my_set)

#borrar un elemento aleatorio
my_set.pop()
print(my_set)

#limpiar el set
my_set.clear()
print(my_set)

"""Operaciones con sets"""

#uniones
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 | my_set2
print(my_set3)

my_set3 = my_set1.union(my_set2)

#interseccion
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 & my_set2
print(my_set3)

my_set3 = my_set1.intersection(my_set2)

#Diferencias
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 - my_set2
print(my_set3)

my_set4 = my_set2 - my_set1
print(my_set4)

my_set5 = my_set1.difference(my_set2)

#diferencia simetrica
my_set1 = {3,4,5}
my_set2 = {5,6,7}

my_set3 = my_set1 ^ my_set2
print(my_set3)

my_set4 = my_set1.symmetric_difference(my_set2)