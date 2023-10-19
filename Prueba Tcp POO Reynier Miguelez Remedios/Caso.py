#el monto lo pondre como parametro
class Caso:
    def __init__(self, nombre, tipo, estado, monto):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado
        self.__monto = monto

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self,valor):
        self.__estado = valor

    def __str__(self):
        return self.__nombre
