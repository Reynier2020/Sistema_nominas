from Trabajador import *


class TrabajadorNoVin(Trabajador):
    def __init__(self, nombre, edad, sexo, fecha_naci, nivel_pro, horas_trab, respons, llegadas_tarde, dept):
        super().__init__(nombre, edad, sexo, fecha_naci, nivel_pro)
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

    def calcular_salario_no_vin(self):
        if self.nivel_pro == "profesional":
            a = 80
        elif self.nivel_pro == "tecnico medio":
            a = 60
        else:
            a = 40

        if self.responsabilidad == "jefe de departamento":
            b = 120
        else:
            b = 200

        salario = int((self.horas_tabajadas * 12.5 + b - (5 * self.llegadas_tardes)) + a)
        return salario

    def string_variado(self):
        return "nombre: {}\nedad: \nsexo: {}\nnivel profesional: {}\nresponsabilidad: {}\ndepartamento: {}".format(
            self.nombre, self.edad, self.sexo, self.nivel_pro, self.responsabilidad, self.dept)
