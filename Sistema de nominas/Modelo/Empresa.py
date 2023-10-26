from Trabajador import Trabajador
from Proyecto import Proyecto


class Empresa:
    def __init__(self):
        self.__lista_proyectos = []
        self.__lita_trabajadores = []

    @property
    def lista_trabajadores(self):
        return self.__lita_trabajadores

    @property
    def lista_proyectos(self):
        return self.__lista_proyectos

    def insertar_trabajador(self, trabajador):
        pass

    def chequear_trabajador(self,nombre):
        for i in range(len(self.__lita_trabajadores)):
            if

    def eliminar_trabajador(self,trabajador):
        lista_trabajadores = list(self.__lita_trabajadores)
        for e in range(len(lista_trabajadores)):
            lista_trabajadores.remove(trabajador)

    def actualizar_trabjador(self, trabajador):
        pass
