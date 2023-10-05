from Trabajador import *
from Proyecto import *


class Trabajadorvin(Trabajador):

    def __int__(self, nombre, edad, sexo, fecha_naci, proy, nivel_pro, rol_proy, plan_cump_men, plan_real_cump):
        super().__int__(nombre, edad, sexo, fecha_naci, nivel_pro)
        self.__proy = proy
        self.__rol_proy = rol_proy
        self.__plan_cump_men = plan_cump_men
        self.__plan_real_cupm = plan_real_cump

