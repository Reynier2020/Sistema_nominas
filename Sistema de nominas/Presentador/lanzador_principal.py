import lanzador_gestionar
import lanzador_vent_prin
from PyQt5 import QtWidgets
import sys


class Lan:
    def __init__(self):
        self.gestion = lanzador_gestionar.LanzadorGest()

    def iniciar(self):
        appe = QtWidgets.QApplication(sys.argv)
        self.prin = lanzador_vent_prin.Lanzador(self)
        self.prin.show()
        appe.exec()



