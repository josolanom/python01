#25-07-19 9:16 V1.0.0
#insertar en modo txt
#

import psycopg2 
from bd import conexion #importo los datos de la conexion

cod_cliente  = input("Codigo Cliente: ")
nom_cliente  = input("Nombre Cliente: ")
cl_direccion = input("Direccion: ")
cl_telefono  = input("Telefono: ")

try:
    with conexion.cursor() as cursor:
        consulta = "INSERT INTO t_cliente (cod_cliente,nom_cliente,cl_direccion,cl_telefono) VALUES (%s,%s,%s,%s);" #cosnulta sql a realizar
        cursor.execute(consulta, (cod_cliente,nom_cliente,cl_direccion,cl_telefono)) #ejecuto la consulta con los valores de las variables
    conexion.commit()  #confirmo la operacion
except psycopg2.Error as e:
    print("Ocurrió un error al insertar: ", e)
else:
    print("Insertado correctamente") 
finally:
    conexion.close()
