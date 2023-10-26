from Trabajador_vin import Trabajadorvin
from Proyecto import Proyecto
from Trabajador_no_vin import TrabajadorNoVin


class Empresa:
    def __init__(self):
        self.__lista_proyectos = []
        self.__lista_trabajadores = []

    @property
    def lista_trabajadores(self):
        return self.__lista_trabajadores

    @property
    def lista_proyectos(self):
        return self.__lista_proyectos

    def insertar_trabajador(self, trabajador):
        if self.chequear_trabajador_x_nom(trabajador.nombre) is not None:
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores.append(trabajador)

    def chequear_trabajador_x_nom(self, nombre):
        for i in range(len(self.lista_trabajadores)):
            if self.lista_trabajadores[i].es_nombre(nombre):
                return i

    def eliminar_trabajador(self, nombre):
        if self.chequear_trabajador_x_nom(nombre) is None:
            raise Exception("El trabajador no existe")
        self.lista_trabajadores.remove(self.chequear_trabajador_x_nom(nombre))

    def actualizar_trabjador(self, nom_ant, trabajador):
        cheq_trab = self.chequear_trabajador_x_nom(nom_ant)
        if cheq_trab is None:
            raise Exception("El trabajador no existe")
        cheq_nue = self.chequear_trabajador_x_nom(trabajador.nombre)
        if (cheq_nue is not None) and (cheq_nue != cheq_trab):
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores[cheq_trab] = trabajador

    def listar_vinculados(self):
        lista_vin = []
        for tra in self.lista_trabajadores:
            if isinstance(tra, Trabajadorvin):
                lista_vin.append(tra)
        return lista_vin

    def listar_no_vin(self):
        lista_no_vin = []
        for tra in self.lista_trabajadores:
            if isinstance(tra, TrabajadorNoVin):
                lista_no_vin.append(tra)
        return lista_no_vin

    def chequear_proyecto(self, nombre):
        for i in self.__lista_proyectos:
            if self.__lista_proyectos[i].es_
    def inertar_proyrcto(self, pro):
        if