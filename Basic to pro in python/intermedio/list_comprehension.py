def run():
    #Esto es una forma de hacerlo sin list comprehension
    squares = []
    for i in range(1, 101):
        squares.append(i**2)
    
    print(squares)

    squares2 = []
    for i in range(1, 101):
        if i % 3 != 0:
            squares2.append(i**2)
            
    #esta es la estructura de una list comprehension: valor + ciclo for + condicion (obligatoria)
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)
    
    multiplos = [i for i in range(1,10000) if i%4==0 and i%6==0 and i%9==0]        
    print(multiplos)
    
    

if __name__ == '__main__':
    run()