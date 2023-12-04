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
        self.ui.pushButton_insertar_vin.clicked.connect(self.insertar_trab_vin)
        self.ui.pushButton_eliminar_vin.clicked.connect(self.borrar_vin)
        self.ui.pushButton_actualizar_vin.clicked.connect(self.actualizar_vin)
        self.ui.tableWidget_vin.itemClicked.connect(self.rellenar_form_vin)
        self.ui.pushButton_act_proy_list.clicked.connect(self.act_list_proy_vin)

    def validar_formulario(self):
        expre = QtCore.QRegExp('^[^0-9][^#@+-&%_$^!]*$')
        valid = QtGui.QRegExpValidator(expre)
        self.ui.lineEdit_nombre_vin.setValidator(valid)

    def rellenar_form_vin(self):
        fila = self.ui.tableWidget_vin.currentRow()
        if fila != -1:
            nombre = self.ui.tableWidget_vin.item(fila, 1)
            edad = self.ui.tableWidget_vin.item(fila, 3)
            fech_na = self.ui.tableWidget_vin.item(fila, 4)
            niv_pro = self.ui.tableWidget_vin.item(fila, 5)
            proy_vin = self.ui.tableWidget_vin.item(fila, 6)
            rol_proy = self.ui.tableWidget_vin.item(fila, 7)
            plan_cump = self.ui.tableWidget_vin.item(fila, 8)
            plan_real = self.ui.tableWidget_vin.item(fila, 9)

            self.ui.lineEdit_nombre_vin = nombre
            self.ui.spinBox_edad = edad
            self.retornar_sexo()
            self.ui.dateEdit_fecha_naci = fech_na
            self.ui.comboBox_niv_pro = niv_pro
            self.ui.comboBox_pro_vin = proy_vin
            self.ui.comboBox_rol = rol_proy
            self.ui.spinBox_plan_cump = plan_cump
            self.ui.spinBox_plan_real = plan_real

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
        if self.ui.tableWidget_vin.item(ind, 2) == 'M':
            self.ui.radioButton_masculino.setChecked()
        else:
            self.ui.radioButton_Femenino.setChecked()

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
                self.ui.spinBox_edad.clear()
                self.ui.dateEdit_fecha_naci.clear()
                self.ui.comboBox_niv_pro.setCurrentIndex(0)
                self.ui.comboBox_rol.setCurrentIndex(0)
                self.ui.spinBox_plan_cump.clear()
                self.ui.spinBox_plan_real.clear()
                self.mostrar_trab_vin()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def extraer_id(self):
        row = self.ui.tableWidget_vin.currentRow()
        return str(row[0])

    def actualizar_vin(self):
        nombre = self.ui.lineEdit_nombre_vin.text()
        sexo = self.comprobar_sex()
        edad = self.ui.spinBox_edad.value()
        fecha_naci = self.ui.dateEdit_fecha_naci.text()
        nivel_pro = self.ui.comboBox_niv_pro.currentText()
        pro_vin = self.ui.comboBox_pro_vin.currentText()
        rol_pro = self.ui.comboBox_rol.currentText()
        plan_cump = self.ui.spinBox_plan_cump.value()
        plan_real = self.ui.spinBox_plan_real.value()

        act = self.datos_total.act_trab_vin(nombre, sexo, edad, fecha_naci, nivel_pro,
                                            pro_vin, rol_pro, plan_cump, plan_real, self.extraer_id)
        if act == 1:
            self.ui.lineEdit_nombre_vin.clear()
            self.ui.spinBox_edad.clear()
            self.ui.dateEdit_fecha_naci.clear()
            self.ui.comboBox_niv_pro.setCurrentIndex(0)
            self.ui.comboBox_rol.setCurrentIndex(0)
            self.ui.spinBox_plan_cump.clear()
            self.ui.spinBox_plan_real.clear()
            self.mostrar_trab_vin()
        else:
            raise (QtWidgets.QMessageBox.critical(self, 'Error', 'No se ha podido actualizar'))

    def borrar_vin(self):
        row = self.ui.tableWidget_vin.currentRow()
        a = self.datos_total.eliminar_vin(row[0])
        if a == 1:
            self.ui.tableWidget_vin.takeItem(row)
        else:
            raise Exception(QtWidgets.QMessageBox.critical(self, 'Error', 'Error al borrar'))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    sas = GestionarDatos()
    sas.show()
    sys.exit(app.exec())
