"""Programa para eliminar los repetidos de una lista"""
# [1, 1, 2, 2, 4] -> [1,2,4]

def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))

#es lo mismo de arriba
def run():
    my_list = [1,1,2,2,4]
    my_set = set(my_list)
    print(my_set)
   
if __name__ == '__main__':
    run()