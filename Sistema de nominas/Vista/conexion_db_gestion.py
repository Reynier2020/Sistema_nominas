import MySQLdb


class RegistroDatos:
    def __init__(self):
        self.conn = \
            MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")

# VINCULADOS

    def insertar_vin(self, nombre, sexo, edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real):
        cursor = self.conn.cursor()
        try:
            sql = """insert into trabajadores_vin(nombre,sexo,edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump,
            plan_real)
            values('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(nombre, sexo, edad, fech_naci, nivel_pro,
                                                                        proy_vin, rol_en_pro, plan_cump, plan_real)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        self.conn.commit()
        cursor.close()

    def buscar_trab_vin(self):
        cur = self.conn.cursor()
        sql = """select t.id, t.nombre,t.sexo, t.edad, t.fecha_naci,
                 t.nivel_pro,p.nombre, t.rol_proyecto, t.plan_cump,
                 t.plan_real from trabajadores_vin t left join proyectos p on p.id = t.proy_vin"""
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

    def act_trab_vin(self,  nombre, sexo, edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real, ide):
        curs = self.conn.cursor()
        sql = """update trabajadores_vin set nombre = '{}', sexo = '{}', edad = '{}',
         fech_naci = '{}', nivel_pro = '{}', proy_vin = '{}', rol_en_pro '{}', plan_cump = '{}', plan_real = '{}'
          where id = '{}' """.format(nombre, sexo, edad, fech_naci, nivel_pro, proy_vin,
                                     rol_en_pro, plan_cump, plan_real, ide)
        curs.execute(sql)
        a = curs.rowcount
        self.conn.commit()
        curs.close()
        return a

    def buscar_pro(self):
        cursor = self.conn.cursor()
        sql = """select nombre from proyectos"""
        cursor.execute(sql)
        list_pro = cursor.fetchall()
        cursor.close()
        return list_pro
