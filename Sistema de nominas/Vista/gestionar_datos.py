import datetime
from Vista.conexion_db_gestion import *
from Vista.UI.gestionar import *


class GestionarDatos(QtWidgets.QWidget):
    def __init__(self, present):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_gestionar_ui()
        self.ui.setupUi(self)
        self.present = present
        self.datos_total = RegistroDatos()
        self.ui.pushButton_aceptar.clicked.connect(quit)

        #                VINCULADOS
        self.ui.pushButton_insertar_vin.setDisabled(True)
        self.ui.pushButton_actualizar_vin.setDisabled(True)
        self.validar_formulario()
        self.ui.lineEdit_nombre_vin.textChanged.connect(self.validar_controles_vin)
        self.mostrar_trab_vin()
        self.act_list_proy_vin()
        self.ui.pushButton_insertar_vin.clicked.connect(self.insertar_trab_vin)
        self.ui.pushButton_eliminar_vin.clicked.connect(self.borrar_vin)
        self.ui.pushButton_actualizar_vin.clicked.connect(self.actualizar_vin)
        self.ui.tableWidget_vin.itemClicked.connect(self.rellenar_form_vin)
        self.ui.pushButton_act_proy_list.clicked.connect(self.act_list_proy_vin)
    #   NO_VINCULADOS
        self.ui.pushButton_insertar_n_vin.setDisabled(True)
        self.ui.pushButton_actualizar_n_vin.setDisabled(True)
        self.ui.lineEdit_nombre_n_vin.textChanged.connect(self.validar_controles_no_vin)
        self.mostrar_trab_no_vin()
        self.ui.pushButton_insertar_n_vin.clicked.connect(self.insertar_no_vin)
        self.ui.tableWidget_no_vin.itemClicked.connect(self.llenar_form_no_vin)
        self.ui.pushButton_actualizar_n_vin.clicked.connect(self.actualizar_no_vin)
        self.ui.pushButton_eliminar_n_vin.clicked.connect(self.eliminar_no_vin)
    #   PROYECTOS
        self.ui.pushButton_insertar_proy.setDisabled(True)
        self.ui.pushButton_actualizar_proy.setDisabled(True)
        self.mostrar_proyecto()
        self.ui.lineEdit_nombre_pory.textChanged.connect(self.validar_controles_proy)
        self.ui.lineEdit_cliente.textChanged.connect(self.validar_controles_proy)
        self.ui.pushButton_insertar_proy.clicked.connect(self.inertar_proy)
        self.ui.pushButton_eliminar_proy.clicked.connect(self.eliminar_proy)
        self.ui.tableWidget_proy.itemClicked.connect(self.llenar_form_proy)
        self.ui.pushButton_actualizar_proy.clicked.connect(self.actualizar_proy)

    def validar_formulario(self):
        expre = QtCore.QRegExp('^[^0-9 ]*$')
        valid = QtGui.QRegExpValidator(expre)
        self.ui.lineEdit_nombre_vin.setValidator(valid)
        self.ui.lineEdit_nombre_n_vin.setValidator(valid)
        self.ui.lineEdit_nombre_pory.setValidator(valid)
        self.ui.lineEdit_cliente.setValidator(valid)

    def validar_controles_vin(self):
        if len(self.ui.lineEdit_nombre_vin.text()) == 0:
            self.ui.pushButton_insertar_vin.setDisabled(True)
            self.ui.pushButton_actualizar_vin.setDisabled(True)
        else:
            self.ui.pushButton_insertar_vin.setDisabled(False)
            self.ui.pushButton_actualizar_vin.setDisabled(False)

    def rellenar_form_vin(self):
        try:
            fila = self.ui.tableWidget_vin.currentRow()
            if fila != -1:
                nombre = self.ui.tableWidget_vin.item(fila, 1).text()
                edad = self.ui.tableWidget_vin.item(fila, 3).text()
                fech_na = self.ui.tableWidget_vin.item(fila, 4).text().split('-')
                niv_pro = self.ui.tableWidget_vin.item(fila, 5).text()
                proy_vin = self.ui.tableWidget_vin.item(fila, 6).text()
                rol_proy = self.ui.tableWidget_vin.item(fila, 7).text()
                plan_cump = self.ui.tableWidget_vin.item(fila, 8).text()
                plan_real = self.ui.tableWidget_vin.item(fila, 9).text()

                self.ui.lineEdit_nombre_vin.setText(nombre)
                self.ui.spinBox_edad.setValue(int(edad))
                self.retornar_sexo()
                self.ui.dateEdit_fecha_naci.setDate(datetime.date(int(fech_na[0]), int(fech_na[1]), int(fech_na[2])))
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
                    self.ui.lineEdit_nombre_vin.setFocus()
            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    #       TRABAJADORES_NO_VIN
    def validar_controles_no_vin(self):
        if len(self.ui.lineEdit_nombre_n_vin.text()) == 0:
            self.ui.pushButton_insertar_n_vin.setDisabled(True)
            self.ui.pushButton_actualizar_n_vin.setDisabled(True)
        else:
            self.ui.pushButton_insertar_n_vin.setDisabled(False)
            self.ui.pushButton_actualizar_n_vin.setDisabled(False)

    def mostrar_trab_no_vin(self):
        datos = self.datos_total.buscar_no_vin()
        i = len(datos)
        self.ui.tableWidget_no_vin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_no_vin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_no_vin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_no_vin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_no_vin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_no_vin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_no_vin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_no_vin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_no_vin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tableWidget_no_vin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            if row[5] == "profesional":
                a = 80
            elif row[5] == "tecnico medio":
                a = 60
            else:
                a = 40

            if row[6] == "jefe de departamento":
                b = 120
            else:
                b = 200

            salario = int(((int(row[8]) * 12.5 + b) - (5 * int(row[7]))) + a)
            self.ui.tableWidget_no_vin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def comprobar_no_vin(self):
        datos = self.datos_total.buscar_no_vin()
        a = 0
        for row in datos:
            if str(row[1]).upper() == self.ui.lineEdit_nombre_n_vin.text().upper():
                a = 1
        return a

    def retornar_sexo_no_vin(self):
        ind = self.ui.tableWidget_no_vin.currentRow()
        if self.ui.tableWidget_no_vin.item(ind, 2).text() == 'M':
            self.ui.radioButton_masculino_2.setChecked(True)
            self.ui.radioButton_Femenino_2.setChecked(False)
        else:
            self.ui.radioButton_Femenino_2.setChecked(True)
            self.ui.radioButton_masculino_2.setChecked(False)

    def llenar_form_no_vin(self):
        try:
            fila = self.ui.tableWidget_no_vin.currentRow()
            if fila != -1:
                nombre = self.ui.tableWidget_no_vin.item(fila, 1).text()
                edad = self.ui.tableWidget_no_vin.item(fila, 3).text()
                fech_na = self.ui.tableWidget_no_vin.item(fila, 4).text().split('-')
                niv_pro = self.ui.tableWidget_no_vin.item(fila, 5).text()
                resp = self.ui.tableWidget_no_vin.item(fila, 6).text()
                lleg_tarde = self.ui.tableWidget_no_vin.item(fila, 7).text()
                horas_trab = self.ui.tableWidget_no_vin.item(fila, 8).text()

                self.ui.lineEdit_nombre_n_vin.setText(nombre)
                self.ui.spinBox_edad_no_vin.setValue(int(edad))
                self.retornar_sexo_no_vin()
                self.ui.dateEdit_fecha_naci.setDate(datetime.date(int(fech_na[0]), int(fech_na[1]), int(fech_na[2])))
                self.ui.comboBox_niv_pro_no_vin.setCurrentText(niv_pro)
                self.ui.comboBox_resp.setCurrentText(resp)
                self.ui.spinBox_tarde.setValue(int(lleg_tarde))
                self.ui.spinBox_horas_tra.setValue(int(horas_trab))

        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def comprobar_sexo_no_vin(self):
        if self.ui.radioButton_Femenino_2.isChecked():
            sexo = 'F'
        else:
            sexo = 'M'

        return sexo

    def insertar_no_vin(self):
        try:
            nombre = self.ui.lineEdit_nombre_n_vin.text()
            edad = self.ui.spinBox_edad_no_vin.value()
            sexo = self.comprobar_sexo_no_vin()
            fecha_naci = self.ui.dateEdit_fecha_naci_no_vin.text()
            nivel_pro = self.ui.comboBox_niv_pro_no_vin.currentText()
            responsabilidad = self.ui.comboBox_resp.currentText()
            llegadas_tarde = self.ui.spinBox_tarde.value()
            horas_trabajadas = self.ui.spinBox_horas_tra.value()
            if self.comprobar_no_vin() == 1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Ya existe un trabajador con ese nombre'))
            else:
                self.datos_total.insetrar_no_vin(nombre, edad, sexo, fecha_naci, nivel_pro, responsabilidad,
                                                 llegadas_tarde, horas_trabajadas)
                self.ui.lineEdit_nombre_n_vin.clear()
                self.ui.spinBox_edad_no_vin.setValue(0)
                self.ui.comboBox_niv_pro_no_vin.setCurrentIndex(0)
                self.ui.comboBox_resp.setCurrentIndex(0)
                self.ui.spinBox_tarde.setValue(0)
                self.ui.spinBox_horas_tra.setValue(0)
                self.mostrar_trab_no_vin()
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def actualizar_no_vin(self):
        try:
            ind = self.ui.tableWidget_no_vin.currentRow()
            if ind == -1:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
            ide = self.ui.tableWidget_no_vin.item(ind, 0).text()
            ide_n = int(ide)
            nombre = self.ui.lineEdit_nombre_n_vin.text()
            edad = self.ui.spinBox_edad_no_vin.value()
            sexo = self.comprobar_sexo_no_vin()
            fecha_naci = self.ui.dateEdit_fecha_naci_no_vin.text()
            nivel_pro = self.ui.comboBox_niv_pro_no_vin.currentText()
            responsabilidad = self.ui.comboBox_resp.currentText()
            llegadas_tarde = self.ui.spinBox_tarde.value()
            horas_trabajadas = self.ui.spinBox_horas_tra.value()
            act = self.datos_total.actualizar_no_vin(nombre, edad, sexo, fecha_naci, nivel_pro,
                                                     responsabilidad, llegadas_tarde, horas_trabajadas, ide_n)
            if act == 1:
                self.ui.lineEdit_nombre_n_vin.clear()
                self.ui.spinBox_edad_no_vin.setValue(0)
                self.ui.comboBox_niv_pro_no_vin.setCurrentIndex(0)
                self.ui.comboBox_resp.setCurrentIndex(0)
                self.ui.spinBox_tarde.setValue(0)
                self.ui.spinBox_horas_tra.setValue(0)
                self.mostrar_trab_no_vin()

        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def eliminar_no_vin(self):
        row = self.ui.tableWidget_no_vin.currentRow()
        try:
            if row != -1:
                ide = self.ui.tableWidget_no_vin.item(row, 0).text()
                a = self.datos_total.eliminar_no_vin((int(ide)))
                if a == 1:
                    self.mostrar_trab_no_vin()
            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona algo antes de borrar'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    #       PROYECTOS

    def validar_controles_proy(self):
        if len(self.ui.lineEdit_nombre_pory.text()) == 0 or len(self.ui.lineEdit_cliente.text()) == 0:
            self.ui.pushButton_insertar_proy.setDisabled(True)
            self.ui.pushButton_actualizar_proy.setDisabled(True)
        else:
            self.ui.pushButton_insertar_proy.setDisabled(False)
            self.ui.pushButton_actualizar_proy.setDisabled(False)

    def llenar_form_proy(self):
        try:
            fila = self.ui.tableWidget_proy.currentRow()
            if fila != -1:
                nombre = self.ui.tableWidget_proy.item(fila, 1).text()
                cliente = self.ui.tableWidget_proy.item(fila, 2).text()
                costo = self.ui.tableWidget_proy.item(fila, 3).text()
                fech_ini = self.ui.tableWidget_proy.item(fila, 4).text().split('-')
                fech_culm = self.ui.tableWidget_proy.item(fila, 5).text().split('-')
                por_culm = self.ui.tableWidget_proy.item(fila, 6).text()

                self.ui.lineEdit_nombre_pory.setText(nombre)
                self.ui.lineEdit_cliente.setText(cliente)
                self.ui.doubleSpinBox_costo.setValue(float(costo))
                self.ui.dateEdit_fecha_ini.setDate(datetime.date(int(fech_ini[0]), int(fech_ini[1]), int(fech_ini[2])))
                self.ui.dateEdit_fecha_culm.setDate(datetime.date(int(fech_culm[0]),
                                                                  int(fech_culm[1]), int(fech_culm[2])))
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

