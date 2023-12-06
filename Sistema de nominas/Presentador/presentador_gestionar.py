from Vista.gestionar_datos import GestionarDatos


class PresentaorGestionar:
    def __init__(self):
        self.lan = GestionarDatos()

    def iniciar(self):
        self.lan.show()
