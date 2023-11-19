import sys
import MySQLdb

try:
    conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
except MySQLdb.Error:
    print("error al conectar con la bd")
    sys.exit(1)
cursor = conn.cursor()
try:
    cursor.execute("""
    insert into productos(id, nombre, cantidad, precio)
    values(101, 'camara', 100, 15)
    """)
    conn.commit()
    print("una fila insertada en la tabla productos")
except MySQLdb.Error:
    conn.rollback()
cursor.close()
conn.close()
