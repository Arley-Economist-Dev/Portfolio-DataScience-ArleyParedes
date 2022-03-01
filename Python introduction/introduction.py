# Here is the charge of a dict for data
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}
# And loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j) # Add j as a friend of user i
    friendships[j].append(i) # Add i as a friend of user j

    """ ¿Cual es el numero de conexiones sociales de los usuarios en el diccionario?
        Esto se hara sumando las longitudes de listas de amigos
    """
    
def number_of_friends(user):
    """How many friends does _user_ have"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                        for user in users) # 24

#Ahora solo se divide por el numero de usuarios
num_users = len(users)  #longitud de la lista de usuarios
avg_connections = total_connections / num_users #24 / 10 == 2.4

#Create a list (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]                                #largest to smallest

# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

#este es el algoritmo para mostrar gente que podrias conocer
#Design Data science you may know
#foaf is the short of friend of a friend

def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return[foaf_id
           for friend_id in friendships[user["id"]]
           for foaf_id in friendships[friend_id]]
    
[0, 2, 3, 0, 1, 3]

print(friendships[0]) # [1, 2]
print(friendships[1]) # [0, 2, 3]
print(friendships[2]) # [0, 1, 3]

from collections import Counter

from numpy import average     #cargando paquete counter
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]       #por cada quien se amigo
        for foaf_id in friendships[friend_id]       #busca a sus amigos
        if foaf_id != user_id                       #que no son los mios
        and foaf_id not in friendships[user_id]     #y que no son mis amigos
    )
    
print(friends_of_friends(users[3]))         #Resultado: Counter({0: 2, 5: 1})

#Vamos a crear un algoritmo para conocer 
#usuarios que compartan los gustos o intereses 
#similares a los mios

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

#el id 0 no tiene amigos en comun con el id 9 pero tienen los mismo intereses
#en java y en big data

def data_scientists_who_likes(target_interest):
    """Encuentra los id de todos los usuarios que les gusta target"""
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]
    
#esto funcionaria pero tiene que buscar en toda la lista de interes 
#por cada busqueda
#seria mejor si se construye un index de intereses para usuarios

from collections import defaultdict

#las keys son intereses, los valores de la lista de user_id con ese interes
user_id_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_id_by_interest[interest].append(user_id)

#y ahora otro del interes de los usuarios

#las keys user_ids, valores son listas de interes para el user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

    """ahora es facil encontrar quien es el que tiene mas intereses en common ingresando
    un usuario con los siguientes pasos
    1- interando sobre los intereses de los usuarios
    2- para cada interes, interar sobre los otros usuarios con los mismos intereses
    3- mantenga contando cuantas veces se vieron uno al otro
    """
#en codigo seria

def most_common_interest_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_id_by_interest[interest]
        if interested_user_id != user["id"]
    )

"""Salarios y Experiencia otra seccion"""
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

#Segun los datos las personas con mas experiencia tienden a ganar mucho mas
#como podemos comprobar esto como un hecho
#la primera idea es ver el salario promedio

#keys son años, los valores son listas de salarios por cada tenure
from collections import defaultdict
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

#las keys son años, cada valor es el salario promedio de use tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

{8.7: 83000.0, 
 8.1: 88000.0, 
 0.7: 48000.0, 
 6: 76000.0, 
 6.5: 69000.0, 
 7.5: 76000.0, 
 2.5: 60000.0, 
 10: 83000.0, 
 1.9: 48000.0, 
 4.2: 63000.0}

#Ahora vamos a agrupar los tenures

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

#Ahora podemos agrupar los salarios a su bucket correspondiente

#las keys son buckets, valores son listas de salarios para ese bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

#Ahora finalmente computamos el average de los salario para cada grupo

#las keys son tenure buckets, los valores son el promedio del salario para cada bucket
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

#Resultado
{'more than five': 79166.66666666667, 
 'less than two': 48000.0, 
 'between two and five': 61500.0}

"""Interpretacion: podemos conocer que dentro de ese dataframe
los data scientist con mas de cinco años de experiencia ganan 
un 65% mas que un cientifico de datos con poco o sin ninguna experiencia
"""

#PAID ACCOUNTS









