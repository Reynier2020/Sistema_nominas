import sys
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
cursor = conn.cursor()
k = "SI"
while k.upper() == "SI":
    pid = int(input("id: "))
    pnombre = input("nombre: ")
    pcantid = int(input("cantidad: "))
    precio = float(input("precio: "))
    try:
        cursor.execute("""
        insert into productos(id, nombre, cantidad, precio)
        values(%d, '%s', %d, %f)
        """ % (pid, pnombre, pcantid, precio))
        conn.commit()
        k = input("quieres insertar mas producto? si/no : ")
    except:
        conn.rollback()
        sys.exit(1)
cursor.close()
conn.close()
