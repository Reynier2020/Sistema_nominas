from datetime import date


class Medicamento:
    
    def __init__(self, nombre, mg_contiene, forma_presentacion, precio_unitario, fecha_vencimiento):
        self.nombre = nombre
        self.mg_contiene = mg_contiene
        self.forma_presentacion = forma_presentacion
        self.precio_unitario = precio_unitario
        self.fecha_vencimiento = fecha_vencimiento
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
    
    @property
    def mg_contiene(self):
        return self.__mg_contiene
    
    @mg_contiene.setter
    def mg_contiene(self, value):
        self.__mg_contiene = value
    
    @property
    def forma_presentacion(self):
        return self.__forma_presentacion
    
    @forma_presentacion.setter
    def forma_presentacion(self, value):
        self.__forma_presentacion = value

    @property
    def precio_unitario(self):
        return self.__precio_unitario
    
    @precio_unitario.setter
    def precio_unitario(self, value):
        self.__precio_unitario = value

    @property
    def fecha_vencimiento(self):
        return self.__fecha_vencimiento
    
    @fecha_vencimiento.setter
    def fecha_vencimiento(self, value):
        self.__fecha_vencimiento = value

    def importe(self, cant_unidades):
        return self.precio_unitario * cant_unidades + 5
    
    def esta_vencido(self):
        return self.fecha_vencimiento <= date.today()
