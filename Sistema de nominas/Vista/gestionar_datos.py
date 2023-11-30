from conexion_db_gestion import *
from Vista.UI.gestionar import *
import time


class GestionarDatos(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)

        self.datos_total = RegistroDatos()

    def calcular_salario(self):
        if self.ui.comboBox_niv_pro.textActivated == "profesional":
            a = 80
        elif self.ui.comboBox_niv_pro.textActivated == "tecnico medio":
            a = 60
        else:
            a = 40

        if self.ui.spinBox_plan_real.text() > 100:
            b = 25.0
        elif (self.ui.spinBox_plan_real.text() <= 100) and (self.ui.spinBox_plan_real.text() >= 95):
            b = 21.5
        elif (self.ui.spinBox_plan_real.text() <= 94) and (self.ui.spinBox_plan_real.text() >= 80):
            b = 18.5
        else:
            b = 15.0

        salario = int(self.ui.spinBox_plan_real.text() * b + a)
        return salario

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
            self.ui.tableWidget_vin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.ui.tableWidget_vin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.ui.tableWidget_vin.setItem(table_row, 10, QtWidgets.QTableWidgetItem(self.calcular_salario()))
            table_row += 1

    def comprobar_sex(self):
        if self.ui.radioButton_Femenino.isChecked():
            sexo = 'F'
        else:
            sexo = 'M'

        return sexo

    def act_list_proy_vin(self):
        datos = self.datos_total.buscar_pro()
        for row in datos:
            self.ui.comboBox_pro_vin.addItem(row[0])

    def insertar_trab_vin(self):
        nombre = self.ui.lineEdit_nombre_vin.text()
        sexo = self.comprobar_sex()
        edad = self.ui.spinBox_edad.value()
        fecha_naci = self.ui.dateEdit_fecha_naci.text()
        nivel_pro = self.ui.comboBox_niv_pro.currentText()
        pro_vin = self.ui.comboBox_pro_vin.currentText()
        rol_pro = self.ui.comboBox_rol.currentText()
        plan_cump = self.ui.spinBox_plan_cump.value()
        plan_real = self.ui.spinBox_plan_real.value()

        self.datos_total.insertar_vin(nombre, sexo, edad, fecha_naci, nivel_pro, pro_vin, rol_pro, plan_cump, plan_real)
        self.ui.lineEdit_nombre_vin.clear()
        self.ui.spinBox_edad.clear()
        self.ui.dateEdit_fecha_naci.clear()
        self.ui.comboBox_niv_pro.setCurrentIndex(0)
        self.ui.comboBox_rol.setCurrentIndex(0)
        self.ui.spinBox_plan_cump.clear()
        self.ui.spinBox_plan_real.clear()

    def extraer_id(self):
        row = self.ui.tableWidget_vin.currentRow()
        return row[0]
