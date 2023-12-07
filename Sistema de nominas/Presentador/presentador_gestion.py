from Vista.gestionar_datos import GestionarDatos


class PresentadorGest:

    def iniciar(self):
        self.ges = GestionarDatos(self)
        self.ges.show()
