import psycopg2
from bd import conexion

num = input("Escriba el ID")

try:
    with conexion.cursor() as cursor:
        consulta_sql = ("SELECT id, nombre, edad FROM mascotas where ID = %s;")
        cursor.execute (consulta_sql,(num,))
        mascota = cursor.fetchone()
        while mascota:
            print(mascota)
            mascota = cursor.fetchone()
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()