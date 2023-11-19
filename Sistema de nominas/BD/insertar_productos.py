import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
cursor = conn.cursor()

cursor.execute("""
insert into productos(id, nombre, cantidad, precio)
values(101, 'camara', 100, 15)
""")

print("una fila insertada en la tabla productos")
cursor.close()
conn.commit()
conn.close()
