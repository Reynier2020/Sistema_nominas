class Trabajador:

    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, es_vin):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__fecha_naci = fecha_naci
        self.__nivel_pro = nivel_pro
        self.__es_vin = es_vin

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

    @property
    def es_vin(self):
        return self.__es_vin

    @es_vin.setter
    def es_vin(self, value):
        self.__es_vin = value

    def es_nombre(self, nombre):
        return self.__nombre == nombre

    def __str__(self):
        return self.nombre

    def string_variado(self):
        return "nombre: {}\nedad: \nsexo:{}\nnivel profesional: {}\nes vinculado: {}".format(
            self.nombre, self.edad, self.sexo, self.nivel_pro, self.es_vin)

    def calcular_salario(self):
        pass