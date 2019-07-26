import psycopg2 
from bd import conexion
try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO mascotas(nombre, edad) VALUES (%s, %s);"
        cursor.execute(consulta, ("Maggie", 19))
        cursor.execute(consulta, ("Capuchina", 19))
        cursor.execute(consulta, ("Guayaba", 19))
        cursor.execute(consulta, ("Panqué", 19))
        cursor.execute(consulta, ("Snowball", 19))
    conexion.commit()  

except psycopg2.Error as e:
    print("Ocurrió un error al insertar: ", e)
else:
    print("Insertado sin error") 
finally:
    conexion.close()
