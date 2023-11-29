from Vista.UI.gestionar import *
from PyQt5 import QtWidgets
import MySQLdb



class GestionarDatos(QtWidgets.QWidget):
    def __init__(self, presentador):
        self.__presentador = presentador
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)

    # VINCULADOS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
