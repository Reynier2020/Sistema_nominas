from PyQt5 import QtWidgets
from conexion_db_gestion import *
from Vista.UI.gestionar import *
import time


class GestionarDatos(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)

        self.datos_total = RegistroDatos()

    def mostrar_trab_vin(self):
        datos = self.datos_total.buscar_trab_vin()
        i = len(datos)
        self.ui.tableWidget_vin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_vin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_vin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_vin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_vin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.ui.tableWidget_vin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.ui.tableWidget_vin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_vin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_vin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))



