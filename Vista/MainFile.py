from sqlalchemy.sql.base import _from_objects
__author__ = 'MariaAlejandraLuisFelipe'
from PyQt5 import QtCore, QtGui, QtWidgets
from Vista.agregarpacienteGUI import Ui_MainWindow
from Vista.buscarDispositivosGUI import Ui_MainWindow2
from Logica.Aplicacion import *
from Persistencia.Base import *
from Logica.Adaptador import *

class MainWindows(QtWidgets.QMainWindow):
    tids, gender=["CC", "CE", "TI", "Registro Civil"], ["F", "M", "Otro"]
    month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def __init__(self, *args, **kwargs):
        super(MainWindows, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ti.addItems(self.tids)
        self.ui.gender.addItems(self.gender)
        self.ui.send.clicked.connect(self.enviarPaciente)
        self.ui.clean.clicked.connect(self.limpia)
        self.add=Agregar()

    def enviarPaciente(self):
        idP, ti=self.ui.idp.toPlainText(), self.tids[self.ui.ti.currentIndex()]
        name, last=self.ui.name.toPlainText(), self.ui.last.toPlainText()
        gender, b=self.gender[self.ui.gender.currentIndex()], self.ui.dateEdit.date() ; birth=""
        if(b.day()<10):
            birth+="0"+str(b.day())
        else:
            birth+=str(b.day())
        if (b.month()<10):
            birth+="/"+"0"+str(b.month())
        else:
            birth+="/"+str(b.month())
        birth+="/"+str(b.year())[2:4] ; print(birth) ;  age=self.ui.spinBox.value(); phone=self.ui.phone.toPlainText()
        if(not(self.validaDatos(idP, name, last, age, phone))):
            raise Exception("ERROR DATOS CORRUPTOS")
        self.add.agregaPaciente(idP, ti, name, last, gender, datetime.datetime.strptime(birth, "%d/%m/%y").date(), age, phone)

    def validaDatos(self, idP, name, last, age, phone):
        r=True
        try:
            int(idP) ; r=len(name.strip())>0 and len(last.strip())>0 and age>=0 and len(phone.strip())>0 ; int(phone)
            print(r) ; return r
        except:
            raise Exception("Datos corruptos")

    def limpia(self):
        self.ui.idp.setText("")
        self.ui.name.setText(""), self.ui.last.setText("")

class TarjetaBitalinoWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(TarjetaBitalinoWindow, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buscarDispositivos)
        self.ui.conectar.clicked.connect(self.conectar)
        self.adaptador = Adaptador()


    def buscarDispositivos(self):
        print("Buscando")
        l = self.adaptador.encontrarDispositivos()
        print(l)
        for d in l:
            self.ui.comboBox.addItem(str(d[0])+"-"+str(d[1]))

    def conectar(self):
        print("Conectando")
        mac  = (self.ui.comboBox.currentText()).split("-")[0]
        print(mac)
        dispositivo = self.adaptador.conectarseADispositivo(mac)

'''def v1():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp = TarjetaBitalinoWindow()
    pp.show()
    sys.exit(app.exec())
v1()'''
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp = MainWindows()
    pp.show()
    sys.exit(app.exec_())



