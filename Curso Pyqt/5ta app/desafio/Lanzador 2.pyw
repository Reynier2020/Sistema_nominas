import sys
from alimentos_2 import *


class Lanzador(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.checkBox_pizza.clicked.connect(self.calcular)
        self.ui.checkBox_ensalada.clicked.connect(self.calcular)
        self.ui.checkBox_pat_fritas.clicked.connect(self.calcular)
        self.ui.checkBox_pollo.clicked.connect(self.calcular)

    def calcular(self):
        precio = 0
        if self.ui.checkBox_pizza.isChecked():
            precio += 20
        if self.ui.checkBox_ensalada.isChecked():
            precio += 5
        if self.ui.checkBox_pat_fritas.isChecked():
            precio += 10
        if self.ui.checkBox_pollo.isChecked():
            precio += 15

        self.ui.lineEdit_resultado.setText(str(precio))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador = Lanzador()
    lanzador.show()
    sys.exit(app.exec())