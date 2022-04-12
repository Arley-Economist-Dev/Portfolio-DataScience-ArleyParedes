setwd("~/Curso de R/Transformacion de los datos/")

library(tidyverse)

#-- Attaching packages ----------------------------------------------------------------- tidyverse 1.3.1 --
#  v ggplot2 3.3.5     v purrr   0.3.4
#v tibble  3.1.5     v dplyr   1.0.7
#v tidyr   1.1.4     v stringr 1.4.0
#v readr   2.0.2     v forcats 0.5.1
#-- Conflicts -------------------------------------------------------------------- tidyverse_conflicts() --
#  x dplyr::filter() masks stats::filter()
#x dplyr::lag()    masks stats::lag()

library(nycflights13)

nycflights13::flights

?flights

#Empezamos a trabajar con tibbles

## filter <- filtrar datos a partir de valores concretos
## arrange <- reoordenar las filas 
## select <- seleccionar variables a sus nombres
## mutate <- crear nuevas variables con funciones a partir de las existentes
## summarize <- colapsar varios valores para dar un resumen de los mismos

## group_by <- agrupar datos en funcion de los parametros

## 1 <- data frame
## 2 <-  operaciones que queremos hacer a las variables del dataframe
## 3 <- Resultado en un nuevo data frame

#filtrado de datos#
jan1 <- filter(flights, month == 1, day == 1)
oct24 <- filter(flights, month == 10, day == 24)
(dic25 <- filter(flights, month == 12, day == 25))

near(sqrt(2)^2, 2)

near(1/49*49, 1)

#Algebra Booleana en R

filter(flights, month == 5 | month == 6)
filter(flights, month == 5 | 6) #esto no esta permitido

may_june <- filter(flights, month %in% c(5,6))

# !(x&y) == (!x)|(!y)
# !(x|y) == (!x)&(!y)

filter(flights, !(arr_delay > 60 | dep_delay > 60))
filter(flights, arr_delay <= 60, dep_delay <= 60)

#Valores de NA

NA > 0
NA == 10
NA + 5
NA / 5
NA == NA

## se desconoce un dato
dato1 <- NA
dato2 <- NA

dato1 == dato2

is.na(dato1)

df <- tibble(x = c(1,2,NA,4,5))
view(df)
filter(df, is.na(x)|x>2)

#Ordenando datos con Arrange
head(flights, 10)
tail(flights, 10)

### ARRANGE
arrange(flights, year)
sorted_date <- arrange(flights, year, month, day)

tail(sorted_date)

arrange(flights, desc(arr_delay))
head(arrange(flights, desc(arr_delay)))

arrange(flights, desc(dep_delay))

view(arrange(flights, carrier))

arrange(flights, distance)

#--------------------- Tarea 1 ------------------------------------------------#

?flights

#Encuentra todos los vuelos que llegaron más de una hora tarde de lo previsto.

filter(flights, arr_delay > 60)

#Encuentra todos los vuelos que volaron hacia San Francisco (aeropuertos SFO y OAK)

(filter(flights, dest == "SFO" | dest == "OAK"))

#Encuentra todos los vuelos operados por United American (UA) o por American Airlines (AA)

filter(flights, carrier == "UA" | carrier == "AA")

#Encuentra todos los vuelos que salieron los meses de primavera (Abril, Mayo y Junio)

spring_flights <- (filter(flights, month %in% c(4,5,6)))

# Encuentra todos los vuelos que llegaron más de una hora tarde pero salieron con menos de una hora de retraso.

filter(flights, arr_delay > 60 & dep_delay < 60)

# Encuentra todos los vuelos que salieron con más de una hora de retraso pero 
# consiguieron llegar con menos de 30 minutos de retraso (el avión aceleró en el aire)

filter(flights, dep_delay > 60 & arr_delay < 30)

#Encuentra todos los vuelos que salen entre medianoche y las 7 de la mañana (vuelos nocturnos).

filter(flights, hour %in% c(0,1,2,3,4,5,6,7))
filter(flights, hour <= 7)

#funcion between
?between
# between(variable, limite inferior, limite superior)

filter(flights, between(hour, 0, 7))

# ¿Cuantos vuelos tienen un valor desconocido de dep_time?
8255
filter(flights, dep_time %in% NA)

#¿Qué variables del dataset contienen valores desconocidos? 
#¿Qué representan esas filas donde faltan los datos?

?flights
contiene_na <- flights[rowSums(is.na(flights)) > 0, ]     
view(contiene_na)

# dep_time, dep_delay, arr_time, arr_delay, tailnum, air_time

#pregunta Final

NA^0 #resultado 1
NA|TRUE #el resultado es un true
FALSE & NA #el resultado es un false
NA*0 #el resultado es NA

#Se retorna NA cuando la operacion es matematica y cuando es logica se retorna el valor logico.

#--------------------- Select function------------------------------------------------#

sorted_date <- (arrange(flights, carrier))

view(sorted_date[1,])
view(sorted_date[1:3,])
view(sorted_date[1024:1068,])

select(sorted_date[1024:1068,], dep_delay, arr_delay)

view(select(sorted_date[1024:1068,], dep_delay, arr_delay))

select(flights, year, month, day)

select(flights, dep_time:arr_delay)

select(flights, -(year:day))

select(flights, starts_with("dep"))

select(flights, ends_with("delay"))

select(flights, contains("s"))

select(flights, matches("(.)\\1")) #expression regular repetida

select(flights, num_range("x", 1:5))

?select 

#renonbrar y reordenar columnas

rename(flights, deptime = dep_time)
#esto sirve para cambiar el nombre, a la izquierda nombre nuevo, derecha nombre antiguo

select(flights, deptime = dep_time)

select(flights, time_hour, distance, air_time, everything())

#--------------------- TAREA 2------------------------------------------------#

?flights

#Pregunta 1
arrange(flights, !is.na(dep_delay), dep_delay)

#pregunta 2
arrange(flights, desc(dep_delay))
view(arrange(flights, dep_delay))

#Se encuentran vuelos con mas de 1300 minutos de retraso y vuelos de que han salido
#hasta 43 minutos antes de los previsto.

#Pregunta 3

?flights

df <- df %>% mutate(c = a * b)

view(head(velocidad <- flights %>% mutate(velocidad = distance/air_time)))
view(head(arrange(velocidad, desc(velocidad))))

#El más retrasado fue: 
  arrange(flights, desc(dep_delay))[1,] 

#El menos retrasado fue: 
  arrange(flights, dep_delay)[1,]

#se calcula la velocidad usando distancia entre tiempo, se calcula la velocidad
#promedio en millas por minuto a la que los vuelos viajan, se encuentran 4 vuelos
#que viajan por encima de 10 millas por minuto

#Pregunta 4
view(head(arrange(flights, desc(distance))))

#Los aeropuertos que alojan los vuelos mas largos son el JFK y el HNL

#Pregunta 5
view(head(arrange(flights,distance)))

#los vuelos mas cortos son los del EWR hacia LGA; o de EWR hacia PHL.

#Pregunta 6
#dep_time, dep_delay, arr_time, arr_delay

select(flights, dep_time, dep_delay, arr_time, arr_delay)
select(flights, dep_time, dep_delay, arr_time, arr_delay, everything())
select(flights, dep_time:arr_delay)
select(flights, starts_with("dep") | starts_with("arr"))

#Pregunta 7
select(flights, dep_time, dep_time, dep_time, dep_time)

#solamente toma el primer valor de la variable el resto los ignora

#Pregunta 8
?one_of()

#One of es una funcion que ayuda a buscar coincidencias dentro de columnas
#Que contienen datos de tipo string

#Pregunta 9
flights <- as_tibble(flights)
ejemplo <- c("year", "month", "day", "dep_delay", "arr_delay")
flights[,ejemplo]
flights %>% select(all_of(ejemplo))

#permite encontrar las coincidencias dentro del dataframe para las columnas
#que tienen el mismo nombre de las variables string de esos vectores

#pregunta 10
select(flights, contains("time"))
?select

#Esta sentencia muestra todas las columnas que contienen la palabra time en el nombre
#podriamos utilizar otros selection helpers para matchear coincidencias con el nombre

#--------------------- NUEVAS VARIABLES------------------------------------------------#

##MUTATE

view(flights_new <-  select(flights,
                       year:day,
                       ends_with("delay"),
                       distance,
                       air_time))

mutate(flights_new, 
       time_gain = arr_delay - dep_delay, #diff_t (min)
       flight_speed = distance/(air_time/60), #v = d/t (km/h)
       time_gain_per_hour = time_gain/(air_time/60)
       ) -> flights_new

transmute(flights_new,
          time_gain = arr_delay - dep_delay,
          air_time_hour = air_time/60,
          flight_speed = distance / air_time_hour,
          time_gain_per_hour = time_gain / air_time_hour) -> data_from_flights

# * Operaciones Aritmeticas +, - , *, /, ^
# * Agregados de funciones: x/sum(x) : proporcion sobre el total
#                   x = mean(x)
#                   (x = mean(x))/sd(x): tipificacion
#                   (x- min(x))/(max(x) - min(x)) : z score
#
# * Aritmetica modular: %/% -> cociente de la division entera, %% resto de la division
#                   x == y * (x%/%y) + (x%%y)

transmute(flights,
          air_time,
          hour_air = air_time %/% 60,
          minute_air = air_time %% 60)

# Uso de logaritmos: log() <- log base e, log2(), log10()
# offsets: lead(), lag()

df <- c(1:12)
lag(df)
lead(df)

#funciones acumulativas: cumsum(), cumprod(), cummax(), cummean()
cumsum(df)
cumprod(df)
cummax(df)
cummin(df)
cummean(df)

# Comparaciones logicas: >, <, >=, <, <=, ==, !=
transmute(flights,
          dep_delay,
          has_been_delayed = dep_delay > 60)

# * Rankings: min_rank()
df <- c(7,1,2,5,3,3,8,NA,3,4,-2)
df
min_rank(df)

df
min_rank(desc(df))

df
row_number(df)

df
dense_rank(df)

df
percent_rank(df)

df
cume_dist(df)

df 
ntile(df, n= 4)  #Genera percentiles

transmute(flights,
          dep_delay,
          ntile(dep_delay, n = 100))

#--------------------- TAREA NUMERO 3------------------------------------------------#

#Ejercicio 1
view(head(flights))

#dep_time, sched_dep_time

mid_night <- mutate(flights,
                    tiempo_real = (dep_time*60)/100,
                    tiempo_schedulel = (sched_dep_time*60)/100
)
                    
view(head(mid_night))

#Ejercicio 2
# air_time arr_time - dep_time.

?flights
compara <- transmute(flights,
                     air_time,
                     comparacion = arr_time - dep_time
                     )
view(select(compara[1:50,], air_time, comparacion))

#esperaba ver una comparativa de el tiempo de aire en minutos y por otro las
#horas que tomo el vuelo en llegar hasta su destino

# veo que la comparativa no se puede realizar por que los datos estan en magnitudes
# diferentes

# se puede corregir transformando las horas para que sean equivalentes 
# a minutos y eso se hace asi

mutate(compara,
       tiempo_aire = air_time,
       comparacion_transformada = (comparacion*60)/100
       )

#Ejercicio 3

#dep_time, sched_dep_time, dep_delay

?flights

comparacion2 <- transmute(flights,
                          atraso_salida = dep_delay,
                          tiempo_calendario = (sched_dep_time*60)/100,
                          tiempo_efectivo = (dep_time*60)/100
                          )
view(select(comparacion2[1:50,],
            atraso_salida,
            tiempo_calendario,
            tiempo_efectivo)
)

#Esto muestra una comparativa que efectivamente muestra el tiempo de retraso

#Ejercicio 4
?min_rank()

air_t <- select(comparacion2, atraso_salida)
air_t
min_rank(desc(air_t))

# [1] 114150 103893 114150 144947 258934 209494 234113 185276 185276 163760
# estos son los vuelos que mas se han tardado en salir

#Ejercicio 5
1:6 + 1:20

#Esto genera un vector de 20 observaciones que se suman con un vector de extension 6

#Ejercicio 6
Usage
cos(x)
sin(x)
tan(x)

acos(x)
asin(x)
atan(x)
atan2(y, x)

cospi(x)
sinpi(x)
tanpi(x)
Arguments
x, y	
numeric or complex vectors.

#--------------------- FUNCION SUMMARIZE ------------------------------------------------#

?summarise
summarise(flights, delay = mean(dep_delay, na.rm = T))

by_month_group <- group_by(flights, year, month)
summarise(by_month_group, delay= mean(dep_delay,na.rm = T))

by_day_group <- group_by(flights, year, month, day)
summarise(by_day_group, delay = mean(dep_delay, na.rm = T),
          median = median(dep_delay, na.rm = T),
          min = min(dep_delay, na.rm = T)
          )

summarize(group_by(flights, carrier),
          delay = mean(dep_delay, na.rm = T))

mutate(summarize(group_by(flights, carrier),
                    delay = mean(dep_delay, na.rm = T)),
                    sorted = min_rank(delay)        
          )

## PIPES

group_by_dest <- group_by(flights, dest)
delay <- summarise(group_by_dest,
                   count = n(),
                   dist = mean(distance, na.rm = T),
                   delay = mean(arr_delay, na.rm = T)
                   )
view(delay[1:50,])

filter(delay, count > 100, dest != "HNL")

ggplot(data = delay, mapping = aes(x=dist, y=delay)) +
  geom_point(aes(size = count), alpha = 0.2) +
  geom_smooth() +
  geom_text(aes(label = dest))
          
ggplot(data = delay, mapping = aes(x=dist, y=delay)) +
  geom_point(aes(size = count), alpha = 0.2) +
  geom_smooth(se = F) +
  geom_text(aes(label = dest), alpha = 0.3)

new_delay <- flights %>%
  group_by(dest) %>%
  summarise(
    count = n(),
    dist = mean(distance, na.rm = T),
    delay = mean(arr_delay, na.rm = T)
  ) %>%
  filter(count > 100, dest!= "HNL")

# x %>% f(y) <-> f(x,y)
# x %>% f(y) %>% g(z) <-> g(f(x,y),z)
# x %>% f(y) %>% g(z) %>% h(t) .................

#Eliminar los NA

flights %>% 
  group_by(year, month, day) %>% 
  summarise(mean = mean(dep_delay, na.rm = T),
            median = median(dep_delay, na.rm = T),
            sd = sd(dep_delay, na.rm = T),
            count = n()
            )

not_cancelled <- flights %>% 
  filter(!is.na(dep_delay),!is.na(arr_delay))

not_cancelled %>% 
  group_by(year, month, day) %>% 
  summarise(mean = mean(dep_delay, na.rm = T),
            median = median(dep_delay, na.rm = T),
            sd = sd(dep_delay, na.rm = T),
            count = n()
  )

## CONTAR Y VISUALIZAR RESUMENES CORRECTAMENTE

delay_numtail <- not_cancelled %>% 
  group_by(tailnum) %>% 
  summarise(delay = mean(arr_delay))

ggplot(data = delay_numtail, mapping = aes(x = delay))+
  geom_freqpoly(binwidth = 5)

ggplot(data = delay_numtail, mapping = aes(x = delay))+
  geom_histogram(binwidth = 5)

delay_numtail <- not_cancelled %>% 
  group_by(tailnum) %>% 
  summarise(delay = mean(arr_delay),
            count = n()
            )

ggplot(data = delay_numtail, mapping = aes(x = count, y = delay))+
  geom_point(alpha = 0.2)

delay_numtail %>% 
  filter(count>30) %>% 
  ggplot(mapping = aes(x = count, y = delay)) +
  geom_point(alpha = 0.2)

## EJEMPLO DEL BEISBOL

view(Lahman::Batting)
?Lahman::Batting

batting <- as_tibble(Lahman::Batting)

batters <- batting %>% 
  group_by(playerID) %>% 
  summarise(hits = sum(H, na.rm = T),
            bats = sum(AB, na.rm = T),
            bat.average = hits / bats
            )

batters %>% 
  filter(bats > 50) %>% 
  ggplot(mapping = aes(x = bats, y= bat.average))+
  geom_point(alpha = 0.2) +
  geom_smooth()
  
batters %>% 
  filter(bats > 100) %>% 
  ggplot(mapping = aes(x = bats, y= bat.average))+
  geom_point(alpha = 0.2) +
  geom_smooth(se = F)  
  
batters %>% 
  arrange(desc(bat.average))
  
batters %>% 
  filter(bats>100) %>% 
  arrange(desc(bat.average))
  
## Medidas de Centralizacion

not_cancelled %>% 
  group_by(carrier) %>% 
  summarise(
    mean= mean(arr_delay),
    mean2 = mean(arr_delay[arr_delay>0]),
    median = median(arr_delay)
  )

## medidas de dispersion

not_cancelled %>% 
  group_by(carrier) %>% 
  summarise(
    sd = sd(arr_delay),
    iqr = IQR(arr_delay),
    mad = mad(arr_delay)
  ) %>% 
  arrange(desc(sd))

## medidas de Orden

not_cancelled %>% 
  group_by(carrier) %>% 
  summarise(
    first = min(arr_delay),
    q1 = quantile(arr_delay, 0.25),
    median = quantile(arr_delay,0.5),
    q3 = quantile(arr_delay,0.75),
    last = max(arr_delay)
  )

## MEDIDAS DE POSICION

not_cancelled %>% 
  group_by(carrier) %>% 
  summarise(
    first_dep = first(dep_time),
    second_dep = nth(dep_time, 2),
    third_dep = nth(dep_time, 3),
    last_dep = last(dep_time)
  )

not_cancelled %>% 
  group_by(carrier) %>% 
  mutate(rank = min_rank(desc(dep_time))) %>% 
  filter(rank %in% range(rank)) -> temp

not_cancelled %>% 
  group_by(carrier) %>% 
  mutate(rank = min_rank((dep_time))) %>% 
  filter(rank %in% range(rank)) -> temp

view(temp)

##FUnciones de conteo

not_cancelled %>% 
  group_by(dest) %>% 
  summarise(
    count = n(),
    carriers = n_distinct(carrier),
    arrivals = sum(!is.na(arr_time))
  ) %>% 
  arrange(desc(carriers))

flights %>% 
  group_by(dest) %>% 
  summarise(
    count = n(),
    carriers = n_distinct(carrier),
    arrivals = sum(!is.na(arr_delay))
  ) %>% 
  arrange(desc(carriers))

not_cancelled %>% count(dest)

not_cancelled %>% count(tailnum, wt = distance)

## sum /mean de valores logicos
not_cancelled %>% 
  group_by(year, month, day) %>% 
  summarise(n_prior_5 = sum(dep_time < 500) )

not_cancelled %>% 
  group_by(year, month, day) %>% 
  summarise(more_than_hour_delay = mean(arr_delay > 60))

not_cancelled %>% 
  group_by(carrier) %>% 
  summarise(more_than_hour_delay = mean(arr_delay > 60)) %>% 
  arrange(desc(more_than_hour_delay))

## AGRUPACIONES MULTIPLES

daily <- group_by(flights, year, month, day)
(per_day <- summarise(daily, n_fl = n()))
(per_month <- summarise(per_day, n_fl = sum(n_fl)))
(per_year <- summarise(per_month, n_fl = sum(n_fl)))

business <- group_by(flights, carrier, dest, origin)
(detail <- summarise(business, n_fl = n())) %>% 
  summarise(n_fl = sum(n_fl)) %>% 
  summarise(n_fl = sum(n_fl))

daily %>% 
  ungroup() %>% 
  summarise(n_fl = n())

business %>% 
  ungroup() %>% 
  summarise(n_fl = n())

business <- group_by(flights, carrier, dest, origin)
(detail <- summarise(business, n_fl = n())) %>% 
  summarise(n_fl = sum(n_fl)) %>% 
  summarise(n_fl = sum(n_fl)) %>% 
  ungroup() %>% 
  summarise(n_fl = sum(n_fl))

##Mutate and filters por segmento

flights %>% 
  group_by(year, month, day) %>% 
  filter(rank(desc(arr_delay))< 10) -> temp
view(temp)

popular_dest <- flights %>% 
  group_by(dest) %>% 
  filter(n()>365)
view(popular_dest)

popular_dest %>% 
  filter(arr_delay > 0) %>% 
  mutate(prop_delay = arr_delay / sum(arr_delay)) %>% 
  select(year:day, dest, arr_delay, prop_delay)

#--------------------- EXAMEN 1 ---------------------------------------#

#EJERCICIO 1

?flights
view(head(flights))
?summarise
#Lo primero que vamos a hacer es construir un data frame con las variables de interes

vuelos <- select(flights,
                    year:day,
                    dep_delay:air_time)

vuelos %>% 
  group_by(carrier) %>% 
  summarise(
    mean= mean(dep_delay, na.rm = T),
    median = median(dep_delay, na.rm = T),
    sd = sd(dep_delay, na.rm = T),
    menor = min(dep_delay, na.rm = T),
    mayor = max(dep_delay, na.rm = T),
    quintiles = quantile(dep_delay, 0.95, na.rm = T)
  ) -> vuelos.por.company

vuelos %>% 
  group_by(dest) %>% 
  summarise(
    mean= mean(dep_delay, na.rm = T),
    median = median(dep_delay, na.rm = T),
    sd = sd(dep_delay, na.rm = T),
    menor = min(dep_delay, na.rm = T),
    mayor = max(dep_delay, na.rm = T),
    quintiles = quantile(dep_delay, 0.95, na.rm = T)
  ) -> vuelos.por.destino 

view(vuelos.por.company)
view(vuelos.por.destino)

#En promedio la compañia que mayor retraso tiene en sus vuelos es F9 con 20 min en promedio
#y la compañia que menor tiempo de retraso en promedio tiene es US con 3.9 min promedio

# la compañia que logro los vuelos con menor antelacion fue B6 con vuelos con antelacion
# de 43 min.

# HA, MQ y AA fueron las empresas que mayores retrasos tuvieron en sus vuelos con tiempos
# superiores a los 1000 min.

# El 50% de los vuelos tiene tiempos de retrasos entre un intervalo de -6 y 1 min
# el 95% de los vuelos tiene tiempos de retraso los 27 y 1000 minutos

# Existen 5 destino que poseen los mayores tiempos de retraso en el 95% de la campana de gauss
#  son HNL, CMH, ORD, SFO, SVG estos vuelos poseen retrasos de mas de 150 minutos.

#EJERCICIO 2
not_cancelled <- flights %>% 
  filter(!is.na(dep_delay),!is.na(arr_delay))

not_cancelled %>% count(dest)

not_cancelled %>% count(tailnum, wt = distance)

aggregate(cbind(count = dest) ~ dest, 
          data = not_cancelled, 
          FUN = function(x){NROW(x)})

aggregate(cbind(count = distance) ~ tailnum, 
          data = not_cancelled, 
          FUN = function(x){sum(x)})

#esto lo hice sin el paquete dyplr pero hay formas mas facil de hacerlo con dyplr

#EJERCICIO 3

(is.na(dep_delay) | is.na(arr_delay))

cancelados <- flights %>% 
  filter(is.na(dep_delay))
view(cancelados)

cancelados2 <- flights %>% 
  filter(is.na(air_time))
view(cancelados2)

#la columna mas importante en este caso es la columna de tiempo de vuelo;

#Ejercicio 4

#Investiga si la proporción de vuelos cancelados está relacionada con el retraso 
#promedio por día en los vuelos.

v_cancel <- flights %>% 
  filter(is.na(air_time)) %>% 
  group_by(time_hour) %>% 
  summarise(cantidad = n())
ggplot(data = v_cancel) +
  geom_point(mapping = aes(x = time_hour, y = cantidad), color = "blue") 
  
#Existe una patron de vuelos cancelados entre las fechas finales e iniciales del a�o
#esto puede deberse a las adversidades climaticas del invierno.

#Investiga si la proporción de vuelos cancelados está relacionada con el retraso 
#promedio por aeropuerto en los vuelos.

cancel.delay <- flights %>% 
  group_by(year, month, day) %>% 
  summarise(air_time, 
            total_day = n(),
            dep_delay_day = sum(dep_delay)) %>% 
  filter(is.na(air_time)) %>% 
  summarise(total_day, total_cancelled_day = n()) %>% 
  mutate(prop_day_cancelled = total_cancelled_day/total_day)

cancel.delay2 <- flights %>% 
  group_by(year, month, day) %>% 
  summarise(dep_delay, air_time, total_day = n()) %>% 
  filter(is.na(air_time)) %>% 
  summarise(total_delay = sum(dep_delay, na.rm = T),
            total_day,
            total_cancelled_day = n()) %>% 
  mutate(prop_day_cancelled = total_cancelled_day/total_day)


ggplot(data = cancel.delay2, mapping = aes(x = total_delay, y=prop_day_cancelled)) + 
  geom_smooth()

#Existe una relacion entre el incremento del retraso total de los vuelos con la proporcion
#de vuelos que son cancelados.

#¿Qué compañía aérea sufre los peores retrasos?

peor_retraso_compa�ia <- flights %>% 
  filter(!is.na(air_time)) %>% 
  group_by(carrier) %>% 
  summarise(retraso = sum(dep_delay, na.rm = T))
view(peor_retraso_compa�ia)

#las compañias que sufren los peores retrasos por cancelacion son UA, B6 y EV
#estas compañias tienen retrasos superiores a los 

#Ejercicio 5

flights %>% 
  group_by(carrier, dest) %>% 
  summarise(
    n = n(),
    retraso = sum(dep_delay, na.rm = T)
  ) %>% 
  arrange(retraso) %>% 
  view

#los tiempos de retraso tienden a incrementar si existe una combinacion de una de las peores
#aerolineas y si hay malos aeropuertos.

#EJercicio 6







