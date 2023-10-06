import sys
from vent_limp import Ui_Dialog, QtWidgets


class Lanzador(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = Lanzador()
    mi_app.show()
    sys.exit(app.exec_())

