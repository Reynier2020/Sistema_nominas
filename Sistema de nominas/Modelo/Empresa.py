from Trabajador import Trabajador
from  Proyecto import  Proyecto
from Trabajador_vin import Trabajadorvin

class Empresa:
    def __init__(self):
        self.__lista_trabajadores_vin = ()
        self.__lista_trabajadores_no_vin = ()
    def insertar_trabajador(self, trabajador):
        list_vin = self.__lista_trabajadores_vin
        list_no_vin = self.__lista_trabajadores_no_vin
        if trabajador.
