""""1. Sistema de nóminas.
Se desea realizar un sistema para gestionar las nóminas de una empresa de proyectos. Se conoce que en la entidad hay trabajadores vinculados que se les paga por productividad y hay trabajadores que se les paga por la estancia en su puesto de trabajo en
el horario establecido. De los trabajadores en general se registra el nombre, el sexo, la fecha de nacimiento, y el nivel profesional (que puede ser profesional, técnico medio u obrero calificado); por otro lado, de los trabajadores vinculados se registran los datos del proyecto en que trabaja, su rol dentro del proyecto, el plan mensual de
cumplimiento de su tarea, que es un valor numérico entre 1 y 100, y el valor real de cumplimiento de su tarea. De los trabajadores no vinculados se registra, además, su responsabilidad (que puede ser obrero, jefe de departamento o director de la empresa), el departamento a que pertenece, la cantidad de llegadas tarde que lleva en el mes y la cantidad de horas trabajadas en el mes. De los proyectos se registra el
nombre del proyecto, el cliente, el costo del proyecto, la fecha de inicio y de culminación y el porciento de terminación. Por último, se conoce que el sistema actualiza su información mensualmente y que tiene una lista con todos los datos de las nóminas de todos los trabajadores de la empresa, el mes y año en que se está trabajando, así como una lista de los proyectos en los que está trabajando la empresa.
El sistema debe permitir las siguientes funcionalidades:
a)	Implemente las funcionalidades necesarias para gestionar (insertar, actualizar, eliminar y listar) los datos de los trabajadores de forma independiente (vinculados y no vinculados), los datos de los proyectos, así como actualizar los datos de cumplimiento del trabajo mensual de cada trabajador.
b)	Implemente la funcionalidad necesaria para determinar el salario de un trabajador dado su nombre y teniendo en cuenta que este se determina a partir de la bonificación por estudios terminados que es de $80 para los profesionales, $60 para los técnicos medio y $40 para los obreros calificados además del cumplimiento de sus labores que se determina de la siguiente forma:
•	Para los trabajadores no vinculados se determina entre la cantidad de horas trabajadas por $12.5 más la bonificación del cargo que es $120 para los jefes de departamento y $200 para el director de la empresa restándole $5 por cada llegada tarde.
•	Para los trabajadores vinculados se determina por el porciento de cumplimiento de su tarea del mes por el coeficiente de eficiencia que es 21.5 si el por ciento de cumplimiento de su tarea del mes está entre 95 y 100, es 18.5 si el porciento está entre 80 y 94, 15 para un porciento menor de 80, y 25 para un porciento mayor de 100.
c)	Implemente la funcionalidad necesaria para determinar el listado de proyectos que tiene la empresa ordenado en orden descendente por el valor añadido que es el costo por el porciento de terminación.
d)	Implemente la funcionalidad necesaria para despedir un trabajador del sistema devolviendo todos sus datos y determinando su salario acumulado en el mes actual.
e)	Implemente la funcionalidad necesaria para determinar qué porciento de los trabajadores vinculados cumplen con más de un porciento dado su labor mensual.
f)	Implemente la funcionalidad necesaria para listar a final de mes la nómina de la empresa con los datos de cada trabajador y el salario a cobrar, además de la sumatoria total de todos los salarios.
g)	Pruebe que las operaciones implementadas en el modelo funcionan correctamente según los datos de prueba que usted le entró al programa.
"""
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
        for i in range(len(self.__lista_proyectos)):
            if self.__lista_proyectos[i].es_nom_pro(nombre):
                return i

    def inertar_proyrcto(self, pro):
        cheq_pro = self.chequear_proyecto(pro.nombre)
        if cheq_pro is not None:
            raise Exception("El pryecto ya existe")
        self.lista_proyectos.append(pro)


