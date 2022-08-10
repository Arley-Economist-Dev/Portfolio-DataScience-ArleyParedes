import datetime

#imprimir la hora exacta del dia de hoy
my_time = datetime.datetime.now()
my_time_utc = datetime.datetime.utcnow()

print(my_time)
print(my_time_utc)

#para conocer la fecha del dia de hoy
my_day = datetime.date.today()
print(my_day)
print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

#EJEMPLOS
from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'formato LATAM: {my_str}')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'formato USA: {my_str}')

my_str = my_datetime.strftime('Estamos en el año %Y')
print(f'Formato random: {my_str}')