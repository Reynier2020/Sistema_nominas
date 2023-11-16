from Trabajador import *
from Proyecto import *


class Trabajadorvin(Trabajador):

    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, rol_proy, plan_cump_men, plan_real_cump):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro)
        self.__proy_vin = list[Proyecto.nom_proy]
        self.__rol_proy = rol_proy
        self.__plan_cump_men = plan_cump_men
        self.__plan_real_cump = plan_real_cump

    def string_variado(self):
        return "nombre: {}\nedad: \nsexo:{}\nnivel profesional: {}\nrol en proyecto:{}\nproyecto vinculado:{}".format(
            self.nombre, self.edad, self.sexo, self.nivel_pro, self.rol_proy, self.proy_vin)

    @property
    def proy_vin(self):
        return self.__proy_vin

    @proy_vin.setter
    def proy_vin(self, value):
        self.__proy_vin = value

    @property
    def rol_proy(self):
        return self.__rol_proy

    @rol_proy.setter
    def rol_proy(self, value):
        self.__rol_proy = value

    @property
    def plan_cump_men(self):
        return self.__plan_cump_men

    @plan_cump_men.setter
    def plan_cump_men(self, value):
        self.__plan_cump_men = value

    @property
    def plan_real_cump(self):
        return self.__plan_real_cump

    @plan_real_cump.setter
    def plan_real_cump(self, value):
        self.__plan_real_cump = value

    def est_plan_real(self, plan):
        return self.plan_real_cump == plan

    def actualizar_pla_real(self, plan_nue):
        if self.plan_real_cump <= plan_nue:
            self.plan_real_cump = plan_nue
        else:
            return

    def calcular_salario(self):
        if self.nivel_pro == "profesional":
            a = 80
        elif self.nivel_pro == "tecnico medio":
            a = 60
        else:
            a = 40

        if self.plan_real_cump > 100:
            b = 25.0
        elif (self.plan_real_cump <= 100) and (self.plan_real_cump >= 95):
            b = 21.5
        elif (self.plan_real_cump <= 94) and (self.plan_real_cump >= 80):
            b = 18.5
        else:
            b = 15.0

        salario = int(self.plan_real_cump * b + a)
        return salario
