from Abogado import Abogado

class Abogado_penal(Abogado):

    def calcular_honorario(self, caso):
        if caso.self.__tipo == "penal":
            hono = 5000 + ((5 / 100) * caso.__monto)
            return hono
        else:
            return 0

