from Persona import Persona


class Profesor(Persona):
    def __init__(self,nombre, edad, sexo, ci, asignatura):
        super().__init__(nombre, edad, sexo, ci)
        self.__asignatura = asignatura

    @property
    def asignatura(self):
        return self.__asignatura

    @asignatura.setter
    def asignatura(self, valor):
        self.__asignatura = valor

p = Profesor("KK",87, "binario",87687557,"pcd")

