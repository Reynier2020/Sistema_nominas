import MySQLdb
conn = MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")
cursor = conn.cursor()
k = "SI"
while k.upper() == "SI":
    p = int(input("escriba una ID: "))
    cursor.execute("""
    select * from productos where id = %d
    """ % p)
    row = cursor.fetchone()
    if row is None:
        print("no se han encontrado datos asignados al id %d" % p)
    else:
        print("los datos del id %d son los siguientes" % p)
        print("nombre: %s, cantidad: %d, precio: %f" % (row[1], row[2], row[3]))
        a = str(input("desea elimnar el producto con id %d ? : " % p))
        if a.upper() == "SI":
            cursor.execute("""
            delete from productos where id = %d
            """ % p)
        k = input("desea seguir eliminando si/no: ")
cursor.close()
conn.commit()
conn.close()
