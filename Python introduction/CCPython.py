"""CRASH COURSE IN PYTHON"""

"""WHITESPACE FORMATTING"""

for i in [1,2,3,4,5]:
    print(i)                #primera linea en el bloque for i
    for j in [1,2,3,4,5]:   
        print(j)            #primera linea en el bloque for j
        print(i+j)          #la ultima linea en el bloque for j
    print(i)                #ultima linea en el bloque for i
    print("done looping")

#Los espacios en blanco ayudan a leer mejor el codigo
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

#podemos usar el \ para indicar que el codigo continua en la siguiente linea

two_plus_three = 2 + \
                 3
                 
#la consecuencia de los espacios en blanco es que se hace dificil copiar y pegar 

for i in [1, 2, 3, 4, 5]:
# notice the blank line
    print(i)

    """MODULOS DE PYTHON"""

#existen funciones que deben ser cargadas para funcionar
#una de las formas mas faciles de hacerlo es la siguiente

from cgitb import lookup
import re
from tokenize import single_quoted

from numpy import empty
my_regex = re.compile("[0-9]+", re.I)

#si ya cargaste re en tu codigo podrias usar un alias
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

#podemos cargar matplotlib para visualizar data
import matplotlib.pyplot as plt
plt.plot(...)

#si necesitamos valores especificos de un modulo podemos importarlos
#de forma explicita usandolos sin calificacion

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

#si fueramos malas personas importariamos todos los contenidos de los modulos
#dentro tu espacio, pero eso podria sobreescribir variables que ya habiamos definido

match = 10
from re import *    #uh oh, re has a match function
print(match)        #"<function match at 0x012644A8>"

#si no sos una mala persona no hagas eso nunca

"""FUNCIONES"""
#En python las funciones se definen usando def

def double(x):
    """aqui podemos poner un docstring para explicar lo que hace la funcion

    Args:
        x (_type_): _description_
    """
    return x*2

def apply_to_one(f):
    """Llamada de funcion f con 1 como su argumento"""
    return f(1)

my_double = double  #se refiere a la funcion definida previamente
x = apply_to_one(my_double) #igual a 2

#se puede crear una funcion corta anonima o lambda
y = apply_to_one(lambda x: x + 4)   #igual a 5

#puedes asignar lambdas a las variables, no obstante muchas personas
#diran que solo deberias usar un def 

another_double = lambda x: 2 * x #don´t do this

def another_double(x):
    """do this instead"""
    return 2 * X

#los parametros de las funciones pueden dar argumentos por defectos donde
#solo se necesitan especificar el valor que quieres que sea por default

def my_print(message = "my default message"):
    print(message)
my_print("hello")   #Prints "hello"
my_print()          #prints my default message

#a veces es util especificar argumentos por nombre

def full_name(first = "what´s-hit-name", last = "Something"):
    return first + " " + last

full_name("Joel", "Grus")   #"Joel Grus"
full_name("Joel")           #"Joel Something"
full_name(last="Grus")      #"What´s-hit-name Grus"

"""STRINGS"""
#los strings pueden definirse con doble o con comillas simples

single_quoted_string = 'data science'
double_quoted_string = "data science"

#python usa el backlash para codificar los caracteres especiales
tab_string = "\t"       #representa el caracter tab
len(tab_string)         #is 1

#si quieres backslashes que sirvan como rutas de directorio se puede hacer
#creando raw string usando r"":

not_tab_string = r"\t"  #represents the characters '|' and 't'
len(not_tab_string)     #is 2

#se pueden crear strings multiline usando tres comillas
multi_line_string = """This is the first line
and this is the second line
and this is the third line
"""

#nueva funcion de python 3.6 es f-string esto permite sustituir valores dentro de los strings
#por ejemplo

first_name = "Joel"
last_name = "Grus"

#deberiamos combinar esto en un nombre completo, hay muchas maneras de hacerlo

full_name1 = first_name + " " + last_name   #string addition
full_name2 = "{0} {1}".format(first_name, last_name) #string.format

#pero los f-strings los resuelven con menos

full_name3 = f"{first_name} {last_name}"

"""EXCEPCIONES"""

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

#las excepciones hacen que tu codigo se vuelva mas simple

"""LISTAS"""

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list) # equals 3
list_sum = sum(integer_list) # equals 6

#se puede obtener o setear el nth de elementos de una lista con llaves cuadradas
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zero = x[0] # equals 0, lists are 0-indexed
one = x[1] # equals 1
nine = x[-1] # equals 9, 'Pythonic' for last element
eight = x[-2] # equals 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, 3, ..., 9]

#podes usar brackets cuadrados para deslizar listas, se hace con
# "i:j" que significan los elementos desde i hasta j

first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, ..., 8]
copy_of_x = x[:] # [-1, 1, 2, ..., 9]

"""Se pueden crear slice de strings de forma secuencial"""
"""un slice que tome los argumentos en la posicion 3"""

every_third = x[::3]    #[-1, 3, 6, 9]
five_to_three = x[5:2:-1]   #[5, 4, 3]

#python tiene un operador para checkear los miembros dentro de una lista

1 in [1, 2, 3] #true
0 in [1, 2, 3] #false

#PODES CONCATENAR LISTAS USANDO LA FUNCION EXTEND
x = [1, 2, 3]
x.extend([4, 5, 6])

#si no quieres modificar x puedes usar una adicion de listas
x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6]; x no cambio

"""Se usa mas frecuentemente el append para añadir valores
de uno en uno a una lista"""

x = [1, 2, 3]
x.append(0)     #x is now [1, 2, 3, 0]
y = x[-1]       # is 0
z = len(x)      # is 4

#a veces es combeniente desempaquetar listas cuando no sabes cuantos elementos tiene

x, y = [1, 2] #ahora x es 1, y es 2

#un idiom comun para tirar un valor que no vas a usar es

_, y = [1, 2]   # ahora y == 2

"""TUPLAS"""
#las tuplas son listas con cousins inmutables.

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3  # my_list is now [1, 3]

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

#las tuplas son convenientes para regresar multiples valores de una funcion

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(2, 3)  # sp is (5, 6)
s, p = sum_and_product(5, 10)   #s is 15, p is 50

#las tuplas y las listas ademas son usadas para multiples tareas

x, y = 1, 2     # now x is 1, y is 2
x, y = y, x     # pythonic way to swap variables; now x is 2, y is 1

"""DICTIONARIES"""
#los dictionarios asocian valores con keys y te permiten obtenerlos rapidamente con la keys

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}

#podes buscar el valor de una llave usando los brackets cuadrados

joels_grade = grades["Joel"]   # equals 80

#podes crear alertas de error si no esta el elemento que buscas en el dict

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate:")

#podes testear la existencia de una key usando in

joel_has_grade = "Joel" in grades #true
kate_has_grade = "Kate" in grades #false

#los diccionarios tienen un metodo que regresa valores por default
#incluso sin hacer excepciones

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("kate", 0)
no_ones_grade = grades.get("No one")

"""Podes asignar keys por pares usando los mismos squares cuadrados"""

grades["Tim"] = 99      #reemplaza el valor anterior
grades["Kate"] = 100    #añade una tercera entrada
num_students = len(grades)  #es igual 3

#podes usar diccionarios para estructurar datos
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

#despues vamos a ver un mejor aproximacion
"""en vez de buscar keys especificas podemos mirarlas a todas"""

tweet_keys = tweet.keys()   #iterable para las llaves
tweet_values = tweet.values()   #iterable para los valores
tweet_items = tweet.items()     #itarable para las tuplas

"user" in tweet_keys    #true, but not pythonic
"user" in tweet         #pythonic way of checking keys
"joelgrus" in tweet_values  #true (es lento pero es la unica forma de checkearlo)

"""DEFAULT DICTS"""
#imagina que tenes queres contar las palabras en un documento
#podes crear un diccionario donde las keys sean palabras y los valores las cuentas
#podes agregar las palabras que contes a un diccionario si no las cuentas no

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

#otra aproximacion es hacerlo viendo el comportamiento para los missing keys

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
    
"""Se puede crear un diccionario por defecto usandolo desde un package"""

from collections import defaultdict

word_counts = defaultdict(int)      #int produce 0
for word in document:
    word_counts[word] += 1

#ellos pueden ser ademas utiles con una lista o directorio, or incluso tus propias funciones

dd_list = defaultdict(list)         #list() produce una lista vacia
dd_list[2].append(1)                # ahora dd_list contiene {2: [1]}

dd_dict = defaultdict(dict)         #dict() produce una lista vacia
dd_dict["Joel"]["City"] = "Seattle" #{"Joel" :{"City" : Seattle"}}

dd_pair = defaultdict(lambda: [0,0])
dd_pair[2][1] = 1                   #ahora dd_pair contiene {2: [0. 1]}

#esto es util para recoger resultados almacenandolos en un diccionario

"""CONTADORES"""

#un contador regresa una secuencia de valores dentro de un diccionario por defecto
#es un dic int como un objeto que mapea el conteo de las keys

from collections import Counter
c = Counter([0, 1, 2, 0])       # c is basically {0: 2, 1: 1, 2: 1}

#esto nos puede ayudar para resolver el problema del conteo de palabras

#recall, document is a list of word
word_counts = Counter(document)

#hay otro metodo de cuenta que es usado frecuentemente

#imprime los 10 mas comunes y su conteo
for word, count in word_counts.most_common(10):
    print (word, count)

"""SETS"""
#Esta es una util estructura de datos, representa una collecion
#de distintos elementos que poder definir seteandolos por lista de elemento entre corchetes
    
primes_bellow_10 = {2, 3, 5, 7} 

#para generar sets vacios hay que hacer set()

s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s

#se usan mas los set porque se pueden hacer cosas mas rapidas
#y por si tenemos una larga collection de items que queremos usar para un test de membresia

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]
"zip" in stopwords_list # False, but have to check every element
stopwords_set = set(stopwords_list)
"zip" in stopwords_set # very fast to check

#la segunda raon is para encontrar distinto item en una colleccion

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

"""CONTROL FLOW"""
#PODEMOS USAR UNOS CONDICIONALES PARA HACER COSITAS

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

#podes escribir una terna if-then-else en una linea

parity = "even" if x % 2 == 0 else "odd"

#python tiene un loop while
x = 0
while x < 10: 
    print(f"{x} is less than 10")
    x += 1

#si necesitas una logica mas compleja podes usar un continue o un brake

for x in range(10):
    if x == 3:
        continue #go immediately to the next iteration
    if x == 5:
        break #sale del loop
    print(x)

"""VERACIDAD EN PYTHON"""
#SE USAN BOOLEANOS EN PYTHON Y EN OTROS LENGUALES 

one_is_less_than_two = 1 < 2 # equals True
true_equals_false = True == False # equals False

x = None
assert x == None, "this is the not the Pythonic way to check for None"
assert x is None, "this is the Pythonic way to check for None"

"""formas de obtener un false"""

# False
# None
# []
# {}
# ""
# set()
# 0
# 0.0

s = some_function_that_returns_a_string()
if s:
    first_char = s[0]
else:
    first_char = ""

# una forma mas corta pero confusa de hacer lo mismo es

first_char = s and s[0]

#similarmente si x is otro numero o posiblemente none

safe_x = x or 0

#es definitivamente un numero ademas

safe_x = x if x is not None else 0

#es posiblemente mas legible

"""python tiene todas las funciones que toman e iteran true cuado
el elemento es true, aqui hay algunas de esas funciones"""

all([True, 1, {3}]) #true, all are truthy
all([True, 1, {}])  #false, {} is falsy
any([True, 1, {}])  #true, es truthy
all([])             #true, no falsy
any([])             #false, no truthy elements in the list

"""ORDENANDO"""
#todo elemento en python puede ser ordenado

x = [4, 1, 2, 3]
y = sorted(x) # y is [1, 2, 3, 4], x is unchanged
x.sort() # now x is [1, 2, 3, 4]

#por defecto las funciones lo ordenan del pequeño al mas grande
#si lo quieres ordenar de mayor a menor, se puede especificar el rever









