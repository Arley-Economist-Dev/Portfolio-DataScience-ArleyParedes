def run():
    
    #resolviendo para seleccionar solo numeros primos con list comprehension
    my_list = [1,4,5,6,9,13,19,21]
    
    odd = [i for i in my_list if i % 2 != 0]
    
    print(odd)
    
    #resolviendo utilizando el metodo de filter
    my_list = [1,4,5,6,9,13,19,21]
    
    odd = list(filter(lambda x: x % 2 != 0, my_list))
    
    print(odd)
    
    #haciendo que los valores de una lista retornen su cuadrado
    my_list = [1,2,3,4,5]
    my_list = [i**2 for i in my_list]
    my_list = [i**2 for i in range(1,6)] #esta es una alternativa
    print(my_list)
    
    #uso de map
    my_list = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list))
    print(squares)
    
    #sumando los valores de una lista con un ciclo for
    my_list = [2,2,2,2,2]
    all_multiplied = 1
    
    for i in my_list:
        all_multiplied = all_multiplied * i
        
    print(all_multiplied)
    
    #funcion reduce
    from functools import reduce
    
    my_list = [2,2,2,2,2]
    all_multiplied = reduce(lambda a, b: a * b, my_list)
    print(all_multiplied)
    

if __name__ == '__main__':
    run()