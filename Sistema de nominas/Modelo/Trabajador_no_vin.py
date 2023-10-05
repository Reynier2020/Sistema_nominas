from Trabajador import *


class TrabajadorNoVin(Trabajador):
    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, horas_trabjadas, respons, llegadas_tarde, dept):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro)
        self.__horas_tabajadas = horas_trabjadas
        self.__responsabilidad = respons
        self.__llegadas_tarde = llegadas_tarde
        self.__dept = dept

    @property
    def horas_tabajadas(self):
        return self.__horas_tabajadas

    @horas_tabajadas.setter
    def set_horas_trabajadas(self, value):
        return self.__horas_tabajadas == value

    @property
    def responsabilidad(self):
        return self.__responsabilidad

    @responsabilidad.setter
    def set_responsabilidad(self, value):
        return self.__responsabilidad == value

    @property
    def llegadas_tardes(self):
        return self.__llegadas_tarde

    @llegadas_tardes.setter
    def set_llegadas_tardes(self, value):
        return self.__llegadas_tarde == value

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def set_dept(self, value):
        return self.__dept == value
