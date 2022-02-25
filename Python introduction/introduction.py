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

num_friends_by_id.sort(                             #sort the list
    key=lambda id_and_friends: id_and_friends[1],   #by num_friends
    reverse = True)                                 #largest to smallest

# Each pair is (user_id, num_friends):
# [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
# (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]

#Design Data science you may know
#foaf is the short of friend of a friend
