# Trabajar con fechas y horas en python

from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
#Obtener fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

#Crear una fecha y hora especifica
specific_date = datetime(2025,1,24,2,30)
print(f"Fecha y hora especifica: {specific_date}")

#Formatear fechas
#metodo strftime()

format_date = now.strftime("%A %d/%m/%Y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

#4. Operaciones con fechas

yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer fue: {yesterday}")

tomorrow = datetime.now() + timedelta(days=0.5)
print(f"Mañana será: {tomorrow}")

twelve_hours = datetime.now() + timedelta(hours=12)
print(f"En 12 horas sera: {twelve_hours}")

year = now.year
print(f"Estas en el año {year}")

month = now.month
print(f"Y en el mes {month}")

date1 = datetime.now()
date2 = datetime(2027,1,24)
diferencia = date2 - date1
print(f"Para tu cumple quedan: {diferencia}")