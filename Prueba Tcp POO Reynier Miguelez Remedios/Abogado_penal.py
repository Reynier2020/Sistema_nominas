from Abogado import Abogado

class Abogado_penal(Abogado):
    def __init__(self,nombre, especialidad, salario):
        super().__init__(nombre, especialidad, salario)

    def calcular_honorario(self, caso):
        if caso.self.__tipo == "penal":
            hono = 5000 + ((5 / 100) * caso.__monto)
            return hono
        else:
            return 0

