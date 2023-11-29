import MySQLdb


class RegistroDatos:
    def __init__(self):
        self.conn = \
            MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")

# VINCULADOS

    def insertar_vin(self, nombre, sexo, edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real):
        cursor = self.conn.cursor()
        sql = """insert into trabajadores_vin(nombre,sexo,edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump,
         plan_real)
         values('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(nombre, sexo, edad, fech_naci, nivel_pro,
                                                                        proy_vin, rol_en_pro, plan_cump, plan_real)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def buscar_trab_vin(self):
        cur = self.conn.cursor()
        sql = """select * from trabajadores_vin"""
        cur.execute(sql)
        registro = cur.fetchall()
        return registro

    def eliminar_vin(self, ide):
        cursor = self.conn.cursor()
        sql = """delete from trabajadores_vin where id = {}""".format(ide)
        cursor.execute(sql)
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a

