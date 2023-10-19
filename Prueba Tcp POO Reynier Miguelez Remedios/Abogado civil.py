from Abogado import Abogado

class Abogado_civil(Abogado):
    def __init__(self,nombre, especialidad,salario):
        super().__init__(nombre,especialidad,salario)

    def calcular_honorario(self, caso):
        if caso.self.__tipo == "civil":
            hono = caso.__monto * (10 / 100)
            return hono
        else:
            return 0


