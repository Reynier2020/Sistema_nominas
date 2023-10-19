from Caso import Caso
class Abogado:

    def __init__(self, nombre, especialidad,salario):
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__salario = salario
        self.__lista_casos = []

    def calcular_honorario(self, caso):
        pass

    def agregar_caso(self, caso):
        self.__lista_casos.append(caso)

    def eliminar_caso(self, caso):
        self.__lista_casos.remove(caso)

    def filtrar_caso(self):
        x = Caso.estado
        a = list(filter(lambda x : x == "activo",self.__lista_casos))



