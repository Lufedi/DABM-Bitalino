# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'senalesPaciente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import pylab

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(808, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.busqueda = QtGui.QTextEdit(self.centralwidget)
        self.busqueda.setGeometry(QtCore.QRect(40, 80, 261, 41))
        self.busqueda.setObjectName(_fromUtf8("busqueda"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(360, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.buscar = QtGui.QPushButton(self.centralwidget)
        self.buscar.setGeometry(QtCore.QRect(480, 80, 131, 41))
        self.buscar.setObjectName(_fromUtf8("buscar"))
        self.agregar = QtGui.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(630, 80, 141, 41))
        self.agregar.setObjectName(_fromUtf8("agregar"))
        self.Nombre = QtGui.QLabel(self.centralwidget)
        self.Nombre.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nombre.setFont(font)
        self.Nombre.setObjectName(_fromUtf8("Nombre"))
        self.nombre = QtGui.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(100, 140, 421, 31))
        self.nombre.setObjectName(_fromUtf8("nombre"))
        self.ID_2 = QtGui.QLabel(self.centralwidget)
        self.ID_2.setGeometry(QtCore.QRect(530, 140, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ID_2.setFont(font)
        self.ID_2.setObjectName(_fromUtf8("ID_2"))
        self.ID = QtGui.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(550, 140, 221, 31))
        self.ID.setObjectName(_fromUtf8("ID"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 510, 731, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.TI = QtGui.QLabel(self.centralwidget)
        self.TI.setGeometry(QtCore.QRect(330, 80, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TI.setFont(font)
        self.TI.setObjectName(_fromUtf8("TI"))
        self.ti = QtGui.QComboBox(self.centralwidget)
        self.ti.setGeometry(QtCore.QRect(350, 80, 101, 41))
        self.ti.setObjectName(_fromUtf8("ti"))
        self.cajita = QtGui.QWidget(self.centralwidget)
        self.cajita.setGeometry(QtCore.QRect(40, 190, 731, 311))
        self.cajita.setObjectName(_fromUtf8("cajita"))
        am=1000
        xAchse=pylab.arange(0,am,1)
        yAchse=pylab.array([0]*am)
        fig =pylab.figure(1)
        ax=fig.add_subplot(111) ; ax.grid(True)
        ax.set_xlabel("Time") ; ax.set_ylabel("Amplitude") ; ax.axis([0,am,-1.5,1.5])
        line1=ax.plot(xAchse,yAchse,'r-')
        self.graficaSenales=FigureCanvas(fig)
        self.graficaSenales.setGeometry(QtCore.QRect(40, 190, 731, 321))
        manager = pylab.get_current_fig_manager()
        """self.senales = QtGui.QTextEdit(self.centralwidget)
        self.senales.setGeometry(QtCore.QRect(40, 190, 731, 321))
        self.senales.setObjectName(_fromUtf8("senales"))"""
        self.layout=QtGui.QVBoxLayout(self.cajita)
        self.layout.setGeometry(QtCore.QRect(40, 190, 731, 321))
        self.layout.setObjectName(_fromUtf8("graficador"))
        self.layout.addWidget(self.graficaSenales)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOpciones = QtGui.QMenu(self.menubar)
        self.menuOpciones.setObjectName(_fromUtf8("menuOpciones"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVer_historial = QtGui.QAction(MainWindow)
        self.actionVer_historial.setObjectName(_fromUtf8("actionVer_historial"))
        self.actionDiagn_stico = QtGui.QAction(MainWindow)
        self.actionDiagn_stico.setObjectName(_fromUtf8("actionDiagn_stico"))
        self.menuOpciones.addAction(self.actionVer_historial)
        self.menuOpciones.addAction(self.actionDiagn_stico)
        self.menubar.addAction(self.menuOpciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.busqueda.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">ID</span></p></body></html>", None))
        self.titulo.setText(_translate("MainWindow", "Paciente", None))
        self.buscar.setText(_translate("MainWindow", "Buscar paciente", None))
        self.agregar.setText(_translate("MainWindow", "Agregar paciente", None))
        self.Nombre.setText(_translate("MainWindow", "Nombre", None))
        self.ID_2.setText(_translate("MainWindow", "ID", None))
        self.pushButton_2.setText(_translate("MainWindow", "Graficar", None))
        self.pushButton.setText(_translate("MainWindow", "Detenerse", None))
        self.TI.setText(_translate("MainWindow", "TI", None))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones", None))
        self.actionVer_historial.setText(_translate("MainWindow", "Ver historial", None))
        self.actionDiagn_stico.setText(_translate("MainWindow", "Diagnóstico", None))

