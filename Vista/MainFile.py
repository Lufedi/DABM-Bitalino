#from PyQt4.QtGui import QMessageBox
from sqlalchemy.sql.base import _from_objects

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from Vista.agregarpacienteGUI import Ui_MainWindow as AgregaPaciente
from Vista.buscarDispositivosGUI import Ui_MainWindow as Dispositivos
from Vista.senalesPaciente import Ui_MainWindow as Senales
from Vista.diagnostico import Ui_MainWindow as DiagnosticoPaciente
from Vista.historialPactiente import Ui_MainWindow as HistorialPaciente
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
        self.ui.actionImportar_pacientes.setShortcut("Ctrl+I")
        self.connect(self.ui.actionImportar_pacientes, SIGNAL("triggered()"),self.importarPacientes)
        self.ui.actionSalir.setShortcut("Ctrl+E")
        self.connect(self.ui.actionSalir, SIGNAL("triggered()"), self.salir)

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
        try:
            if(AplicacionBitalino.validaDatos(idP, name, last, age, phone, b.year())):
                AplicacionBitalino.agregarPaciente(idP,ti, name,  last, gender, birth, age, phone)
                QtGui.QMessageBox.about(self, "ACCION", "El paciente ha sido agregado correctamente")
            else:
                QtGui.QMessageBox.about(self, "DATOS CORRUPTOS", "Por favor revise los datos ingresados")
        except Exception as e:
                QtGui.QMessageBox.about(self, "ERROR ", e.message)

    def salir(self):
        exit()

    def importarPacientes(self):
        try:
            errores=AplicacionBitalino.importarPacientes("../pacientes.txt")
            if(len(errores)==0):
                 QtGui.QMessageBox.about(self, "ACCION", "Se ha terminado de importar el archivo de pacientes")
            else:
                msg="\n".join(errores)
                QtGui.QMessageBox.about(self, "ERROR", "Se ha terminado de importar el archivo de pacientes\n"+
                                                        "No se pudieron importar los siguientes pacientes: \n"+msg)
        except Exception as e:
            QtGui.QMessageBox.about(self, "ERROR DE ARCHIVO", "El archivo pacientes no existe")

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
        self.ui.conectar.setDisabled(True)
        self.ui.Leer.setDisabled(True)
        self.ui.plainTextEdit.setDisabled(True)

    def buscarDispositivos(self):
        self.ui.comboBox.clear()
        self.dispositivos=[]
        print("Buscando")
        l = self.adaptador.encontrarDispositivos()
        for d in l:
            print(d[0], d[1])
            self.dispositivos.append(str(d[0])+"-"+str(d[1]))
        self.ui.comboBox.addItems(self.dispositivos)
        self.ui.conectar.setEnabled(True)

    def conectar(self):
        try:

            mac  = str((self.ui.comboBox.currentText()).split("-")[0])
            print(mac)
            self.adaptador.conectarseADispositivo(mac)
            QtGui.QMessageBox.about(self, "ACCION", "Se ha conectado correctamente al dispositivo " + mac)
            self.close()
        except:
            QtGui.QMessageBox.about(self, "ERROR", "Han habido problemas conectando el dispositivo")


    def leer(self):
        #print("Leyendo")
        #self.adaptador.comenzar([0])
        #data =  self.adaptador.leer()
        #self.ui.plainTextEdit.setPlainText(str(data[4:]))
        pass
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
        self.ui.nombre.setDisabled(True) ; self.ui.ID.setDisabled(True)
        self.ventanaAgregar=MainWindows()

    def agregaPaciente(self):
        self.ventanaAgregar.show()

    def accionesMenu(self):
        self.ui.actionDiagn_stico.setShortcut("Ctrl+D")
        self.connect(self.ui.actionDiagn_stico, SIGNAL("triggered()"), self.realizaDiagnostico)
        self.ui.actionTarjeta_Bitalino.setShortcut("Ctrl+T")
        self.connect(self.ui.actionTarjeta_Bitalino, SIGNAL("triggered()"), self.seleccionaTarjeta)
        self.ui.actionVer_historial.setShortcut("Ctrl+H")
        self.connect(self.ui.actionVer_historial, SIGNAL("triggered()"), self.verHistorial)

    def verHistorial(self):
        idP = str(self.ui.busqueda.toPlainText())
        tiP = str(self.tids[self.ui.ti.currentIndex()])
        if(len(idP)>0 and idP !="ID"):
            self.ventanaHistorial=HistorialPacientesWindow(idP, tiP)
            self.ventanaHistorial.show()
        else:
            QtGui.QMessageBox.about(self, "ERROR", "Los campos de identificacion y tipo de identificacion no pueden ser vacios.")
    def seleccionaTarjeta(self):
        self.ejec=TarjetaBitalinoWindow()
        self.ejec.show()

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
        self.ui.finalizar_medicion.setDisabled(True)
        self.ui.graficar(i)

    def detener(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(True)
        self.ui.detener()
        self.ui.finalizar_medicion.setEnabled(True)

    #TODO crear un controlador que desacople la logica de la vista
    def buscaPaciente(self):

        try:
            if Adaptador.mac != None:
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
                    self.ui.actionVer_historial.setEnabled(True)
                else:
                    QtGui.QMessageBox.about(self, "INFO", "No se ha encontrado un paciente")
            else:
                QtGui.QMessageBox.about(self, "INFO", "No ha conectado un dispositivo de lectura")
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
class HistorialPacientesWindow(QtGui.QMainWindow):
    def __init__(self, idPaciente, tiPaciente,  *args, **kwargs):
        super(HistorialPacientesWindow, self).__init__(*args, **kwargs)
        self.ui = HistorialPaciente()
        self.ui.setupUi(self)
        self.idP= idPaciente
        self.tiP=tiPaciente
        paciente=AplicacionBitalino.consultarPacientePorId(self.idP, self.tiP)
        self.ui.nombre_paciente_lbl.setText(paciente.nombres+" "+paciente.apellidos + " - " + self.idP)
        self.prepararVentanas()
        self.ui.diagnosticos_list.clicked.connect(self.prepararMediciones)
        self.ui.cargar_btn.clicked.connect(self.cargarSenal)
    def prepararVentanas(self):
        diagnosticos = AplicacionBitalino.consultarDiagnosticosPaciente(self.idP)
        for d in diagnosticos:
            self.ui.diagnosticos_list.addItem("No. " + str(d.id) + " " + str(d.comentarios))
    def prepararMediciones(self):
        self.ui.senales_list.clear()
        diagnostico_id = self.ui.diagnosticos_list.currentItem().text().split(" ")[1]
        #print str(diagnostico_id)
        senales = AplicacionBitalino.consultarSenalesDelDiagnostico(str(diagnostico_id))
        for s in senales:
            self.ui.senales_list.addItem("Senal No: " + str(s.id))

    def cargarSenal(self):
        senal_id = self.ui.senales_list.currentItem().text().split(" ")[2]
        data  =  AplicacionBitalino.consultarSenal(str(senal_id))
        pylab.plot(data)
        pylab.ylabel("Pulso")
        pylab.xlabel("Tiempo")
        pylab.show()









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
        self.ui.Guardar.clicked.connect(self.actualizarDiagnostico)

    def actualizarDiagnostico(self):
        comentarios=str(self.ui.textEdit.toPlainText())
        #AplicacionBitalino.agregarDiagnostico(comentarios, self.idP)
        AplicacionBitalino.actualizarDiagnostico(comentarios, self.idP)
        self.close()
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
    #pp = MainWindows() #Agregar paciente
    pp = pacienteWindow() #seleccionat paciente
    #pp = HistorialPacientesWindow("1020793766", "CC")
    #pp=DiagnosticoWindow("101010101", "CC")
    pp.show()
    sys.exit(app.exec_())
