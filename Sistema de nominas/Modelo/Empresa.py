from Trabajador import Trabajador
from operator import attrgetter
from Trabajador_vin import Trabajadorvin


class Empresa:
    def __init__(self):
        self.__lista_proyectos = []
        self.__lista_trabajadores_vin = []
        self.__lista_trabajadores_no_vin = []
        self.__lista_trabajadores = []

    @property
    def lista_trabajadores(self):
        return self.__lista_trabajadores

    @property
    def lista_trabajadores_no_vin(self):
        return self.__lista_trabajadores_no_vin

    @property
    def lista_trabajadores_vin(self):
        return self.__lista_trabajadores_vin

    @property
    def lista_proyectos(self):
        return self.__lista_proyectos

# TRABAJADOR_VINCULADO

    def insertar_trabajador_vin(self, trabajador):
        if self.chequear_trabajador_vin_x_nom(trabajador.nombre) is not None:
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores_vin.append(trabajador)

    def chequear_trabajador_vin_x_nom(self, nombre):
        for i in range(len(self.lista_trabajadores_vin)):
            if self.lista_trabajadores_vin[i].Trabajador.es_nombre(nombre):
                return i

    def eliminar_trabajador_vin(self, nombre):
        if self.chequear_trabajador_vin_x_nom(nombre) is None:
            raise Exception("El trabajador no existe")
        self.lista_trabajadores_vin.remove(self.chequear_trabajador_vin_x_nom(nombre))

    def actualizar_trabjador_vin(self, nom_ant, trabajador):
        cheq_trab = self.chequear_trabajador_vin_x_nom(nom_ant)
        if cheq_trab is None:
            raise Exception("El trabajador no existe")
        cheq_nue = self.chequear_trabajador_vin_x_nom(trabajador.nombre)
        if (cheq_nue is not None) and (cheq_nue != cheq_trab):
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores_vin[cheq_trab] = trabajador

# TRABAJADOR NO VINCULADO

    def insertar_trab_no_vin(self, tra):
        if self.chequear_tra_no_vin(tra.nombre) is not None:
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores_no_vin.append(tra)

    def chequear_tra_no_vin(self, nombre):
        for i in self.lista_trabajadores_no_vin:
            if self.lista_trabajadores_no_vin[i].Trabajador.es_nombre(nombre):
                return i

    def eliminar_no_vin(self, nombre):
        if self.chequear_tra_no_vin(nombre) is None:
            raise Exception("El trabajador no existe")
        self.lista_trabajadores_no_vin.remove(self.chequear_tra_no_vin(nombre))

    def actualizar_trabjador_no_vin(self, nom_ant, trabajador):
        cheq_trab = self.chequear_tra_no_vin(nom_ant)
        if cheq_trab is None:
            raise Exception("El trabajador no existe")
        cheq_nue = self.chequear_tra_no_vin(trabajador.nombre)
        if (cheq_nue is not None) and (cheq_nue != cheq_trab):
            raise Exception("El trabajador ya existe")
        self.lista_trabajadores_no_vin[cheq_trab] = trabajador

    def chequear_proyecto(self, nombre):
        for i in range(len(self.__lista_proyectos)):
            if self.__lista_proyectos[i].Proyecto.es_nom_pro(nombre):
                return i

    def inertar_proyecto(self, pro):
        cheq_pro = self.chequear_proyecto(pro.nombre)
        if cheq_pro is not None:
            raise Exception("El pryecto ya existe")
        self.lista_proyectos.append(pro)

    def eliminar_proyecto(self, nombre):
        if self.chequear_proyecto(nombre) is None:
            raise Exception("El proyecto no existe")
        self.lista_proyectos.remove(self.chequear_proyecto(nombre))

    def listar_proyecto(self):
        for i in self.lista_proyectos:
            return i

    def chequear_trabajador(self, nombre):
        for i in self.lista_trabajadores:
            if self.lista_trabajadores[i].Trabajador.es_nombre(nombre):
                return i

    def listar_trabajadores(self):
        self.lista_trabajadores.append(list[self.lista_trabajadores_no_vin.extend(self.lista_trabajadores_vin)])
        return self.lista_trabajadores

    def ordenar_proyectos(self):
        sorted(self.lista_proyectos, key=attrgetter('costo', 'pciento_culm'), reverse=True)

    def despedir_trabajador(self, nombre):
        a = self.chequear_trabajador(nombre)
        if a is None:
            raise Exception("El trabajador no existe")
        return "El trabajador {} con un salario de {} ha sido despedido".format(
            Trabajador.string_variado(a), Trabajador.calcular_salario(a)
        )

    def eliminar_trabajador(self, nombre):
        if self.chequear_trabajador(nombre) is None:
            raise Exception("El trabajador no existe")
        self.lista_trabajadores.remove(self.chequear_trabajador(nombre))

    def porciento_trab_vin_cumplido(self, porciento):
        a = len(self.lista_trabajadores_vin)
        b = []
        c = len(b)
        for i in self.lista_trabajadores_vin:
            if Trabajadorvin.plan_real_cump > porciento:
                b.append(i)
        resultado = (c * 100)/a
        return resultado

    def sumatoria_salarios(self):
        total_salarios = 0
        for i in self.lista_trabajadores:
            total_salarios += Trabajador.calcular_salario(i)
        return total_salarios
