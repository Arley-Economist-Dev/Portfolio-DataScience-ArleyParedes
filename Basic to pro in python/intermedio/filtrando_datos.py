DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #encontrando los desarrolladores que solo programan en python con list comprehension
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #encuentro los trabajadores que trabajan en python con list comprehension 
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"]== "Platzi"] 
    
    #aqui se usa filter para encontrar a los mayores de edad
    adults = list(filter(lambda worker: worker["age"] > 18,DATA))
    #se sobreescribe la linea de arriba usando map para que solo aparezcan los nombres 
    adults = list(map(lambda worker: worker["name"], adults)) 
    
    #aqui se usa map para agregar una variable booleana sobre los datos para ver cuales son mayores de 70 años
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) 

    # Resolviendo con list comprehensions
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]
    
    #Con high order functions
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))

    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
        
    for worker in all_python_devs:
        print(worker)
        
    for worker in all_platzi_workers:
        print(worker)
        
    for worker in adults:
        print(worker)
    
    for worker in old_people:
        print(worker)

if __name__ == '__main__':
    run()