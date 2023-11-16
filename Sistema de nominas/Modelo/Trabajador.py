from datetime import date


class Trabajador:
    _atri_identif = 0

    def __new__(cls, *args, **kwargs):
        cls._atri_identif += 1
        return super().__new__(cls)

    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro):
        self.identificador = self._atri_identif
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__fecha_naci = fecha_naci
        self.__nivel_pro = nivel_pro

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, value):
        self.__edad = value

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, value):
        self.__sexo = value

    @property
    def fecha_naci(self):
        self.__fecha_naci = date(day=int(), month=int(), year=int())
        return self.__fecha_naci

    @fecha_naci.setter
    def fecha_naci(self, value):
        self.__fecha_naci = value

    @property
    def nivel_pro(self):
        return self.__nivel_pro

    @nivel_pro.setter
    def nivel_pro(self, value):
        self.__nivel_pro = value

    def es_nombre(self, nombre):
        return self.__nombre == nombre

    def __str__(self):
        return self.nombre

    def string_variado(self):
        pass

    def calcular_salario(self):
        pass

    def obtener_id(self, ident):
        return self.identificador == ident
