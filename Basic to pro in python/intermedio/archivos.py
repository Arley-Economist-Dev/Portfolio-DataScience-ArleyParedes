def read():
    #creamos una lista vacia que va contener los numeros del archivos
    numbers = []
    #Abrimos el archivo, se codifica en utf 8 para evitar problemas de compatibilidad
    with open("./archivos/numbers.txt","r", encoding = "utf-8") as f:
        for line in f:
            numbers.append(int(line))
            #print(numbers) si dejas esto aqui se imprime secuencialmente
    print(numbers)
    
def write():
    #aqui si hace lo contrario a partir de una lista creamos un archivo
    names = ["Sonia","Amalia","Jhonny","Jahoska","Xochilt"]
    #el alias as simboliza la conexcion de python con el archivo
    #with open("./archivos/names.txt", "w", encoding = "utf-8") as n:
    with open("./archivos/names.txt", "a", encoding = "utf-8") as n:
        #en este ciclo se recorren los nombre y \n es un espaciado
        for name in names:
            n.write(name)
            n.write("\n")

def run():
    """
    Modos de Apertura

r -> Solo lectura
r+ -> Lectura y escritura
w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
a -> Añadido (agregar contenido). Crea el archivo si éste no existe
a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

"""

    #with open(<ruta>, <modo_apertura>) as <nombre>:
    #read()
    write()

if __name__ == '__main__':
    run()