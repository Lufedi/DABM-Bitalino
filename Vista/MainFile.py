#from PyQt4.QtGui import QMessageBox
from sqlalchemy.sql.base import _from_objects

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from Vista.agregarpacienteGUI import Ui_MainWindow as AgregaPaciente
from Vista.buscarDispositivosGUI import Ui_MainWindow as Dispositivos
from Vista.senalesPaciente import Ui_MainWindow as Senales
from Vista.diagnostico import Ui_MainWindow as DiagnosticoPaciente
from Persistencia.Base import *
from Logica.Adaptador import *
from Logica.AplicacionBitalino import AplicacionBitalino
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
        self.add=AplicacionBitalino()


    def enviarPaciente(self):
        idP = str(self.ui.idp.toPlainText())
        ti = self.tids[self.ui.ti.currentIndex()]
        name, last=str(self.ui.name.toPlainText()), str(self.ui.last.toPlainText())
        gender, b=self.gender[self.ui.gender.currentIndex()], self.ui.dateEdit.date() ; birth=""
        if(b.day()<10):
            birth+="0"+str(b.day())
        else:
            birth+=str(b.day())
        if (b.month()<10):
            birth+="/"+"0"+str(b.month())
        else:
            birth+="/"+str(b.month())
        birth+="/"+str(b.year())[2:4] ; print(birth) ;  age=str(self.ui.spinBox.value()); phone=str(self.ui.phone.toPlainText())
        print("idp " + idP, type(idP))

        print("birth  : " + birth)
        print( " ti " + ti )
        print(" name " + name)
        print(" gener " + gender )
        print(" date " + datetime.datetime.strptime(birth, "%d/%m/%y").date().__str__() )
        print(" age " + str(age) )
        print("phone " + phone )


        if ( self.validaDatos(idP, name, last, age, gender)):
            AplicacionBitalino.agregarPaciente(idP,ti, name,  last, gender, datetime.datetime.strptime(birth, "%d/%m/%y").date(), age, phone)
    def validaDatos(self, idP, name, last, age, phone):
            r=True
            try:
                int(idP) ; r=len(name.strip())>0 and len(last.strip())>0 and age>=0 and len(phone.strip())>0 ; int(phone)
                return (r)
            except:
                #raise Exception("DATOS CORRUPTOS, Por favor revise los datos ingresados")
                QtGui.QMessageBox.about(self, "Error", "DATOS CORRUPTOS, Por favor revise los datos ingresados")
        #birth = "10/06/94"
        #self.add.agregaPaciente(idP, "CC" , "luis" , "felipe" , "M" , datetime.datetime.strptime(birth, "%d/%m/%y").date(), "300210593", 21)   def validaDatos(self, idP, name, last, age, phone, year):



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
        self.preparaVentana()
        self.accionesMenu()

    def preparaVentana(self):
        self.ui.buscar.clicked.connect(self.buscaPaciente)
        self.ui.agregar.clicked.connect(self.agregaPaciente)
        self.ui.pushButton.clicked.connect(self.detener)
        self.ui.pushButton_2.clicked.connect(self.graficaSenal)
        self.ui.nueva_medicion.clicked.connect(self.nuevaMedicion)
        self.ui.finalizar_medicion.clicked.connect(self.terminarMedicion)
        self.ui.pushButton.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.nueva_medicion.setDisabled(True)
        self.ui.finalizar_medicion.setDisabled(True)
        self.ui.actionVer_historial.setDisabled(True)
        self.ui.nombre.setDisabled(True) ; self.ui.ID.setDisabled(True)
        self.ventanaAgregar=MainWindows()

    def agregaPaciente(self):
        self.ventanaAgregar.show()

    def accionesMenu(self):
        self.ui.actionDiagn_stico.setShortcut("Ctrl+D")
        self.connect(self.ui.actionDiagn_stico, SIGNAL("triggered()"), self.realizaDiagnostico)


    def terminarMedicion(self):
        self.ui.finalizar_medicion.setDisabled(True)
        self.ui.pushButton_2.setDisabled(True)
        self.ui.nueva_medicion.setEnabled(True)
    def nuevaMedicion(self):
        self.ui.nuevaMedicion()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.nueva_medicion.setDisabled(True)
        self.ui.finalizar_medicion.setEnabled(True)

    def graficaSenal(self):
        adaptador = Adaptador()
        i = adaptador.getInputStream()
        adaptador.comenzarAGraficar()
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.setEnabled(True)
        self.ui.graficar(i)

    def detener(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.detener()

    #TODO crear un controlador que desacople la logica de la vista
    def buscaPaciente(self):
        try:
            #Limpiar los campos
            self.ui.nombre.setText("")
            self.ui.ID.setText("")
            idP = str(self.ui.busqueda.toPlainText())
            tiP = self.tids[self.ui.ti.currentIndex()]
            paciente = AplicacionBitalino.consultarPacientePorId(idP, tiP)
            print(paciente)
            if paciente != None:
                self.ui.nueva_medicion.setEnabled(True)
                self.ui.nombre.setText(paciente.nombres + " " + paciente.apellidos)
                self.ui.ID.setText(paciente.id)
                self.ui.graficaSenales.set_paciente(paciente)
                AplicacionBitalino.agregarDiagnostico(None, paciente.id)
                diagnostico = AplicacionBitalino.consultarMaxIdDiagnostrico()
                self.ui.graficaSenales.set_diagnostico(diagnostico)

            else:
                QtGui.QMessageBox.about(self, "Info", "No se ha encontrado un paciente")
        except Exception as e:
            raise e

    def realizaDiagnostico(self):
        idP = str(self.ui.busqueda.toPlainText())
        tiP = str(self.tids[self.ui.ti.currentIndex()])
        if(len(idP)>0 and idP !="ID"):
            self.ventanaDiagnostico=DiagnosticoWindow(idP, tiP)
            self.ventanaDiagnostico.show()
        else:
            QtGui.QMessageBox.about(self, "ERROR", "Los campos de identificacion y tipo de identificacion no pueden ser vacios.")

class DiagnosticoWindow(QtGui.QMainWindow):
    def __init__(self, idPaciente, tiPaciente,  *args, **kwargs):
        super(DiagnosticoWindow, self).__init__(*args, **kwargs)
        self.ui = DiagnosticoPaciente()
        self.ui.setupUi(self)
        self.idP= idPaciente
        self.tiP=tiPaciente
        self.ui.TI.setText(self.tiP) ; self.ui.TI.setEnabled(False)
        self.ui.IDp.setText(self.idP) ; self.ui.IDp.setEnabled(False)
        paciente=AplicacionBitalino.consultarPacientePorId(self.idP, self.tiP)
        self.ui.nombreP.setText(paciente.nombres+" "+paciente.apellidos)
        self.ui.Guardar.clicked.connect(self.agregaDiagnostico)

    def agregaDiagnostico(self):
        comentarios=str(self.ui.textEdit.toPlainText())
        AplicacionBitalino.agregarDiagnostico(comentarios, self.idP)

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
    #pp=DiagnosticoWindow("101010101", "CC")
    pp.show()
    sys.exit(app.exec_())
