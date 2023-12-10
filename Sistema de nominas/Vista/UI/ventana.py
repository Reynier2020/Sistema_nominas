# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindo_principal(object):
    def setupUi(self, MainWindo_principal):
        MainWindo_principal.setObjectName("MainWindo_principal")
        MainWindo_principal.resize(639, 480)
        MainWindo_principal.setMinimumSize(QtCore.QSize(404, 350))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        MainWindo_principal.setFont(font)
        MainWindo_principal.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/thumbs-up.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindo_principal.setWindowIcon(icon)
        MainWindo_principal.setStyleSheet("QLineEdit{\n"
"border:1px solid #167;}\n"
"\n"
"\n"
"")
        MainWindo_principal.setIconSize(QtCore.QSize(30, 23))
        self.centralwidget = QtWidgets.QWidget(MainWindo_principal)
        self.centralwidget.setStyleSheet("border-radus:10px;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(212, 13, 46);\n"
"font:12pt \"Tw Cen MT Condensed\";\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setContentsMargins(0, 0, 3, 0)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame_9)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_11.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_9)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 9)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget_principal = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget_principal.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_principal.setFont(font)
        self.tabWidget_principal.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_principal.setAutoFillBackground(False)
        self.tabWidget_principal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.tabWidget_principal.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_principal.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_principal.setUsesScrollButtons(True)
        self.tabWidget_principal.setTabsClosable(False)
        self.tabWidget_principal.setMovable(False)
        self.tabWidget_principal.setTabBarAutoHide(False)
        self.tabWidget_principal.setObjectName("tabWidget_principal")
        self.tab_vinculados = QtWidgets.QWidget()
        self.tab_vinculados.setObjectName("tab_vinculados")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_vinculados)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_busar_vin = QtWidgets.QLineEdit(self.tab_vinculados)
        self.lineEdit_busar_vin.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_busar_vin.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_busar_vin.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_busar_vin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid  rgb(248, 16, 51);")
        self.lineEdit_busar_vin.setText("")
        self.lineEdit_busar_vin.setCursorPosition(0)
        self.lineEdit_busar_vin.setDragEnabled(False)
        self.lineEdit_busar_vin.setReadOnly(False)
        self.lineEdit_busar_vin.setClearButtonEnabled(True)
        self.lineEdit_busar_vin.setObjectName("lineEdit_busar_vin")
        self.horizontalLayout_6.addWidget(self.lineEdit_busar_vin)
        self.pushButton_desp_vin = QtWidgets.QPushButton(self.tab_vinculados)
        self.pushButton_desp_vin.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_desp_vin.setMaximumSize(QtCore.QSize(38, 22))
        self.pushButton_desp_vin.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}")
        self.pushButton_desp_vin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/user-x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_desp_vin.setIcon(icon1)
        self.pushButton_desp_vin.setIconSize(QtCore.QSize(30, 23))
        self.pushButton_desp_vin.setObjectName("pushButton_desp_vin")
        self.horizontalLayout_6.addWidget(self.pushButton_desp_vin)
        self.pushButton_refrsh_vin = QtWidgets.QPushButton(self.tab_vinculados)
        self.pushButton_refrsh_vin.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_refrsh_vin.setMaximumSize(QtCore.QSize(38, 22))
        self.pushButton_refrsh_vin.setAutoFillBackground(False)
        self.pushButton_refrsh_vin.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}\n"
"")
        self.pushButton_refrsh_vin.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refrsh_vin.setIcon(icon2)
        self.pushButton_refrsh_vin.setIconSize(QtCore.QSize(25, 20))
        self.pushButton_refrsh_vin.setCheckable(False)
        self.pushButton_refrsh_vin.setChecked(False)
        self.pushButton_refrsh_vin.setAutoDefault(False)
        self.pushButton_refrsh_vin.setDefault(False)
        self.pushButton_refrsh_vin.setFlat(False)
        self.pushButton_refrsh_vin.setObjectName("pushButton_refrsh_vin")
        self.horizontalLayout_6.addWidget(self.pushButton_refrsh_vin)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.tableWidget_vin_prin = QtWidgets.QTableWidget(self.tab_vinculados)
        self.tableWidget_vin_prin.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget_vin_prin.setMaximumSize(QtCore.QSize(16777215, 9999999))
        self.tableWidget_vin_prin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.tableWidget_vin_prin.setObjectName("tableWidget_vin_prin")
        self.tableWidget_vin_prin.setColumnCount(11)
        self.tableWidget_vin_prin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_vin_prin.setHorizontalHeaderItem(10, item)
        self.verticalLayout_3.addWidget(self.tableWidget_vin_prin)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.tabWidget_principal.addTab(self.tab_vinculados, "")
        self.tab_no_vinculado = QtWidgets.QWidget()
        self.tab_no_vinculado.setObjectName("tab_no_vinculado")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_no_vinculado)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_no_vin = QtWidgets.QLineEdit(self.tab_no_vinculado)
        self.lineEdit_no_vin.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_no_vin.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_no_vin.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_no_vin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid  rgb(248, 16, 51);")
        self.lineEdit_no_vin.setText("")
        self.lineEdit_no_vin.setCursorPosition(0)
        self.lineEdit_no_vin.setDragEnabled(False)
        self.lineEdit_no_vin.setReadOnly(False)
        self.lineEdit_no_vin.setClearButtonEnabled(True)
        self.lineEdit_no_vin.setObjectName("lineEdit_no_vin")
        self.horizontalLayout_2.addWidget(self.lineEdit_no_vin)
        self.pushButton_dep_no_vin = QtWidgets.QPushButton(self.tab_no_vinculado)
        self.pushButton_dep_no_vin.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_dep_no_vin.setMaximumSize(QtCore.QSize(50, 22))
        self.pushButton_dep_no_vin.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}")
        self.pushButton_dep_no_vin.setText("")
        self.pushButton_dep_no_vin.setIcon(icon1)
        self.pushButton_dep_no_vin.setIconSize(QtCore.QSize(30, 23))
        self.pushButton_dep_no_vin.setObjectName("pushButton_dep_no_vin")
        self.horizontalLayout_2.addWidget(self.pushButton_dep_no_vin)
        self.pushButton_refresh_no = QtWidgets.QPushButton(self.tab_no_vinculado)
        self.pushButton_refresh_no.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_refresh_no.setMaximumSize(QtCore.QSize(38, 22))
        self.pushButton_refresh_no.setAutoFillBackground(False)
        self.pushButton_refresh_no.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}\n"
"")
        self.pushButton_refresh_no.setText("")
        self.pushButton_refresh_no.setIcon(icon2)
        self.pushButton_refresh_no.setIconSize(QtCore.QSize(25, 20))
        self.pushButton_refresh_no.setCheckable(False)
        self.pushButton_refresh_no.setChecked(False)
        self.pushButton_refresh_no.setAutoDefault(False)
        self.pushButton_refresh_no.setDefault(False)
        self.pushButton_refresh_no.setFlat(False)
        self.pushButton_refresh_no.setObjectName("pushButton_refresh_no")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh_no)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.tableWidget_no_vin_prin = QtWidgets.QTableWidget(self.tab_no_vinculado)
        self.tableWidget_no_vin_prin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_no_vin_prin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.tableWidget_no_vin_prin.setObjectName("tableWidget_no_vin_prin")
        self.tableWidget_no_vin_prin.setColumnCount(10)
        self.tableWidget_no_vin_prin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_no_vin_prin.setHorizontalHeaderItem(9, item)
        self.verticalLayout_4.addWidget(self.tableWidget_no_vin_prin)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.tabWidget_principal.addTab(self.tab_no_vinculado, "")
        self.tab_proyectos = QtWidgets.QWidget()
        self.tab_proyectos.setObjectName("tab_proyectos")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_proyectos)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_proy = QtWidgets.QLineEdit(self.tab_proyectos)
        self.lineEdit_proy.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEdit_proy.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_proy.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_proy.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px solid  rgb(248, 16, 51);")
        self.lineEdit_proy.setText("")
        self.lineEdit_proy.setCursorPosition(0)
        self.lineEdit_proy.setDragEnabled(False)
        self.lineEdit_proy.setReadOnly(False)
        self.lineEdit_proy.setClearButtonEnabled(True)
        self.lineEdit_proy.setObjectName("lineEdit_proy")
        self.horizontalLayout_5.addWidget(self.lineEdit_proy)
        self.pushButton_ordenar_pro = QtWidgets.QPushButton(self.tab_proyectos)
        self.pushButton_ordenar_pro.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_ordenar_pro.setMaximumSize(QtCore.QSize(50, 22))
        self.pushButton_ordenar_pro.setAutoFillBackground(False)
        self.pushButton_ordenar_pro.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}")
        self.pushButton_ordenar_pro.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ordenar_pro.setIcon(icon3)
        self.pushButton_ordenar_pro.setIconSize(QtCore.QSize(30, 25))
        self.pushButton_ordenar_pro.setCheckable(False)
        self.pushButton_ordenar_pro.setObjectName("pushButton_ordenar_pro")
        self.horizontalLayout_5.addWidget(self.pushButton_ordenar_pro)
        self.pushButton_refresh_proy = QtWidgets.QPushButton(self.tab_proyectos)
        self.pushButton_refresh_proy.setMinimumSize(QtCore.QSize(35, 22))
        self.pushButton_refresh_proy.setMaximumSize(QtCore.QSize(38, 22))
        self.pushButton_refresh_proy.setAutoFillBackground(False)
        self.pushButton_refresh_proy.setStyleSheet("QPushButton{\n"
"border:1px solid #ffffff;\n"
"background-color: #ffffff;}\n"
"\n"
"QPushButton:hover{\n"
"border-color: rgb(248, 16, 51);}\n"
"")
        self.pushButton_refresh_proy.setText("")
        self.pushButton_refresh_proy.setIcon(icon2)
        self.pushButton_refresh_proy.setIconSize(QtCore.QSize(25, 20))
        self.pushButton_refresh_proy.setCheckable(False)
        self.pushButton_refresh_proy.setChecked(False)
        self.pushButton_refresh_proy.setAutoDefault(False)
        self.pushButton_refresh_proy.setDefault(False)
        self.pushButton_refresh_proy.setFlat(False)
        self.pushButton_refresh_proy.setObjectName("pushButton_refresh_proy")
        self.horizontalLayout_5.addWidget(self.pushButton_refresh_proy)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tableWidget_proy_prin = QtWidgets.QTableWidget(self.tab_proyectos)
        self.tableWidget_proy_prin.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget_proy_prin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.tableWidget_proy_prin.setObjectName("tableWidget_proy_prin")
        self.tableWidget_proy_prin.setColumnCount(7)
        self.tableWidget_proy_prin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_proy_prin.setHorizontalHeaderItem(6, item)
        self.verticalLayout_5.addWidget(self.tableWidget_proy_prin)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        self.tabWidget_principal.addTab(self.tab_proyectos, "")
        self.horizontalLayout_3.addWidget(self.tabWidget_principal)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindo_principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindo_principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 25))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuGestion = QtWidgets.QMenu(self.menubar)
        self.menuGestion.setObjectName("menuGestion")
        self.menuFuncionalidades = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        self.menuFuncionalidades.setFont(font)
        self.menuFuncionalidades.setObjectName("menuFuncionalidades")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        self.menuAyuda.setFont(font)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindo_principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindo_principal)
        self.statusbar.setObjectName("statusbar")
        MainWindo_principal.setStatusBar(self.statusbar)
        self.actionDescripcion = QtWidgets.QAction(MainWindo_principal)
        self.actionDescripcion.setObjectName("actionDescripcion")
        self.actionAcerca_de = QtWidgets.QAction(MainWindo_principal)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionCargar_Nomina = QtWidgets.QAction(MainWindo_principal)
        self.actionCargar_Nomina.setObjectName("actionCargar_Nomina")
        self.actionSalvar_Datos = QtWidgets.QAction(MainWindo_principal)
        self.actionSalvar_Datos.setObjectName("actionSalvar_Datos")
        self.actionSalir = QtWidgets.QAction(MainWindo_principal)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        self.actionSalir.setFont(font)
        self.actionSalir.setObjectName("actionSalir")
        self.actionA_adir = QtWidgets.QAction(MainWindo_principal)
        self.actionA_adir.setObjectName("actionA_adir")
        self.actionEliminar = QtWidgets.QAction(MainWindo_principal)
        self.actionEliminar.setObjectName("actionEliminar")
        self.actionListar = QtWidgets.QAction(MainWindo_principal)
        self.actionListar.setObjectName("actionListar")
        self.actionA_adir_2 = QtWidgets.QAction(MainWindo_principal)
        self.actionA_adir_2.setObjectName("actionA_adir_2")
        self.actionEliminar_2 = QtWidgets.QAction(MainWindo_principal)
        self.actionEliminar_2.setObjectName("actionEliminar_2")
        self.actionListar_2 = QtWidgets.QAction(MainWindo_principal)
        self.actionListar_2.setObjectName("actionListar_2")
        self.actionCalcular_Salario = QtWidgets.QAction(MainWindo_principal)
        self.actionCalcular_Salario.setObjectName("actionCalcular_Salario")
        self.actionDespedir_Trabajador = QtWidgets.QAction(MainWindo_principal)
        self.actionDespedir_Trabajador.setObjectName("actionDespedir_Trabajador")
        self.actionA_adir_3 = QtWidgets.QAction(MainWindo_principal)
        self.actionA_adir_3.setObjectName("actionA_adir_3")
        self.actionEliminar_3 = QtWidgets.QAction(MainWindo_principal)
        self.actionEliminar_3.setObjectName("actionEliminar_3")
        self.actionListar_3 = QtWidgets.QAction(MainWindo_principal)
        self.actionListar_3.setObjectName("actionListar_3")
        self.actionListado_de_Proyectos = QtWidgets.QAction(MainWindo_principal)
        self.actionListado_de_Proyectos.setObjectName("actionListado_de_Proyectos")
        self.actionPorciento_de_cumplimiento = QtWidgets.QAction(MainWindo_principal)
        self.actionPorciento_de_cumplimiento.setObjectName("actionPorciento_de_cumplimiento")
        self.actionDeterminar_N_mina = QtWidgets.QAction(MainWindo_principal)
        self.actionDeterminar_N_mina.setObjectName("actionDeterminar_N_mina")
        self.actionTrabajadores_Vinculados = QtWidgets.QAction(MainWindo_principal)
        self.actionTrabajadores_Vinculados.setObjectName("actionTrabajadores_Vinculados")
        self.actionTrabajadores_no_VInculados = QtWidgets.QAction(MainWindo_principal)
        self.actionTrabajadores_no_VInculados.setObjectName("actionTrabajadores_no_VInculados")
        self.actionProyectos = QtWidgets.QAction(MainWindo_principal)
        self.actionProyectos.setObjectName("actionProyectos")
        self.actionAbrir = QtWidgets.QAction(MainWindo_principal)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionTotal_de_salarios_a_pagar = QtWidgets.QAction(MainWindo_principal)
        self.actionTotal_de_salarios_a_pagar.setObjectName("actionTotal_de_salarios_a_pagar")
        self.actionAbrir_Gest = QtWidgets.QAction(MainWindo_principal)
        self.actionAbrir_Gest.setObjectName("actionAbrir_Gest")
        self.actionAbrir_Gest_2 = QtWidgets.QAction(MainWindo_principal)
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed")
        font.setPointSize(12)
        self.actionAbrir_Gest_2.setFont(font)
        self.actionAbrir_Gest_2.setShortcutVisibleInContextMenu(True)
        self.actionAbrir_Gest_2.setObjectName("actionAbrir_Gest_2")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuGestion.addAction(self.actionAbrir_Gest_2)
        self.menuFuncionalidades.addAction(self.actionPorciento_de_cumplimiento)
        self.menuFuncionalidades.addSeparator()
        self.menuFuncionalidades.addAction(self.actionTotal_de_salarios_a_pagar)
        self.menuAyuda.addAction(self.actionDescripcion)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcerca_de)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuGestion.menuAction())
        self.menubar.addAction(self.menuFuncionalidades.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindo_principal)
        self.tabWidget_principal.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindo_principal)

    def retranslateUi(self, MainWindo_principal):
        _translate = QtCore.QCoreApplication.translate
        MainWindo_principal.setWindowTitle(_translate("MainWindo_principal", "Sistema de Nóminas"))
        self.label_2.setText(_translate("MainWindo_principal", "NOMINAS"))
        self.lineEdit_busar_vin.setPlaceholderText(_translate("MainWindo_principal", " Buscar para despedir:"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(0)
        item.setText(_translate("MainWindo_principal", "ID"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(1)
        item.setText(_translate("MainWindo_principal", "Nombre"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(2)
        item.setText(_translate("MainWindo_principal", "Sexo"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(3)
        item.setText(_translate("MainWindo_principal", "Edad"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(4)
        item.setText(_translate("MainWindo_principal", "Fecha de nacimiento"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(5)
        item.setText(_translate("MainWindo_principal", "Nivel profesional"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(6)
        item.setText(_translate("MainWindo_principal", "Proyecto vinculado"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(7)
        item.setText(_translate("MainWindo_principal", "Rol desempeñado"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(8)
        item.setText(_translate("MainWindo_principal", "Plan asig"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(9)
        item.setText(_translate("MainWindo_principal", "Plan real"))
        item = self.tableWidget_vin_prin.horizontalHeaderItem(10)
        item.setText(_translate("MainWindo_principal", "Salario"))
        self.tabWidget_principal.setTabText(self.tabWidget_principal.indexOf(self.tab_vinculados), _translate("MainWindo_principal", "Trabajadores Vinculados"))
        self.lineEdit_no_vin.setPlaceholderText(_translate("MainWindo_principal", " Buscar para despedir:"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(0)
        item.setText(_translate("MainWindo_principal", "ID"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(1)
        item.setText(_translate("MainWindo_principal", "Nombre"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(2)
        item.setText(_translate("MainWindo_principal", "Sexo"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(3)
        item.setText(_translate("MainWindo_principal", "Edad"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(4)
        item.setText(_translate("MainWindo_principal", "Fecha de nacimiento"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(5)
        item.setText(_translate("MainWindo_principal", "Nivel profesional"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(6)
        item.setText(_translate("MainWindo_principal", "Responsabilidad"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(7)
        item.setText(_translate("MainWindo_principal", "Llegadas tarde"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(8)
        item.setText(_translate("MainWindo_principal", "Horas trabajadas"))
        item = self.tableWidget_no_vin_prin.horizontalHeaderItem(9)
        item.setText(_translate("MainWindo_principal", "Salario"))
        self.tabWidget_principal.setTabText(self.tabWidget_principal.indexOf(self.tab_no_vinculado), _translate("MainWindo_principal", "Trabajadores no Vinculados"))
        self.lineEdit_proy.setPlaceholderText(_translate("MainWindo_principal", " Buscar:"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(0)
        item.setText(_translate("MainWindo_principal", "ID"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(1)
        item.setText(_translate("MainWindo_principal", "Nombre"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(2)
        item.setText(_translate("MainWindo_principal", "Cliente"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(3)
        item.setText(_translate("MainWindo_principal", "Costo"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(4)
        item.setText(_translate("MainWindo_principal", "Fecha de inicio"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(5)
        item.setText(_translate("MainWindo_principal", "Fecha de culminacion"))
        item = self.tableWidget_proy_prin.horizontalHeaderItem(6)
        item.setText(_translate("MainWindo_principal", "% Culminacion"))
        self.tabWidget_principal.setTabText(self.tabWidget_principal.indexOf(self.tab_proyectos), _translate("MainWindo_principal", "Proyectos"))
        self.menuArchivo.setTitle(_translate("MainWindo_principal", "Archivo"))
        self.menuGestion.setTitle(_translate("MainWindo_principal", "Gestión"))
        self.menuFuncionalidades.setTitle(_translate("MainWindo_principal", "Funcionalidades"))
        self.menuAyuda.setTitle(_translate("MainWindo_principal", "Ayuda"))
        self.actionDescripcion.setText(_translate("MainWindo_principal", "Descripción"))
        self.actionAcerca_de.setText(_translate("MainWindo_principal", "Acerca de:"))
        self.actionCargar_Nomina.setText(_translate("MainWindo_principal", "Cargar Nomina"))
        self.actionSalvar_Datos.setText(_translate("MainWindo_principal", "Salvar Datos"))
        self.actionSalir.setText(_translate("MainWindo_principal", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindo_principal", "Ctrl+Q"))
        self.actionA_adir.setText(_translate("MainWindo_principal", "Añadir"))
        self.actionEliminar.setText(_translate("MainWindo_principal", "Eliminar"))
        self.actionListar.setText(_translate("MainWindo_principal", "Listar"))
        self.actionA_adir_2.setText(_translate("MainWindo_principal", "Añadir"))
        self.actionEliminar_2.setText(_translate("MainWindo_principal", "Eliminar"))
        self.actionListar_2.setText(_translate("MainWindo_principal", "Listar"))
        self.actionCalcular_Salario.setText(_translate("MainWindo_principal", "Calcular Salario"))
        self.actionDespedir_Trabajador.setText(_translate("MainWindo_principal", "Despedir Trabajador"))
        self.actionA_adir_3.setText(_translate("MainWindo_principal", "Añadir"))
        self.actionEliminar_3.setText(_translate("MainWindo_principal", "Eliminar"))
        self.actionListar_3.setText(_translate("MainWindo_principal", "Listar"))
        self.actionListado_de_Proyectos.setText(_translate("MainWindo_principal", "Listado de Proyectos"))
        self.actionPorciento_de_cumplimiento.setText(_translate("MainWindo_principal", "Porciento de cumplimiento actual"))
        self.actionDeterminar_N_mina.setText(_translate("MainWindo_principal", "Determinar Nómina"))
        self.actionTrabajadores_Vinculados.setText(_translate("MainWindo_principal", "Trabajadores Vinculados"))
        self.actionTrabajadores_no_VInculados.setText(_translate("MainWindo_principal", "Trabajadores no VInculados"))
        self.actionProyectos.setText(_translate("MainWindo_principal", "Proyectos"))
        self.actionAbrir.setText(_translate("MainWindo_principal", "Abrir"))
        self.actionTotal_de_salarios_a_pagar.setText(_translate("MainWindo_principal", "Total de salarios a pagar"))
        self.actionAbrir_Gest.setText(_translate("MainWindo_principal", "Abrir"))
        self.actionAbrir_Gest_2.setText(_translate("MainWindo_principal", "Abrir"))
        self.actionAbrir_Gest_2.setShortcut(_translate("MainWindo_principal", "Ctrl+G"))
from Vista.UI.iconos_qr import iconos_rc
