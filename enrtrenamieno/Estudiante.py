from Persona import Persona


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, ci, becado):
        super().__init__(nombre, edad, sexo, ci)
        self.__becado = becado

    @property
    def becado(self):
        return self.__becado

    @becado.setter
    def becado(self, valor):
        self.__becado = valor

