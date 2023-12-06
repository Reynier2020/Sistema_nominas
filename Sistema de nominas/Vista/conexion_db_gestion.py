import MySQLdb


class RegistroDatos:
    def __init__(self):
        self.conn = \
            MySQLdb.connect(host="localhost", user="root", password="r3yni3r2020@gmail.com", db="sistema_nominas")

# VINCULADOS

    def insertar_vin(self, nombre, sexo, edad, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real):
        cursor = self.conn.cursor()
        try:
            sql = """insert into trabajadores_vin(nombre, edad, sexo, fecha_naci, nivel_pro,
                proy_vin, rol_proyecto, plan_cump, plan_real)
            values('{}',{},'{}','{}','{}',{},'{}',{},{})""".format(nombre, edad, sexo, fech_naci, nivel_pro,
                                                                   proy_vin, rol_en_pro, plan_cump, plan_real)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        self.conn.commit()
        cursor.close()

    def busca_al_trab_vin(self, nombre_vin):
        curso = self.conn.cursor()
        try:
            sql = """select * from trabajadores_vin where nombre = '{}'""".format(nombre_vin)
            curso.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        resultado = curso.fetchall()
        return resultado

    def buscar_trab_vin(self):
        cur = self.conn.cursor()
        try:
            sql = """select t.id, t.nombre,t.sexo, t.edad, t.fecha_naci,
                    t.nivel_pro,p.nombre, t.rol_proyecto, t.plan_cump,
                    t.plan_real from trabajadores_vin t left join proyectos p on p.id = t.proy_vin"""
            cur.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        registro = cur.fetchall()
        return registro

    def eliminar_vin(self, ide):
        cursor = self.conn.cursor()
        try:
            sql = """delete from trabajadores_vin where id = {}""".format(ide)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a

    def act_trab_vin(self,  nombre, edad, sexo, fech_naci, nivel_pro, proy_vin, rol_en_pro, plan_cump, plan_real, ide):
        curs = self.conn.cursor()
        try:
            sql = """update trabajadores_vin set nombre = '{}', edad = {}, sexo = '{}', fecha_naci = '{}',
            nivel_pro = '{}', proy_vin = {}, rol_proyecto = '{}', plan_cump = {}, plan_real = {} 
            where id = {} """.format(nombre, edad, sexo, fech_naci, nivel_pro, proy_vin,
                                     rol_en_pro, plan_cump, plan_real, ide)
            curs.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = curs.rowcount
        self.conn.commit()
        curs.close()
        return a

#   TRABAJADORES_NO_VIN
    def buscar_no_vin(self):
        cur = self.conn.cursor()
        try:
            sql = """select * from trabajadores_no_vin"""
            cur.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        registro = cur.fetchall()
        return registro

    def eliminar_no_vin(self, ide):
        cursor = self.conn.cursor()
        try:
            sql = """delete from trabajadores_no_vin where id = {}""".format(ide)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a

    def insetrar_no_vin(self, nombre, edad, sexo, fecha_naci, nivel_pro,
                        responsabilidad, llegadas_tarde, horas_trabajadas):
        cursor = self.conn.cursor()
        try:
            sql = """insert into trabajadores_no_vin(nombre,edad,sexo,fecha_naci,nivel_pro,responsabilidad,
            llegadas_tarde,horas_trabajadas)
            values('{}',{},'{}','{}','{}','{}',{},{});""".format(nombre, edad, sexo, fecha_naci, nivel_pro,
                                                                 responsabilidad, llegadas_tarde, horas_trabajadas)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        self.conn.commit()
        cursor.close()

    def actualizar_no_vin(self, nombre, edad, sexo, fecha_naci, nivel_pro,
                          responsabilidad, llegadas_tarde, horas_trabajadas, ide):
        cursor = self.conn.cursor()
        try:
            sql = """update trabajadores_no_vin set nombre = '{}', edad = {}, sexo = '{}', fecha_naci = '{}',
            nivel_pro = '{}',responsabilidad = '{}',llegadas_tarde = {},
            horas_trabajadas = {} where id = {}""".format(nombre, edad, sexo, fecha_naci, nivel_pro,
                                                          responsabilidad, llegadas_tarde, horas_trabajadas, ide)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a

    def busca_al_trab_no_vin(self, nombre_no_vin):
        curso = self.conn.cursor()
        try:
            sql = """select * from trabajadores_no_vin where nombre = '{}'""".format(nombre_no_vin)
            curso.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        resultado = curso.fetchall()
        return resultado

#   PROYECTOS

    def busca_el_pro(self, nomb_pro):
        cursor = self.conn.cursor()
        try:
            sql = """select * from proyectos where nombre = '{}'""".format(nomb_pro)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        list_pro = cursor.fetchall()
        cursor.close()
        return list_pro

    def buscar_pro(self):
        cursor = self.conn.cursor()
        try:
            sql = """select * from proyectos"""
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        list_pro = cursor.fetchall()
        cursor.close()
        return list_pro

    def insertar_proy(self, nombre, cliente, costo, fecha_inicio, fecha_culminacion, porcentaje_cump):
        cursor = self.conn.cursor()
        try:
            sql = """insert into proyectos(nombre, cliente, costo, fecha_inicio, fecha_culminacion, porcentaje_cump)
                    values('{}', '{}', {}, '{}', '{}', {})""".format(nombre, cliente, costo, fecha_inicio,
                                                                     fecha_culminacion, porcentaje_cump)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        self.conn.commit()
        cursor.close()

    def eliminar_proy(self, ide):
        cursor = self.conn.cursor()
        try:
            sql = """delete from proyectos where id = {}""".format(ide)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a

    def actualizar_proy(self, nombre, cliente, costo, fecha_inicio, fecha_culminacion, porcentaje_cump, ide):
        cursor = self.conn.cursor()
        try:
            sql = """update proyectos set nombre = '{}', cliente = '{}',costo = {},fecha_inicio = '{}',
            fecha_culminacion = '{}', porcentaje_cump = {} where id = {}""".format(nombre, cliente,
                                                                                   costo, fecha_inicio,
                                                                                   fecha_culminacion, porcentaje_cump,
                                                                                   ide)
            cursor.execute(sql)
        except MySQLdb.Error:
            self.conn.rollback()
        a = cursor.rowcount
        self.conn.commit()
        cursor.close()
        return a
