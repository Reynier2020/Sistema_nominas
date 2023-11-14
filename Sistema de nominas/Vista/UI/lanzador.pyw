import sys
from ventana import *


class Lanzador(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindo_principal()
        self.ui.setupUi(self)
        self.ui.actionSalir.triggered.connect(quit)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador = Lanzador()
    lanzador.show()
    sys.exit(app.exec())
