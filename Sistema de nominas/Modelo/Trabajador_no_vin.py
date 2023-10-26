from Trabajador import *


class TrabajadorNoVin(Trabajador):
    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, es_vin, horas_trab, respons, llegadas_tarde, dept):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro, es_vin)
        self.__horas_tabajadas = horas_trab
        self.__responsabilidad = respons
        self.__llegadas_tarde = llegadas_tarde
        self.__dept = dept

    @property
    def horas_tabajadas(self):
        return self.__horas_tabajadas

    @horas_tabajadas.setter
    def horas_trabajadas(self, value):
        self.__horas_tabajadas = value

    @property
    def responsabilidad(self):
        return self.__responsabilidad

    @responsabilidad.setter
    def responsabilidad(self, value):
        self.__responsabilidad = value

    @property
    def llegadas_tardes(self):
        return self.__llegadas_tarde

    @llegadas_tardes.setter
    def llegadas_tardes(self, value):
        self.__llegadas_tarde = value

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, value):
        self.__dept = value
