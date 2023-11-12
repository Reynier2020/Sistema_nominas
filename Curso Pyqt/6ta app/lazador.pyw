import sys
from lista import *


class Lanzador(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_pais)

    def add_pais(self):
        texto = self.ui.lineEdit_pais.text()
        self.ui.listWidget.addItem(texto)
        self.ui.lineEdit_pais.clear()
        self.ui.lineEdit_pais.setFocus()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador_2 = Lanzador()
    lanzador_2.show()
    sys.exit(app.exec())
