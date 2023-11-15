from medicamento_controlado import MedicamentoControlado


class Farmacia:

    def __init__(self):
        self.lista_medicamentos = []
    
    @property
    def lista_medicamentos(self):
        return self.__lista_medicamentos

    @lista_medicamentos.setter
    def lista_medicamentos(self, value):
        self.__lista_medicamentos = value
    
    # determinar el importe de una compra en la farmacia
    def importe_compra(self, nombre_medicamento, cant_unidades):
        for med in self.lista_medicamentos:
            if med.nombre == nombre_medicamento:
                return med.importe(cant_unidades)
        return None
    
    # determinar si se puede comprar un medicamento controlado
    def comprar_medicamento_controlado(self, nombre_med, cant_unidades):
        for med in self.lista_medicamentos:
            if med.nombre == nombre_med and isinstance(med, MedicamentoControlado):
                return cant_unidades <= med.cant_max_venta and not med.esta_vencido() 
        return None
