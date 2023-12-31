from tabla import *
import sys
from PyQt5 import QtSql


def crear_coneccion():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setDatabaseName('sistema_nominas')
    db.setUserName('postgres')
    db.setPassword("r3yni3r2020@gmail.com")
    print(db.drivers())
    db.open()

    print(db.lastError().text())
    if db.open():
        print("conexion correcta")
        return True
    else:
        print("conexion incorrecta")
        return False


class Lanzador(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable('productos')
        self.model.setEditStrategy(QtSql.QSqlTableModel.EditStrategy.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    if not crear_coneccion():
        sys.exit(1)
    lan = Lanzador()
    lan.show()
    sys.exit(app.exec())
