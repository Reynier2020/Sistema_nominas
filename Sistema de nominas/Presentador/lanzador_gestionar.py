from Vista.UI.gestionar import *
import sys


class LanzadorGest(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador_gest = LanzadorGest()
    lanzador_gest.show()
    sys.exit(app.exec())

