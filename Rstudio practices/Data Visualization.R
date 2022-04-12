"Primera clase"
"Arley Paredes Espinoza"
#8 de diciembre 2021

library(tidyverse)
#  v ggplot2 3.3.5     v purrr   0.3.4
#v tibble  3.1.5     v dplyr   1.0.7
#v tidyr   1.1.4     v stringr 1.4.0
#v readr   2.0.2     v forcats 0.5.1

#¿Los coches de motor mas grande consumen mas o menos gas?
#¿hay relacion lineal entre consumo y tamaño? o ¿no lineal? ¿es exponencial?
#Es positivo? Es negativo?

view(mpg)
help(mpg)
?mpg
#displ es el tamaño del motor del coche en litros
#hwy son las millas por galon de gasolina

?ggplot

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y= hwy)) #grafico de dispersion/ Scatterplot

"ggplot(data = dataframe) +
  geom_funtions(mapping = aes(x = variable1, y= variable2))"

"<::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::>"

#Tarea 1
ggplot(data = mpg)
#no se muestra nada en la ventana de plots

?mpg
"el dataframe tiene 234 observaciones, es decir, la informacion de 234 automoviles
el numero de columnas del data frame es de 11 lo que significa 11 variables."

view(mpg)
"la variable drv es una variable cualitativa nominal que categoriza con f 
a los front-wheel drive, con r a los rear wheel drive, y con 4 a los 4wd"

ggplot(data = mpg) +
  geom_point(mapping = aes(x = hwy, y= cyl))
"se observa la dispersion de los datos frente a otro, donde a mayor numero de 
cilindros menor es la cantidad de millas recorridas por galon"

ggplot(data = mpg) +
  geom_point(mapping = aes(x = cty, y= cyl))
"Los datos muestran una relacion inversa en la que entre mas cilindros posee el
automovil menos millas de ciudad por galon realiza"

ggplot(data = mpg) +
  geom_point(mapping = aes(x = class, y= drv))
"se observa un grafico que muestra la relacion entre la clase y el tipo de tren
de conduccion del vehiculo, esto no presenta informacion relevante pues no
son variables cuantitativas que puedan mostrar el total de la distribuccion de estos datos"

"<::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::>"

"cambiando la forma de los esteticos del grafico"

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, color = class))
"Este grafico permite ver un diagrama de dispersion colorido segun la clase a 
la que pertenece el automovil"

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, size = class))
#Tamaño de los puntos segun la clase, pero es mejor si es numerico

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, alpha = class))
#Alpha sirve para modificar la transparencia de los puntos

ggplot(data = mpg) + 
  geom_point(mapping = aes(x = displ, y = hwy, shape = class))
#shape sirve para modificar la forma de los puntos segun clase

#Eleccion manual de estetica
ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy), color = "red")

#Color = nombre del color en formato string
#Size = tamaño del punto en mm
#shape = forma del punto con numeros del 0 al 24

#todas las formas de shape
d=data.frame(p=c(0:25,32:127))
ggplot() +
  scale_y_continuous(name="") +
  scale_x_continuous(name="") +
  scale_shape_identity() +
  geom_point(data=d, mapping=aes(x=p%%16, y=p%/%16, shape=p), size=5, fill="red") +
  geom_text(data=d, mapping=aes(x=p%%16, y=p%/%16+0.25, label=p), size=3)


#Generando un grafico de dispersion personalizado
ggplot(data = mpg) +
  geom_point(mapping = aes(x= displ, y = hwy),
             color = "red", fill = "yellow", shape = 23, size = 5)

#<------------------------------------------------------------------------------>
#Tarea 2

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy), color = "green")

#Variables que son Categoricas y otras que son Continuas
?mpg

#manufacturer es categorica
#model es categorica
#trans es categorica
#drv es categorica
#fl es categorica
#class es categorica

#hwy es continua
#cty es continua
#cyl es continua
#year es continua
#displ es continua

ggplot(data = mpg) +
  geom_point(mapping = aes(x = hwy, y= cty),
             color = "black", size = 3, shape = 22, fill= "red")

ggplot(data = mpg) +
  geom_point(mapping = aes(x = hwy, y= cty),
             color = "black", size = 3, shape = 22, fill= "red", stroke = 2)

ggplot(data = mpg) +
  geom_point(mapping = aes(x = hwy, y= hwy),
             color = "black", size = 3, shape = 22, fill= "red", stroke = 2)

ggplot(data = mpg) +
  geom_point(mapping = aes(color = displ < 4))

#<----------------------------------------------------------------------------->
#Seccion 3 - errores de R

ggplot(data = mpg) +
  geom_point(mapping = aes(x= displ, y = hwy ,color = displ < 4))

#FACETS
# facet_wraps(~<FORMULA_VARIABLE>): la variable debe ser discreta
ggplot(data = mpg) +
  geom_point(mapping = aes(x= displ, y = hwy))+
  facet_wrap(~class, nrow = 3)

#facet_grid(<FORMULA_VARIABLE1>~<FORMULA_VARIABLE>)
ggplot(data = mpg) +
  geom_point(mapping = aes(x= displ, y = hwy))+
  facet_grid(drv~cyl)

ggplot(data = mpg) +
  geom_point(mapping = aes(x= displ, y = hwy))+
  facet_grid(.~cyl)

#<----------------------------------------------------------------------------->
#Tarea 3 

#¿Qué ocurre si hacemos un facet de una variable contínua?
"lo que ocurre es que se crea un grafico donde se segmentan las distribuciones
de acuerdo a las categorias que se esten analizando."

#¿Qué significa si alguna celda queda vacía en el gráfico facet_grid(drv~cyl)?
"esto significa que no existen observaciones en el dataframe que nos muestre el
conjunto de datos que tengan relaciones entre los numeros de cilindros y la clase
de tren de conduccion"

#¿Qué relación guardan esos huecos vacíos con el gráfico siguiente?
ggplot(data = mpg) +
  geom_point(mapping = aes(x=drv, y = cyl)) 

"los espacios en blanco concuerdan con los mismos espacios que no se muestran con
puntos dentro del grafico anterior, pues se comparan las mismas variables de clase
que en el grafico con faced_grid"

#¿Qué gráficos generan las siguientes dos instrucciones? 
#¿Qué hace el punto? ¿Qué diferencias hay de escribir 
#la variable antes o después de la virgula?

ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y = hwy)) +
  facet_grid(.~cyl)
"el primer grafico muestra las millas de autopistas recorridas en relacion con
el cilindraje del motor y la clasificacion de los cilindros que tiene el auto"

ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y = hwy)) +
  facet_grid(drv~.)
"el segundo grafico muestra el cilindraje del motor en relacion con las millas 
recorridas en autopista; clasificada segun el tipo de tren de conduccion,
el efecto que tiene poner el punto antes a la izquierda o derecha es la
orientacion del grafico en pantalla."

#El primer facet que hemos pintado era el siguiente:

ggplot(data = mpg) +
  geom_point(mapping = aes(x = displ, y = hwy)) +
  facet_wrap(~class, nrow = 3)

#¿Qué ventajas crees que tiene usar facets en lugar de la estética del color? 
#¿Qué desventajas? 
#¿Qué cambiaría si tu dataset fuera mucho más grande?

"Usar facets puede permitirnos visualizar la data de forma segmentada en un solo
grafico, tiene como desventajas que podemos perder de vista la distribucion
general de las data con respecto a la homocedasticidad de la misma; si el data
set fuera mas grande y tuviera mas categorias el grafico se sobrecargaria."

?facet_wrap

#¿Qué hace el parámetro nrow?
"Este parametro permite poner el numero de filas que se quiere en el grafico"
#¿Y el parámetro ncol?
"este parametro permite poner el numero de columnas que se quiere en el grafico"
#¿Qué otras opciones sirven para controlar el layout de los paneles individuales?
"Se pueden utilizar las opciones scales, shrink, labeller, as.table, switch, drop
dir y strip.position"
#¿Por qué facet_grid() no tiene los parámetros de nrow ni de ncol?
"faced_grid posee parametros para ajustar las rows y cols, no posee los mismo nombres
para compatibilizar las funciones dentro del paquete"
#Razona la siguiente afirmación:
#Cuando representemos un facet con facet_grid() conviene poner la variable con 
#más niveles únicos en las columnas.
"Es mas conveniente pues se puede dividir el grafico considerando las categorias
de las variables que pueden ser categoricas relacionadas a otra variable que pueda ser discreta"

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

#diferentes geometrias
ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y= hwy))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x= displ, y= hwy))

ggplot(data = mpg) +
  geom_smooth(mapping = aes(x= displ, y= hwy, linetype= drv))

ggplot(data = mpg) +
  geom_point(mapping = aes(x=displ, y= hwy, color=drv)) +
  geom_smooth(mapping = aes(x= displ, y= hwy, linetype= drv, color = drv))

#Combinacion de graficos
ggplot(data = mpg)+
  geom_smooth(mapping = aes(x=displ, y=hwy))

ggplot(data = mpg)+
  geom_smooth(mapping = aes(x=displ, y=hwy, group = drv))

ggplot(data = mpg)+
  geom_smooth(mapping = aes(x=displ, y=hwy, color = drv),
  show.legend = TRUE)

ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) +
  geom_point() +
  geom_smooth()

ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) +
  geom_point(mapping = aes(color = class)) +
  geom_smooth(mapping = aes(color = drv))

ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) +
  geom_point(mapping = aes(color = class)) +
  geom_smooth(data = filter(mpg, class == "suv"), se = F)

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

#Primera pregunta
Se crea un grafico de dispersion con lineas de tendencia clasificando los datos
de acuerdo las categorias de conduccion

#segunda pregunta
show_legend es una opcion que nos permite mostrar o no la clasificacion de los 
datos en dependencia de las variables utilizadas para clasificar, si se mantiene 
en FALSE la leyenda no se muestra, si se quita las leyenda se mostraran

#tercera pregunta
geom_smooth ayuda a visualizar datos en presencia de sobresaturacion de 
informacion en los graficos, mostrando diferencias y colores en dependencia de las categorias.
si no existe sobresaturacion de la visualizacion lo quitaria.

#cuarta pregunta
Los dos codigos generan un grafico de dispersion con linea de tendencia y su region critica
la diferencia esta en como se especifican los mappings, uno siendo de forma global y otro de forma critica

#quinta pregunta
ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) + 
  geom_point() + 
  geom_smooth( se = F)

#sexta pregunta
ggplot(data = mpg,mapping = aes(x=displ, y=hwy))+
  geom_point() +
  geom_smooth(mapping = aes(group = drv), se = F)

#septima pregunta
ggplot(data = mpg,mapping = aes(x=displ, y=hwy))+
  geom_point(mapping = aes(color = drv)) +
  geom_smooth(mapping = aes(group = drv, color = drv), se = F)

#octava pregunta
ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) + 
  geom_point(mapping = aes(shape = drv, color = drv)) + 
  geom_smooth(se = F)

#novena pregunta
ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) + 
  geom_point(mapping = aes(shape = drv, color = drv)) + 
  geom_smooth(mapping = aes(linetype= drv), se = F)

#decima pregunta
ggplot(data = mpg, mapping = aes(x=displ, y = hwy)) + 
  geom_point(aes(shape = drv, color = drv, fill = drv), color = "white", size = 3, 
             shape = 23, stroke = 2)

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

#transformaciones estadisticas comunes

view(diamonds)
#grafico de barra

?geom_bar

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut))

ggplot(data = diamonds) +
  stat_count(mapping = aes(x = cut))

demo.diamonds <- tribble(
  ~cut,    ~freqs,
  "fair",  1610,
  "good",  4906,
  "very good", 12082,
  "premium", 13791,
  "ideal", 21551
)

view(demo.diamonds)

ggplot(data = demo.diamonds) +
  geom_bar(mapping = aes(x = cut, y = freqs), stat = "identity")

ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = cut, y = ..prop.., group = 1))

ggplot(data = diamonds) +
  stat_summary(
    mapping = aes(x = cut, y= depth),
    fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )

ggplot(data = diamonds) +
  stat_summary(
    mapping = aes(x = cut, y= price),
    fun.ymin = min,
    fun.ymax = max,
    fun.y = median
  )

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

#ejercicio 1
Ambas funciones son utiles para generar graficos de barra, geom_col se diferencia
porque representa las alturas de las barras como valores en los datos
geom_bar usa stat_count y geom_col usa stat_identity()

#ejercicio 2
Los stats son funciones que realizan las mismas funciones de las funciones ggplot

#ejercicio 3
La variables stat_smooth es un alias de la geometria smooth, esta funcion nos sirve
para visualizar datos que estan sobresaturados, los parametros que controlan su comportamiento
son y o x, ymin o xmin, ymax o xmax, se para el error estandar.

#ejercicio 4
ggplot(data = diamonds)+
  geom_bar(mapping = aes(x = cut, y = ..prop..))

?geom_bar

#ejercicio 5
ggplot(data = diamonds) + 
  geom_bar(mapping = aes(x = cut, y = ..prop.., group = 1))

ggplot(data = diamonds) + 
  geom_bar(mapping = aes(x = cut, y = ..prop.., fill = color)) 

Los problemas que tienen estos graficos es que no se muestran las escalas del eje y
acorde a la proporciones que se generan con los datos obtenidos.

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, colour = cut))


ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = cut))


ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = clarity))


ggplot(data = diamonds) +
  geom_bar(mapping = aes(x = cut, fill = color))

## position = "identity"

ggplot(data = diamonds, mapping = aes(x = cut,colour = clarity)) +
  geom_bar(fill = NA, position = "identity")

## position = "Fill" para comparar proporciones

ggplot(data = diamonds, mapping = aes(x = cut,fill = clarity)) +
  geom_bar(position = "fill")

## position = "dodge" para ver que categoria es mejor
ggplot(data = diamonds, mapping = aes(x=cut, fill=clarity))+
  geom_bar(position="dodge")

#volvemos al scatterplot
#position = "jitter"
ggplot(data = mpg, mapping = aes(x = displ, y= hwy)) +
  geom_point(position = "jitter")

ggplot(data = mpg, mapping = aes(x = displ, y= hwy)) +
  geom_jitter()

#Sistemas de coordenadas

#cood_flip() -> cambia llos papeles de x e y
ggplot(data = mpg, mapping = aes(x=class, y=hwy))+
  geom_boxplot()+
  coord_flip()

#coord__quickmap() -> configurar el aspect ratio para mapas

usa <- map_data("usa")
ggplot(usa, aes(long, lat, group = group)) +
  geom_polygon(fill = "blue", color = "red") +
  coord_quickmap()

italy <- map_data("italy")
ggplot(italy, aes(long, lat, group = group)) +
  geom_polygon(fill = "blue", color = "red") +
  coord_quickmap()

#coord_polar()

ggplot(data = diamonds) +
  geom_bar(
    mapping = aes(x = cut, fill = cut),
    show.legend = F,
    width = 1
  ) +
  theme(aspect.ratio = 1)+
  labs(x = NULL, y = NULL) +
  coord_polar()

#Gramatica por capas para ggplot2

# ggplot(data = DATA FRAME) +
#   GEOM_FUNCTION(
#                 mapping = aes(mappings),
#                 stat= STATS,
#                 position = positions,
#               ) +
#   COORDINATE_FUNCTION() +
#   FACET_FUNCTION()

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=clarity,fill=clarity,y=..count..))+
  coord_polar()+
  facet_wrap(~cut)+
  labs(x=NULL, y=NULL,title="Ejemplo final seccion 3 del curso",
       caption = "dos variables cruzadas de diamonds", subtitle = "aprender ggplot")

#<----------------------------------------------------------------------------->
#<----------------------------------------------------------------------------->

#Ejercicio 1

ggplot(data = mpg, mapping = aes(x = cty, y = hwy, color = class )) + 
  geom_point(position = "jitter")+
  labs(,title = "Dispercion de datos", subtitule = "clase de vehiculo",
       caption = "fuente R studio")
  
#Ejercicio 2

Dentro del comando geom_jitter se pueden identificar como parametro para ver
la cantidad de dispersion en el grafico son width y height los cuales modifican
la altura y anchura dentro de la dispersion de los graficos con jitter

#Ejercicio 3
?geom_count
?geom_jitter

Geom count se utiliza para contar el numero de observacion en cada localizacion
el grafico cuenta los puntos en el area, es util cuando tiene una variable discreta
y esta sobrerepresentada, en cambio el jitter añade ruido a los graficos de dispercion
para ver la cantidad real de puntos, usan los mismos argumentos y parametros a excepcion
de el ancho y el alto de jitter.

#Ejercicio 4

¿Cual es el valor por defecto del parámetro position de un geom_boxplot? 

La posicion de un boxplot por defecto es la de un indicador vertical, que puede
ser modificado por el argumento position para ajustarlo.
  
ggplot(data = diamonds, mapping = aes(x= cut, y= price)) +
  geom_boxplot(position = )

#Ejercicio 5

#Grafico de tarta para grafico de apilado
ggplot(data = diamonds, mapping = aes(x = cut,fill = clarity)) +
  geom_bar(position = "fill") +
  coord_polar()

#Ejercicio 6
El argumento labs sirve para agregar etiquetas, titulos, subtitulos o anotaciones
para agregar al grafico.

#Ejercicio 7
?coord_map
?coord_quickmap

coord_map es una funcion que proporciona una imagen 2D detallada de la
cartografia esferica de la tierra, el quickmap da una aproximacion mas rapida, 
mucho menos detallada de areas mas pequeñas cercanas al ecuador.

#Ejercicio 8
?coord_fixed

p <- ggplot(mtcars, aes(mpg, wt)) + geom_point()
p + coord_fixed(ratio = 1)
p + coord_fixed(ratio = 5)
p + coord_fixed(ratio = 1/5)
p + coord_fixed(xlim = c(15, 30))

Un sistema de coordenadas de escala fija fuerza una relación específica entre 
la representación física de las unidades de datos en los ejes.

#Ejercicio 9

esta añade lineas de referencias al grafico, pueden ser horizontal, vertical o
diagonales.

geom_vline(): xintercept

geom_hline(): yintercept

geom_abline(): slope and intercept

#Ejercicio 10
ggplot(data = mpg, mapping = aes(x = cty, y = hwy )) + 
  geom_point() + 
  geom_abline() + 
  coord_fixed()

El grafico nos indica una relacion directa entre la distancia que recorre un vehiculo en la
ciudad y una autopista; asi pues podemos ver que en una autopista se recorren muchas mas millas
que en la ciudad.

?stat_summary
