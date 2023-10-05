from Trabajador import Trabajador
from Proyecto import Proyecto


class Empresa:
    def __init__(self):
        self.__lista_trabajadores_vin = []
        self.__lista_trabajadores_no_vin = []
        self.__lista_proyectos = []

    def insertar_trabajador(self, trabajador):
        list_vin = self.__lista_trabajadores_vin
        list_no_vin = self.__lista_trabajadores_no_vin
        if trabajador.es_vin:
            list_vin.append(trabajador)
        else:
            list_no_vin.append(trabajador)
