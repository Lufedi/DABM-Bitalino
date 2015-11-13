#from PyQt4.QtGui import QMessageBox
from sqlalchemy.sql.base import _from_objects


from PyQt4 import QtGui
from Vista.agregarpacienteGUI import Ui_MainWindow as AgregaPaciente
from Vista.buscarDispositivosGUI import Ui_MainWindow as Dispositivos
from Vista.senalesPaciente import Ui_MainWindow as Senales
from Persistencia.Base import *
from Logica.Adaptador import *
from Logica.AplicacionBitalino import *
import time
from collections import deque
import Queue
import pylab

class MainWindows(QtGui.QMainWindow):
    tids, gender=["CC", "CE", "TI", "Registro Civil"], ["F", "M", "Otro"]
    month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    def __init__(self, *args, **kwargs):
        super(MainWindows, self).__init__(*args, **kwargs)
        self.ui = AgregaPaciente()
        self.ui.setupUi(self)
        self.ui.ti.addItems(self.tids)
        self.ui.gender.addItems(self.gender)
        self.ui.send.clicked.connect(self.enviarPaciente)
        self.ui.clean.clicked.connect(self.limpia)
       # self.add=Agregar()

    def enviarPaciente(self):
        self.ui.idp.toPlainText()+""
        idP, ti=self.ui.idp.toPlainText()+"", self.tids[self.ui.ti.currentIndex()]+""
        name, last=self.ui.name.toPlainText()+"", self.ui.last.toPlainText()+""
        gender, b=self.gender[self.ui.gender.currentIndex()], self.ui.dateEdit.date() ; birth=""
        if(b.day()<10):
            birth+="0"+str(b.day())
        else:
            birth+=str(b.day())
        if (b.month()<10):
            birth+="/"+"0"+str(b.month())
        else:
            birth+="/"+str(b.month())
        birth+="/"+str(b.year())[2:4] ; print(birth) ;  age=self.ui.spinBox.value(); phone=self.ui.phone.toPlainText()+""
        if(not(self.validaDatos(idP, name, last, age, phone, b.year()))):
            raise Exception("ERROR DATOS CORRUPTOS")
        self.add.agregaPaciente(idP, ti, name, last, gender, datetime.datetime.strptime(birth, "%d/%m/%y").date(), age, phone)

    def validaDatos(self, idP, name, last, age, phone, year):
        try:
            r=True
            int(idP) ; r=len(name)>0 and len(last)>0 and age>=0 and len(phone)>0 and year+age== datetime.datetime.now().year
            int(phone); print (r) ; return r
        except:
            raise Exception("Datos corruptos")
    def limpia(self):
        self.ui.idp.setText("")
        self.ui.name.setText(""), self.ui.last.setText("")
        self.ui.phone.clear()
        self.ui.spinBox.clear()
        self.ui.dateEdit.clear()

class TarjetaBitalinoWindow(QtGui.QMainWindow):
    dispositivos=[]
    def __init__(self, *args, **kwargs):
        super(TarjetaBitalinoWindow, self).__init__(*args, **kwargs)
        self.ui = Dispositivos()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.buscarDispositivos)
        self.ui.conectar.clicked.connect(self.conectar)
        self.ui.Leer.clicked.connect(self.leer)
        self.adaptador = Adaptador()

    def buscarDispositivos(self):
        self.ui.comboBox.clear()
        self.dispositivos=[]
        print("Buscando")
        l = self.adaptador.encontrarDispositivos()
        for d in l:
            print(d[0], d[1])
            self.dispositivos.append(str(d[0])+" "+str(d[1]))
        self.ui.comboBox.addItems(self.dispositivos)

    def conectar(self):
        print("Conectando")
        mac  = (self.ui.comboBox.currentText()).split("-")[0]
        print(mac)
        self.adaptador.conectarseADispositivo(mac)

    def leer(self):
        print("Leyendo")
        self.adaptador.comenzar([0])
        data =  self.adaptador.leer()
        self.ui.plainTextEdit.setPlainText(str(data[4:]))

class pacienteWindow(QtGui.QMainWindow):
    def __init__(self, *args, **kwargs):
        self.tids=["CC", "CE", "TI", "Registro Civil"]
        super(pacienteWindow, self).__init__(*args, **kwargs)
        self.ui = Senales()
        self.ui.setupUi(self)
        self.ui.ti.addItems(self.tids)
        self.ui.buscar.clicked.connect(self.buscaPaciente)
        self.ui.agregar.clicked.connect(self.agregaPaciente)
        self.ui.pushButton.clicked.connect(self.detener)
        self.ui.pushButton_2.clicked.connect(self.graficaSenal)
        self.ui.nombre.setDisabled(True) ; self.ui.ID.setDisabled(True)
        self.ventanaAgregar=MainWindows()

    def agregaPaciente(self):
        self.ventanaAgregar.show()


    def graficaSenal(self):
        self.ui.graficar()


    def detener(self):
        self.ui.detener()

    def buscaPaciente(self):
        try:
            #Limpiar los campos
            self.ui.nombre.setText("")
            self.ui.ID.setText("")
            idP = self.ui.busqueda.toPlainText()
            tiP = self.tids[self.ui.ti.currentIndex()]
            app = AplicacionBitalino()
            paciente = app.consultarPacientePorId(idP, tiP)
            print(paciente)
            if paciente != None:
                self.ui.nombre.setText(paciente.nombres)
                self.ui.ID.setText(paciente.id)
            else:
                QtGui.QMessageBox.about(self, "Info", "No se ha encontrado un paciente")
        except Exception as e:
            print(e)

"""def v1():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp = TarjetaBitalinoWindow()
    pp.show()
    sys.exit(app.exec())
v1()"""


"""if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp = TarjetaBitalinoWindow() #seleccionar tarjeta
    #pp = MainWindows() #Agregar paciente
    #pp = pacienteWindow() #seleccionat paciente
    pp.show()
    sys.exit(app.exec_())"""

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    #pp = TarjetaBitalinoWindow() #seleccionar tarjeta
    pp = MainWindows() #Agregar paciente
    #pp = pacienteWindow() #seleccionat paciente
    pp.show()
    sys.exit(app.exec_())
