import psycopg2
from bd import conexion
try:
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, edad FROM mascotas;")
        mascota = cursor.fetchone()
        while mascota:
            print(mascota)
            mascota = cursor.fetchone()
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()