import lanzador_gestionar
import lanzador_vent_prin
from PyQt5 import QtWidgets
import sys


class Lan:
    def __init__(self):
        self.gestion = lanzador_gestionar.LanzadorGest()

    def iniciar(self):
        appe = QtWidgets.QApplication(sys.argv)
        self.prin = lanzador_vent_prin.Lanzador()
        self.prin.show()
        appe.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lanzador = Lan()
    lanzador.iniciar()



