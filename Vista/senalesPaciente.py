# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'senalesPaciente.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowPaciente(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.busqueda = QtWidgets.QTextEdit(self.centralwidget)
        self.busqueda.setGeometry(QtCore.QRect(40, 80, 261, 41))
        self.busqueda.setObjectName("busqueda")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(360, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.buscar = QtWidgets.QPushButton(self.centralwidget)
        self.buscar.setGeometry(QtCore.QRect(480, 80, 131, 41))
        self.buscar.setObjectName("buscar")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(630, 80, 141, 41))
        self.agregar.setObjectName("agregar")
        self.Nombre = QtWidgets.QLabel(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nombre.setFont(font)
        self.Nombre.setObjectName("Nombre")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(100, 140, 421, 31))
        self.nombre.setObjectName("nombre")
        self.ID_2 = QtWidgets.QLabel(self.centralwidget)
        self.ID_2.setGeometry(QtCore.QRect(530, 140, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ID_2.setFont(font)
        self.ID_2.setObjectName("ID_2")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(550, 140, 221, 31))
        self.ID.setObjectName("ID")
        self.senales = QtWidgets.QTextEdit(self.centralwidget)
        self.senales.setGeometry(QtCore.QRect(40, 190, 731, 321))
        self.senales.setObjectName("senales")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 510, 731, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.TI = QtWidgets.QLabel(self.centralwidget)
        self.TI.setGeometry(QtCore.QRect(330, 80, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TI.setFont(font)
        self.TI.setObjectName("TI")
        self.ti = QtWidgets.QComboBox(self.centralwidget)
        self.ti.setGeometry(QtCore.QRect(350, 80, 101, 41))
        self.ti.setObjectName("ti")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName("menubar")
        self.menuOpciones = QtWidgets.QMenu(self.menubar)
        self.menuOpciones.setObjectName("menuOpciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVer_historial = QtWidgets.QAction(MainWindow)
        self.actionVer_historial.setObjectName("actionVer_historial")
        self.actionDiagn_stico = QtWidgets.QAction(MainWindow)
        self.actionDiagn_stico.setObjectName("actionDiagn_stico")
        self.menuOpciones.addAction(self.actionVer_historial)
        self.menuOpciones.addAction(self.actionDiagn_stico)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.busqueda.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ID</p></body></html>"))
        self.titulo.setText(_translate("MainWindow", "Paciente"))
        self.buscar.setText(_translate("MainWindow", "Buscar paciente"))
        self.agregar.setText(_translate("MainWindow", "Agregar paciente"))
        self.Nombre.setText(_translate("MainWindow", "Nombre"))
        self.ID_2.setText(_translate("MainWindow", "ID"))
        self.senales.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Señales</p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Graficar"))
        self.pushButton.setText(_translate("MainWindow", "Detenerse"))
        self.TI.setText(_translate("MainWindow", "TI"))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones"))
        self.actionVer_historial.setText(_translate("MainWindow", "Ver historial"))
        self.actionDiagn_stico.setText(_translate("MainWindow", "Diagnóstico"))

