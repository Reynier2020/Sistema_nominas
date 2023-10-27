from Trabajador import *
from Proyecto import *


class Trabajadorvin(Trabajador):

    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, es_vin, rol_proy, plan_cump_men, plan_real_cump):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro, es_vin)
        self.__proy = list[Proyecto.nom_proy]
        self.__rol_proy = rol_proy
        self.__plan_cump_men = plan_cump_men
        self.__plan_real_cump = plan_real_cump

    @property
    def proy(self):
        return self.__proy

    @proy.setter
    def proy(self, value):
        self.__proy = value

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


