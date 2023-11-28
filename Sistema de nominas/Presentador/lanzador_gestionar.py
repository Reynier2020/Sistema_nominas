from Vista.UI.gestionar import *


class LanzadorGest(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)

