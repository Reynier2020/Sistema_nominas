import sys
from lista import *


class Lanzador(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_pais)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar)

    def add_pais(self):
        texto = self.ui.lineEdit_pais.text()
        if len(self.ui.lineEdit_pais.text()) == 0:
            return 0
        else:
            self.ui.listWidget.addItem(texto)
            self.ui.lineEdit_pais.clear()
            self.ui.lineEdit_pais.setFocus()

    def eliminar(self):
        objeto = self.ui.listWidget.item()
        if objeto.isSelected():
            self.ui.listWidget.clear(objeto)
        else:
            return 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador_2 = Lanzador()
    lanzador_2.show()
    sys.exit(app.exec())
