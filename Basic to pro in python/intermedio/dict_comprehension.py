def run():
    #forma de hacerlo sin dict comprehension
    my_dict = {}
    for i in range(1,101):
        my_dict[i] = i**3
    
    my_dict = {}
    for i in range(1, 101):
        if i%3!=0:
            my_dict[i] = i**3
    
    #la estructura del dict comprehension es el id: resultado + un ciclo for + condicion (opcional)
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0 }
    
    my_dict = {i: pow(i, 1/2) for i in range(1,1001)}
        
    print(my_dict)


if __name__ == '__main__':
    run()