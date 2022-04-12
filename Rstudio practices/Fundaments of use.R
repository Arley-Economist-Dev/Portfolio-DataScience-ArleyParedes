setwd("") #Esto es para definir la ubicacion del directorio

#R como calculadora

1+1

1/25*87

(8+4*5)/3

round(pi,digits = 8)

sin(pi/2)

tan(pi/6)

sqrt(64)

log(7, base = 8)

e(1)

exp(2)

2^5

factorial(5)

choose(6,2) #numero combinatorio

x = 2*3

x <- sqrt(32)

round(sqrt(45), 3) -> x

x <-  sin(pi/4)

#reglas para programar

# 1 - los objetos empiezan por letras
variable_creada_con_snake_case <- sqrt(5)

VariableCreadaConCamelCase <- sqrt(6)

variable.separada.por.puntos <- sqrt(5)

#Funciones en R

function_name(arg1 = val1, arg2 = val2)

round(pi, digits = 15)

seq(1,12,by = 3) #genera secuencia de numeros

x <- "Hola mundo"

y <- seq(1,12,length.out = 8)

y[8] #los arrays sirven para encontrar el valor del numero en el orden

#Scripts y modos de trabajo en R

getwd() #para conocer el directorio de trabajo donde se esta almacenando la info

setwd("/Users/Pasante/Downloads/")

setwd("~/Curso de R/Fundamentos de uso/") #esa expresion nos lleva directo a documentos

#Grafico Bonus
ggplot(diamonds, aes(carat,price)) +
  geom_hex()

ggsave("Curso de R/Fundamentos de uso/diamonds_hex.pdf") #guardar plots en pdf

write_csv(diamonds, "Curso de R/Fundamentos de uso/diamonds.csv") #guardar dataframes en tipo csv



