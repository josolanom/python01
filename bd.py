import psycopg2
import json
with open ("pass.json") as archivo_permisos: #pass.json archivo con los permisos
	permisos = json.load(archivo_permisos) # leo los permisos
try:
	conexion = psycopg2.connect(**permisos) # uso los permisos (**indiga que vienen argumentos con nombres) para conectarme y creo conexion
except psycopg2.Error as e:
	print ("Error al conectar a la BD",e)
else:
	print("Conectado a BD, OK")