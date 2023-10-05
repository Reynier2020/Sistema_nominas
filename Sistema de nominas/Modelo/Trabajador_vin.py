from Trabajador import *
from Proyecto import *


class Trabajadorvin(Trabajador):

    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, rol_proy, plan_cump_men, plan_real_cump):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro)
        self.__proy = Proyecto.nom_proy
        self.__rol_proy = rol_proy
        self.__plan_cump_men = plan_cump_men
        self.__plan_real_cump = plan_real_cump

    @property
    def proy(self):
        return self.__proy

    @proy.setter
    def set_proy(self, value):
        return self.__proy == value

    @property
    def rol_proy(self):
        return self.__rol_proy

    @rol_proy.setter
    def set_rol_proy(self, value):
        return self.__rol_proy == value

    @property
    def plan_cump_men(self):
        return self.__plan_cump_men

    @plan_cump_men.setter
    def set_plan_cump_men(self, value):
        return self.__plan_cump_men == value

    @property
    def plan_real_cump(self):
        return self.__plan_real_cump

    @plan_real_cump.setter
    def set_plan_real_cump(self, value):
        return self.__plan_real_cump == value
