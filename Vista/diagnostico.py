# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtUi\diagnostico.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.resize(622, 520)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.titulo = QtGui.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(240, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setObjectName(_fromUtf8("titulo"))
        self.TI = QtGui.QLineEdit(self.centralwidget)
        self.TI.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.TI.setObjectName(_fromUtf8("TI"))
        self.Guardar = QtGui.QPushButton(self.centralwidget)
        self.Guardar.setGeometry(QtCore.QRect(190, 460, 75, 23))
        self.Guardar.setObjectName(_fromUtf8("Guardar"))
        self.IDp = QtGui.QLineEdit(self.centralwidget)
        self.IDp.setGeometry(QtCore.QRect(120, 70, 171, 31))
        self.IDp.setObjectName(_fromUtf8("IDp"))
        self.Cancelar = QtGui.QPushButton(self.centralwidget)
        self.Cancelar.setGeometry(QtCore.QRect(310, 460, 75, 23))
        self.Cancelar.setObjectName(_fromUtf8("Cancelar"))
        self.nombreLabel = QtGui.QLabel(self.centralwidget)
        self.nombreLabel.setGeometry(QtCore.QRect(20, 110, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nombreLabel.setFont(font)
        self.nombreLabel.setObjectName(_fromUtf8("nombreLabel"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 180, 581, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 269))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.textEdit = QtGui.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 581, 271))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.nombreP = QtGui.QTextEdit(self.centralwidget)
        self.nombreP.setGeometry(QtCore.QRect(90, 110, 511, 31))
        self.nombreP.setObjectName(_fromUtf8("nombreP"))
        self.obsLabel = QtGui.QLabel(self.centralwidget)
        self.obsLabel.setGeometry(QtCore.QRect(20, 150, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.obsLabel.setFont(font)
        self.obsLabel.setObjectName(_fromUtf8("obsLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.titulo.setText(_translate("MainWindow", "Diagnóstico", None))
        self.Guardar.setText(_translate("MainWindow", "Guardar", None))
        self.Cancelar.setText(_translate("MainWindow", "Cancelar", None))
        self.nombreLabel.setText(_translate("MainWindow", "Nombre", None))
        self.obsLabel.setText(_translate("MainWindow", "Observaciones: ", None))

