import sys
from seg_app import *


class Lanzador(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QMetaObject.connectSlotsByName(self.)

    def mostrar_mensaje(self):
        self.ui.label_Mensaje.setText("Hola " + self.ui.lineEdit_escribaUnNombre.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    miapp = Lanzador()
    miapp.show()
    sys.exit(app.exec())


