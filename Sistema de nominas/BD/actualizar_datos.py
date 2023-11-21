import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
cursor = conn.cursor()
k = "SI"
p = int(input("escriba una ID: "))
cursor.execute("""
select * from productos where id = %d
""" % p)
row = cursor.fetchone()
while k.upper() == "SI":
    if row is None:
        print("no se han encontrado datos asignados al id %d" % p)
    else:
        print("los datos del id %d son los siguientes" % p)
        print("nombre: %s, cantidad: %d, precio: %f" % (row[1], row[2], row[3]))
        new_nombre = input("escribe un nuevo nombre: ")
        ncantid = int(input("nueva cantidad; "))
        n_precio = float(input("nuevo precio: "))
        cursor.execute("""
        update productos set nombre = '%s',cantidad = %d, precio = %f where id = %d
        """ % (new_nombre, ncantid, n_precio, p))
        k = input("desea seguir actualizando si/no: ")
cursor.close()
conn.commit()
conn.close()
