import MySQLdb


class RegistroDatos:
    def __init__(self):
        self.conn = \
            MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")

    def insertar_vin(self, nombre, sexo, edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real):
        cursor = self.conn.cursor()
        sql = """insert into trabajadores_vin(nombre,sexo,edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump,
         plan_real)
         values('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(nombre, sexo, edad, fech_naci, nivel_pro,
                                                                        proy_vin, rol_en_pro, plan_cump, plan_real)
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
