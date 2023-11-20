import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
cursor = conn.cursor()
k = "SI"
while k.upper() == "SI":
    p = int(input("escribe un id: "))
    cursor.execute("""
        select * from productos where id = %d
    """ % p)
    row = cursor.fetchone()
    if row is None:
        print("no hay datos en el id %d" % p)
    else:
        print("el producto con id %d es la siguiente:" % p)
        print("id: %d, nombre: %s, cantidad: %d, precio: %f" % (row[0], row[1], row[2], row[3]))
        k = input("desea seguir buscando? si/no: ")
cursor.close()
conn.close()
