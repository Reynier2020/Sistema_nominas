from __future__ import division
from Practica import *
import sys


class Lanzador(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def calcular(self):
        if len(self.ui.lineEdit_cantidad.text()) != 0:
            q = int(self.ui.lineEdit_cantidad.text())
        else:
            q = 0
        if len(self.ui.lineEdit_precio.text()) != 0:
            r = int(self.ui.lineEdit_precio.text())
        else:
            r = 0
        if len(self.ui.lineEdit_descuento.text()) != 0:
            s = int(self.ui.lineEdit_descuento.text())
        else:
            s = 0
        cantidad_pre = q * r
        descuento = cantidad_pre*s/100
        cantidad_net = cantidad_pre - descuento
        self.ui.label_resultado.setText("cantidad total: "+str(cantidad_pre),
                                        ", descuento: "+str(descuento), ", cantidad neta: " + str(cantidad_net))

        self.ui.pushButton_calcular.clicked.connect(self.calcular)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador = Lanzador()
    lanzador.show()
    sys.exit(app.exec())
