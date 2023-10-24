import sys
from trabajo_num import *


class Lanzador(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_sumar.clicked.connect(self.sumar_num)

    def sumar_num(self):
        if self.ui.lineEdit_primer_numero.text() != 0:
            a = int(self.ui.lineEdit_primer_numero.text())
        else:
            a = 0
        if self.ui.lineEdit_seg_numero.text() != 0:
            b = int(self.ui.lineEdit_seg_numero.text())
        else:
            b = 0
        sum = a + b
        return self.ui.label_resultado.setText("suma: " + str(sum))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lan = Lanzador()
    lan.show()
    sys.exit(app.exec())
