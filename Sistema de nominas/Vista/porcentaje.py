from UI.porcentaje import *
from conexion_db_gestion import RegistroDatos


class Porcentaje(QtWidgets.QWidget):
    def __init__(self, present):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.pre = present
        self.datos = RegistroDatos()
        self.ui.pushButton_determinar.clicked.connect(self.determinar_por)

    def determinar_por(self):
        datos = self.datos.buscar_trab_vin()
        por_dado = self.ui.spinBox.value()
        total = len(datos)
        if len(datos) == 0:
            return QtWidgets.QMessageBox.critical(self, "Error", "No hay datos")
        parte = 0
        for row in datos:
            if row[8] > por_dado:
                parte += 1
        por_total = int((parte / total) * 100)
        msg = QtWidgets.QMessageBox.information(self, "Porciento", "El porciento de"
                                                                   " trabajadores es de {}".format(por_total))
        return msg
