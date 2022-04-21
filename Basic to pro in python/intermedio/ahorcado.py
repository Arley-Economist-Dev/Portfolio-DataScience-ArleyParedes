from random import randint
from os import system

def read():
    with open("./archivos/data.txt", "r", encoding='utf-8') as f:
        words = [i.replace('\n','') for i in f]
    return(words)

def comparison(word, lineas):
    w=list(word)
    l=list(lineas)
    usuario = ''
    while w != l or usuario == 'dedo':
        usuario = input('ingrese una letra: ')
        
        assert len(usuario) == 1, '!!!Presionaste mas de una letra¡¡¡'
        system('clear')
        for i in range(0, len(w)):
            if w[i] == usuario:
                l[i] == w[i]
        print(' '.join(l).upper())
        print('\n')
        
    print('!Ganaste la palabra era¡ ' + word.upper())

def run():
    words = read()
    index = randint(0, len(words))
    word = words[index]
    lines = '-'*len(word)
    
    print('!Adivina la palabra¡')
    print(' '.join(lines))
    print('\n')
    
    comparison(word, lines)
    
if __name__ == '__main__':
    run()