"""Un generador es un iterador escrito de forma elegante
en python, esto es sugar sintaxis"""

def my_gen():
    """ejemplo de generador"""
    
    print('Hello World')
    n = 0
    yield n
    
    print('Hello Heaven')
    n = 1
    yield n
    
    print('Hello Hell')
    n = 2
    yield n
    
a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a)) #StopIteration

#GENERATOR EXPRESSION
my_list = [0,1,4,7,9,10]

my_second_list = [x*2 for x in my_list] #list comprehension
my_second_gen = (x*2 for x in my_list) #list comprehension
