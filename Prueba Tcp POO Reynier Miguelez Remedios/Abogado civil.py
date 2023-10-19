from Abogado import Abogado

class Abogado_civil(Abogado):
    def __init__(self,):
    def calcular_honorario(self, caso):
        if caso.self.__tipo == "civil":
            hono = caso.__monto * (10 / 100)
            return hono
        else:
            return 0


