from Vista.conexion_db_gestion import RegistroDatos
from Vista.UI.ventana import *


class VentanaPrin(QtWidgets.QMainWindow):
    def __init__(self, pre):
        self.pre = pre
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindo_principal()
        self.ui.setupUi(self)

        self.datos_totales = RegistroDatos()
        self.validar_formulario()
        self.mostrar_trab_vin_prin()
        self.mostrar_trab_no_vin_prin()
        self.mostrar_proyecto_prin()
        # CONEXIONES
        self.ui.actionAcerca_de.triggered.connect(self.ayuda)
        self.ui.actionSalir.triggered.connect(quit)
        self.ui.actionTotal_de_salarios_a_pagar.triggered.connect(self.total_salarios)
        self.ui.actionAbrir_Gest.triggered.connect(self.pre.iniciar_gestion)
        self.ui.actionPorciento_de_cumplimiento.triggered.connect(self.pre.iniciar_por)
        self.ui.lineEdit_busar_vin.textChanged.connect(self.buscar_al_vin)
        self.ui.pushButton_dep_no_vin.clicked.connect(self.despedir_no_vin)
        self.ui.pushButton_desp_vin.clicked.connect(self.despedir_vin)
        self.ui.lineEdit_no_vin.textChanged.connect(self.buscar_al_no)
        self.ui.lineEdit_proy.textChanged.connect(self.buscar_el_proy)
        self.ui.pushButton_refrsh_vin.clicked.connect(self.mostrar_trab_vin_prin)
        self.ui.pushButton_refresh_no.clicked.connect(self.mostrar_trab_no_vin_prin)
        self.ui.pushButton_refresh_proy.clicked.connect(self.mostrar_proyecto_prin)

    def validar_formulario(self):
        expre = QtCore.QRegExp('^[^0-9 ]*$')
        valid = QtGui.QRegExpValidator(expre)
        self.ui.lineEdit_busar_vin.setValidator(valid)
        self.ui.lineEdit_no_vin.setValidator(valid)
        self.ui.lineEdit_proy.setValidator(valid)

    def mostrar_trab_vin_prin(self):
        datos = self.datos_totales.buscar_trab_vin()
        i = len(datos)
        self.ui.tableWidget_vin_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_vin_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(row[9])))
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
            self.ui.tableWidget_vin_prin.setItem(table_row, 10, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def mostrar_trab_no_vin_prin(self):
        datos = self.datos_totales.buscar_no_vin()
        i = len(datos)
        self.ui.tableWidget_no_vin_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
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
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def mostrar_proyecto_prin(self):
        datos = self.datos_totales.buscar_pro()
        i = len(datos)
        self.ui.tableWidget_proy_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_proy_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_proy_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_proy_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            table_row += 1

    def buscar_al_vin(self):
        nombre = self.ui.lineEdit_busar_vin.text()
        datos = self.datos_totales.busca_al_trab_vin(nombre)
        i = len(datos)
        self.ui.tableWidget_vin_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_vin_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.ui.tableWidget_vin_prin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
            self.ui.tableWidget_vin_prin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(row[9])))
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
            self.ui.tableWidget_vin_prin.setItem(table_row, 10, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def buscar_al_no(self):
        nombre = self.ui.lineEdit_no_vin.text()
        datos = self.datos_totales.busca_al_trab_no_vin(nombre)
        i = len(datos)
        self.ui.tableWidget_no_vin_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[2])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 7, QtWidgets.QTableWidgetItem(str(row[7])))
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 8, QtWidgets.QTableWidgetItem(str(row[8])))
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
            self.ui.tableWidget_no_vin_prin.setItem(table_row, 9, QtWidgets.QTableWidgetItem(str(salario)))
            table_row += 1

    def buscar_el_proy(self):
        nombre = self.ui.lineEdit_proy.text()
        datos = self.datos_totales.busca_el_pro(nombre)
        i = len(datos)
        self.ui.tableWidget_proy_prin.setRowCount(i)
        table_row = 0
        for row in datos:
            self.ui.tableWidget_proy_prin.setItem(table_row, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_proy_prin.setItem(table_row, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_proy_prin.setItem(table_row, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 5, QtWidgets.QTableWidgetItem(str(row[5])))
            self.ui.tableWidget_proy_prin.setItem(table_row, 6, QtWidgets.QTableWidgetItem(str(row[6])))
            table_row += 1

    def despedir_vin(self):
        fila = self.ui.tableWidget_vin_prin.currentRow()
        try:
            if fila != -1:
                nombre = self.ui.tableWidget_vin_prin.item(fila, 1).text()
                sexo = self.ui.tableWidget_vin_prin.item(fila, 2).text()
                edad = self.ui.tableWidget_vin_prin.item(fila, 3).text()
                fech_na = self.ui.tableWidget_vin_prin.item(fila, 4).text()
                niv_pro = self.ui.tableWidget_vin_prin.item(fila, 5).text()
                proy_vin = self.ui.tableWidget_vin_prin.item(fila, 6).text()
                rol_proy = self.ui.tableWidget_vin_prin.item(fila, 7).text()
                plan_cump = self.ui.tableWidget_vin_prin.item(fila, 8).text()
                plan_real = self.ui.tableWidget_vin_prin.item(fila, 9).text()
                salario = self.ui.tableWidget_vin_prin.item(fila, 10).text()

                ide = self.ui.tableWidget_vin_prin.item(fila, 0).text()
                a = self.datos_totales.eliminar_vin(int(ide))
                if a == 1:
                    self.mostrar_trab_vin_prin()
                    self.ui.lineEdit_busar_vin.setFocus()
                    return (QtWidgets.QMessageBox.information(self, '!!!DESPEDIDO!!!', 'Se ha despedido a: nombre: {}\n'
                                                              'sexo: {}\nedad: {}\nfecha_nacimiento: {}\n'
                                                              'nivel_pro: {}\nproy_vin: {}\nrol: {}\n'
                                                              'plan_asig: {}\nplan_real: {}\n'
                                                              'salario: {}'.format(nombre, sexo, edad,
                                                                                   fech_na, niv_pro, proy_vin,
                                                                                   rol_proy, plan_cump,
                                                                                   plan_real, salario)))

            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona a alguien antes de despedirlo'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def despedir_no_vin(self):
        fila = self.ui.tableWidget_no_vin_prin.currentRow()
        try:
            if fila != -1:
                nombre = self.ui.tableWidget_no_vin_prin.item(fila, 1).text()
                sexo = self.ui.tableWidget_no_vin_prin.item(fila, 2).text()
                edad = self.ui.tableWidget_no_vin_prin.item(fila, 3).text()
                fech_na = self.ui.tableWidget_no_vin_prin.item(fila, 4).text()
                niv_pro = self.ui.tableWidget_no_vin_prin.item(fila, 5).text()
                resp = self.ui.tableWidget_no_vin_prin.item(fila, 6).text()
                lleg_tarde = self.ui.tableWidget_no_vin_prin.item(fila, 7).text()
                horas_trab = self.ui.tableWidget_no_vin_prin.item(fila, 8).text()
                salario = self.ui.tableWidget_no_vin_prin.item(fila, 9).text()

                ide = self.ui.tableWidget_no_vin_prin.item(fila, 0).text()
                a = self.datos_totales.eliminar_no_vin(int(ide))
                if a == 1:
                    self.mostrar_trab_no_vin_prin()
                    self.ui.lineEdit_no_vin.setFocus()
                    return (QtWidgets.QMessageBox.information(self, '!!!DESPEDIDO!!!', 'Se ha despedido a: nombre: {}\n'
                                                              'sexo: {}\nedad: {}\nfecha_nacimiento: {}\n'
                                                              'nivel_pro: {}\nresponsabilidad: {}\nllegadas_tarde: {}\n'
                                                              'horas_trab: {}\n'
                                                              'salario: {}'.format(nombre, sexo, edad, fech_na, niv_pro,
                                                                                   resp, lleg_tarde,
                                                                                   horas_trab, salario)))

            else:
                raise (QtWidgets.QMessageBox.critical(self, 'Error', 'Selecciona a alguien antes de despedirlo'))
        except Exception as error:
            return QtWidgets.QMessageBox.critical(self, 'Error', error.args[0])

    def sumatoria_salarios_vin(self):
        table_row = 0
        datos = self.datos_totales.buscar_trab_vin()
        datos_sal = self.ui.tableWidget_vin_prin.item(table_row, 10).text()
        salario_total_vin = 0
        for row in datos:
            salario_total_vin += float(datos_sal)
            table_row += 1
        return salario_total_vin

    def sumatoria_salarios_no_vin(self):
        table_row = 0
        datos = self.datos_totales.buscar_no_vin()
        datos_sal = self.ui.tableWidget_no_vin_prin.item(table_row, 9).text()
        salario_total_no = 0
        for row in datos:
            salario_total_no += float(datos_sal)
        return salario_total_no

    def total_salarios(self):
        total_vin = self.sumatoria_salarios_vin()
        total_no_vin = self.sumatoria_salarios_no_vin()
        total_salarios = float(total_vin) + float(total_no_vin)
        msg = QtWidgets.QMessageBox.information(self, "Salarios", "Total de salarios: {}".format(total_salarios))
        return msg

    def ayuda(self):
        msg = QtWidgets.QMessageBox.information(self, "Creado por:", "Alexai ------\nIdel--------\nReynier-------")
        return msg
