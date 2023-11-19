import sys
import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", base_datos="sistema_nominas")
cursor = conn.cursor()

try:
    cursor.execute("""
    create table productos( id smallint not null,
    nombre char(50),
    cantidad smallint,
    precio float)
    """)
except MySQLdb.Error:
    print("error al crear la tabla")
    sys.exit(1)
cursor.close()
conn.close()
