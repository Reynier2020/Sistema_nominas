from tabla import *
import sys
from PyQt5 import QtSql


def crear_coneccion():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setUserName('root')
    db.setPassword('r3yni3r2020@gmail.com')
    db.setDatabaseName('sistema_nominas')
    db.open()
    print(db.lastError().text())


class Lanzador(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("productos")
        self.model.setEditStrategy(QtSql.QSqlTableModel)
