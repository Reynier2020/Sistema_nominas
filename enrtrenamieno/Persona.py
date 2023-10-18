"""una clase persona, una estudiante y otra profesores. persona tiene nombre,
edad, sexo, CI.Estudiante tiene vecados o no.Prof tiene asignatura """


class Persona:
    def __init__(self, nombre, edad, sexo, ci):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__ci = ci

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        self.__edad = valor

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def set_sexo(self, valor):
        self.__sexo = valor

    @property
    def get_ci(self):
        return self.__ci

    @get_ci.setter
    def set_ci(self, valor):
        self.__ci = valor
