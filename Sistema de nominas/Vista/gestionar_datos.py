import datetime

from conexion_db_gestion import *
from Vista.UI.gestionar import *
import sys


class GestionarDatos(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)

        self.datos_total = RegistroDatos()

        #                VINCULADOS
        self.validar_formulario()
        self.mostrar_trab_vin()
        self.act_list_proy_vin()
        self.ui.pushButton_insertar_vin.clicked.connect(self.insertar_trab_vin)
        self.ui.pushButton_eliminar_vin.clicked.connect(self.borrar_vin)
        self.ui.pushButton_actualizar_vin.clicked.connect(self.actualizar_vin)
        self.ui.tableWidget_vin.itemClicked.connect(self.rellenar_form_vin)
        self.ui.pushButton_act_proy_list.clicked.connect(self.act_list_proy_vin)
    #   PROYECTOS
        self.mostrar_proyecto()
        self.ui.pushButton_insertar_proy.clicked.connect(self.inertar_proy)
        self.ui.pushButton_eliminar_proy.clicked.connect(self.eliminar_proy)
        self.ui.tableWidget_proy.itemClicked.connect(self.llenar_form_proy)
        self.ui.pushButton_actualizar_proy.clicked.connect(self.actualizar_proy)

    def validar_formulario(self):
        expre = QtCore.QRegExp('^[^0-9]*$')
        valid = QtGui.QRegExpValidator(expre)
        self.ui.lineEdit_nombre_vin.setValidator(valid)
        self.ui.lineEdit_nombre_n_vin.setValidator(valid)
        self.ui.lineEdit_nombre_pory.setValidator(valid)
        self.ui.lineEdit_cliente.setValidator(valid)

    def rellenar_form_vin(self):
        try:
            fila = self.ui.tableWidget_vin.currentRow()
            if fila != -1:
                nombre = self.ui.tableWidget_vin.item(fila, 1).text()
                edad = self.ui.tableWidget_vin.item(fila, 3).text()
                # fech_na = self.ui.tableWidget_vin.item(fila, 4).text()
                niv_pro = self.ui.tableWidget_vin.item(fila, 5).text()
                proy_vin = self.ui.tableWidget_vin.item(fila, 6).text()
                rol_proy = self.ui.tableWidget_vin.item(fila, 7).text()
                plan_cump = self.ui.tableWidget_vin.item(fila, 8).text()
                plan_real = self.ui.tableWidget_vin.item(fila, 9).text()

                self.ui.lineEdit_nombre_vin.setText(nombre)
                self.ui.spinBox_edad.setValue(int(edad))
                self.retornar_sexo()
                # self.ui.dateEdit_fecha_naci = fech_na
                self.ui.comboBox_niv_pro.setCurrentText(niv_pro)
                self.ui.comboBox_pro_vin.setCurrentText(proy_vin)
                self.ui.comboBox_rol.setCurrentText(rol_proy)
                self.ui.spinBox_plan_cump.setValue(int(plan_cump))
                self.ui.spinBox_plan_real.setValue(int(plan_real))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def mostrar_trab_vin(self):
        datos = self.datos_total.buscar_trab_vin()
        i = len(datos)
        self.ui.tableWidget_vin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_vin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_vin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_vin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_vin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_vin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_vin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_vin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_vin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget_vin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_vin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(row[9])))
            if row[5] == "profesional":
                a = 80
            elif row[5] == "tecnico medio":
                a = 60
            else:
                a = 40

            if int(row[9]) > 100:
                b = int(row[9]) * 25.0
            elif 100 >= int(row[9]) >= 95:
                b = int(row[9]) * 21.5
            elif 94 >= int(row[9]) >= 80:
                b = int(row[9]) * 18.5
            else:
                b = int(row[9]) * 15.0

            salario = (int(row[9]) * b + a)
            self.ui.tableWidget_vin.setItem(table_row, 10, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def comprobar_sex(self):
        if self.ui.radioButton_Femenino.isChecked():
            sexo = 'F'
        else:
            sexo = 'M'

        return sexo

    def retornar_sexo(self):
        ind = self.ui.tableWidget_vin.currentRow()
        if self.ui.tableWidget_vin.item(ind, 2).text() == 'M':
            self.ui.radioButton_masculino.setChecked(True)
            self.ui.radioButton_Femenino.setChecked(False)
        else:
            self.ui.radioButton_Femenino.setChecked(True)
            self.ui.radioButton_masculino.setChecked(False)

    def act_list_proy_vin(self):
        datos = self.datos_total.buscar_pro()
        self.ui.comboBox_pro_vin.clear()
        self.ui.comboBox_pro_vin.addItem('')
        for row in datos:
            self.ui.comboBox_pro_vin.addItem(str(row[1]))

    def devolver_id_proy(self):
        datos = self.datos_total.buscar_pro()
        for row in datos:
            if self.ui.comboBox_pro_vin.currentText() == str(row[1]):
                return int(row[0])
            else:
                return 'null'

    def comp_trab_vin(self):
        datos = self.datos_total.buscar_trab_vin()
        a = 0
        for row in datos:
            if str(row[1]).upper() == self.ui.lineEdit_nombre_vin.text().upper():
                a = 1
        return a

    def insertar_trab_vin(self):
        try:
            nombre = self.ui.lineEdit_nombre_vin.text()
            edad = self.ui.spinBox_edad.value()
            sexo = self.comprobar_sex()
            fecha_naci = self.ui.dateEdit_fecha_naci.text()
            nivel_pro = self.ui.comboBox_niv_pro.currentText()
            pro_vin = self.devolver_id_proy()
            rol_pro = self.ui.comboBox_rol.currentText()
            plan_cump = self.ui.spinBox_plan_cump.value()
            plan_real = self.ui.spinBox_plan_real.value()
            if self.comp_trab_vin() == 1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Ya existe un trabajador con ese nombre'))
            else:
                self.datos_total.insertar_vin(nombre, sexo, edad, fecha_naci, nivel_pro,
                                              pro_vin, rol_pro, plan_cump, plan_real)
                self.ui.lineEdit_nombre_vin.clear()
                self.ui.spinBox_edad.setValue(0)
                self.ui.comboBox_niv_pro.setCurrentIndex(0)
                self.ui.comboBox_rol.setCurrentIndex(0)
                self.ui.spinBox_plan_cump.setValue(0)
                self.ui.spinBox_plan_real.setValue(0)
                self.mostrar_trab_vin()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def actualizar_vin(self):
        try:
            ind = self.ui.tableWidget_vin.currentRow()
            if ind == -1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
            ide = self.ui.tableWidget_vin.item(ind, 0).text()
            ide_n = int(ide)
            nombre = self.ui.lineEdit_nombre_vin.text()
            edad = self.ui.spinBox_edad.value()
            sexo = self.comprobar_sex()
            fecha_naci = self.ui.dateEdit_fecha_naci.text()
            nivel_pro = self.ui.comboBox_niv_pro.currentText()
            pro_vin = self.devolver_id_proy()
            rol_pro = self.ui.comboBox_rol.currentText()
            plan_cump = self.ui.spinBox_plan_cump.value()
            plan_real = self.ui.spinBox_plan_real.value()
            act = self.datos_total.act_trab_vin(nombre, edad, sexo, fecha_naci, nivel_pro, pro_vin, rol_pro,
                                                plan_cump, plan_real, ide_n)
            if act == 1:
                self.ui.lineEdit_nombre_vin.clear()
                self.ui.spinBox_edad.setValue(0)
                self.ui.comboBox_niv_pro.setCurrentIndex(0)
                self.ui.comboBox_rol.setCurrentIndex(0)
                self.ui.spinBox_plan_cump.setValue(0)
                self.ui.spinBox_plan_real.setValue(0)
                self.mostrar_trab_vin()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def borrar_vin(self):
        row = self.ui.tableWidget_vin.currentRow()
        try:
            if row != -1:
                ide = self.ui.tableWidget_vin.item(row, 0).text()
                a = self.datos_total.eliminar_vin(int(ide))
                if a == 1:
                    self.mostrar_trab_vin()
            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    #       TRABAJADORES_NO_VIN
    #       PROYECTOS

    def llenar_form_proy(self):
        try:
            fila = self.ui.tableWidget_proy.currentRow()
            if fila != -1:
                nombre = self.ui.tableWidget_proy.item(fila, 1).text()
                cliente = self.ui.tableWidget_proy.item(fila, 2).text()
                costo = self.ui.tableWidget_proy.item(fila, 3).text()
                # fech_ini = self.ui.tableWidget_proy.item(fila, 4).text()
                # fech_culm = self.ui.tableWidget_proy.item(fila, 5).text()
                por_culm = self.ui.tableWidget_proy.item(fila, 6).text()

                self.ui.lineEdit_nombre_pory.setText(nombre)
                self.ui.lineEdit_cliente.setText(cliente)
                self.ui.doubleSpinBox_costo.setValue(float(costo))
                # self.ui.dateEdit_fecha_ini = fech_ini
                # self.ui.dateEdit_fecha_culm = fech_culm
                self.ui.doubleSpinBox_porci_culm.setValue(float(por_culm))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def mostrar_proyecto(self):
        datos = self.datos_total.buscar_pro()
        i = len(datos)
        self.ui.tableWidget_proy.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_proy.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_proy.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_proy.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_proy.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_proy.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_proy.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_proy.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            table_row += 1

    def comp_proy(self):
        datos = self.datos_total.buscar_pro()
        a = 0
        for row in datos:
            if str(row[1]).upper() == self.ui.lineEdit_nombre_pory.text().upper():
                a = 1
        return a

    def inertar_proy(self):
        try:
            nombre = self.ui.lineEdit_nombre_pory.text()
            cliente = self.ui.lineEdit_cliente.text()
            costo = self.ui.doubleSpinBox_costo.value()
            fech_ini = self.ui.dateEdit_fecha_ini.text()
            fech_culm = self.ui.dateEdit_fecha_culm.text()
            por_culm = self.ui.doubleSpinBox_porci_culm.value()
            if self.comp_proy() == 1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Ya existe un proyecto con ese nombre'))
            else:
                self.datos_total.insertar_proy(nombre, cliente, costo, fech_ini, fech_culm, por_culm)
            self.ui.lineEdit_nombre_pory.clear()
            self.ui.lineEdit_cliente.clear()
            self.ui.doubleSpinBox_costo.setValue(0)
            self.ui.dateEdit_fecha_ini.setDate(datetime.date(2000, 1, 1))
            self.ui.dateEdit_fecha_culm.setDate(datetime.date(2000, 1, 1))
            self.ui.doubleSpinBox_porci_culm.setValue(0)
            self.mostrar_proyecto()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def eliminar_proy(self):
        row = self.ui.tableWidget_proy.currentRow()
        try:
            if row != -1:
                ide = self.ui.tableWidget_proy.item(row, 0).text()
                a = self.datos_total.eliminar_proy(int(ide))
                if a == 1:
                    self.mostrar_proyecto()
            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def actualizar_proy(self):
        try:
            ind = self.ui.tableWidget_proy.currentRow()
            if ind == -1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
            ide = self.ui.tableWidget_proy.item(ind, 0).text()
            ide_n = int(ide)
            nombre = self.ui.lineEdit_nombre_pory.text()
            cliente = self.ui.lineEdit_cliente.text()
            costo = self.ui.doubleSpinBox_costo.value()
            fech_ini = self.ui.dateEdit_fecha_ini.text()
            fech_culm = self.ui.dateEdit_fecha_culm.text()
            por_culm = self.ui.doubleSpinBox_porci_culm.value()

            act = self.datos_total.actualizar_proy(nombre, cliente, costo, fech_ini, fech_culm, por_culm, ide_n)
            if act == 1:
                self.ui.lineEdit_nombre_pory.clear()
                self.ui.lineEdit_cliente.clear()
                self.ui.doubleSpinBox_costo.setValue(0)
                self.ui.dateEdit_fecha_ini.setDate(datetime.date(2000, 1, 1))
                self.ui.dateEdit_fecha_culm.setDate(datetime.date(2000, 1, 1))
                self.ui.doubleSpinBox_porci_culm.setValue(0)
                self.mostrar_proyecto()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sas = GestionarDatos()
    sas.show()
    sys.exit(app.exec())
