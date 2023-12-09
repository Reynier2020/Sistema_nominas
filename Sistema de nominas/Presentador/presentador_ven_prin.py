from Presentador.presentador_gestion import PresentadorGest
from Vista.ventana_prin import *
import sys
from Presentador.presentador_porcentaje import PresentadorPor


class PresentadorPrin:

    def iniciar_ven_prin(self):
        app = QtWidgets.QApplication(sys.argv)
        self.prin = VentanaPrin(self)
        self.prin.show()
        app.exec()

    def iniciar_gestion(self):
        gest = PresentadorGest()
        gest.iniciar()

    def iniciar_por(self):
        por = PresentadorPor()
        por.iniciar()
