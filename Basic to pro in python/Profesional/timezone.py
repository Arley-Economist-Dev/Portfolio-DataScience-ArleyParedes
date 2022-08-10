from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime('%d/%m/%Y, %H: %M: %S'))

managua_timezone = pytz.timezone("America/Managua")
managua_date = datetime.now(managua_timezone)
print("Managua: ", managua_date.strftime('%d/%m/%Y, %H: %M: %S'))

madrid_timezone = pytz.timezone("Europe/Madrid")
madrid_date = datetime.now(madrid_timezone)
print("Madrid: ", madrid_date.strftime('%d/%m/%Y, %H: %M: %S'))