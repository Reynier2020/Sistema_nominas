from medicamento import Medicamento


class MedicamentoControlado(Medicamento):

    def __init__(self, nombre, mg_contiene, forma_presentacion, precio_unitario, fecha_vencimiento, especialidad_doctor_receta, cant_max_venta):
        Medicamento.__init__(self, nombre, mg_contiene, forma_presentacion, precio_unitario, fecha_vencimiento)
        self.especialidad_doctor_receta = especialidad_doctor_receta
        self.cant_max_venta = cant_max_venta
    
    @property
    def especialidad_doctor_receta(self):
        return self.__especialidad_doctor_receta
    
    @especialidad_doctor_receta.setter
    def especialidad_doctor_receta(self, value):
        self.__especialidad_doctor_receta = value

    @property
    def cant_max_venta(self):
        return self.__cant_max_venta

    @cant_max_venta.setter
    def cant_max_venta(self, value):
        self.__cant_max_venta = value

    def importe(self, cant_unidades):
        return Medicamento.importe(self, cant_unidades) + 10
