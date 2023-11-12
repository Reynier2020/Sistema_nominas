import sys
from lista import *


class Lanzador(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_pais)
        self.ui.pushButton_eliminar.clicked.connect(self.eliminar)
        self.ui.pushButton_vaciar.clicked.connect(self.vaciar)
        self.ui.pushButton_editar.clicked.connect(self.editar)

    def add_pais(self):
        texto = self.ui.lineEdit_pais.text()
        if len(self.ui.lineEdit_pais.text()) == 0:
            return 0
        else:
            self.ui.listWidget.addItem(texto)
            self.ui.lineEdit_pais.clear()
            self.ui.lineEdit_pais.setFocus()

    def eliminar(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def vaciar(self):
        self.ui.listWidget.clear()

    def editar(self):
        row = self.ui.listWidget.currentRow()
        nuevo_texto, aceptar = QtWidgets.QInputDialog.getText(self, "Editar", "Escribe un texto:")
        if aceptar and len(nuevo_texto) != 0:
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row, str(nuevo_texto))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador_2 = Lanzador()
    lanzador_2.show()
    sys.exit(app.exec())
