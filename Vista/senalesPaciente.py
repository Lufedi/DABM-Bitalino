# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'senalesPaciente.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import pylab
import time
import Queue
from Logica.AplicacionBitalino import AplicacionBitalino

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
    am=1000
    xAchse=pylab.arange(0,am,1)
    yAchse=pylab.array([0]*am)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(822, 664)
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 560, 571, 51))
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


        #-------------CONFIGURACION DEL GRAFICADOR CON PYLAB
        #TODO pasar el graficador pylab a otra clase para desacoplarlo de la glase PyQt
        dc = Plot(None, width=20, height=20, dpi=100)
        self.graficaSenales = dc

        self.fig =pylab.figure(1)
        ax=self.fig.add_subplot(111) ; ax.grid(True)
        ax.set_xlabel("Time") ; ax.set_ylabel("Amplitude"); ax.axis([0,self.am,-1*self.graficaSenales.amplitud,self.graficaSenales.amplitud])
        line1=ax.plot(self.xAchse,self.yAchse,'r-')


        self.graficaSenales.setGeometry(QtCore.QRect(40, 190, 731, 321))
        manager = pylab.get_current_fig_manager()
        self.layout=QtGui.QVBoxLayout(self.cajita)
        self.layout.setGeometry(QtCore.QRect(40, 190, 731, 321))
        self.layout.setObjectName(_fromUtf8("graficador"))
        self.layout.addWidget(self.graficaSenales)

        #--------------------------
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 520, 571, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.nueva_medicion = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.nueva_medicion.setObjectName(_fromUtf8("nueva_medicion"))
        self.horizontalLayout_2.addWidget(self.nueva_medicion)
        self.finalizar_medicion = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.finalizar_medicion.setObjectName(_fromUtf8("finalizar_medicion"))
        self.horizontalLayout_2.addWidget(self.finalizar_medicion)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 570, 111, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.Nombre_2 = QtGui.QLabel(self.centralwidget)
        self.Nombre_2.setGeometry(QtCore.QRect(60, 530, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Nombre_2.setFont(font)
        self.Nombre_2.setObjectName(_fromUtf8("Nombre_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 21))
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
        self.nueva_medicion.setText(_translate("MainWindow", "Nueva Medicion", None))
        self.finalizar_medicion.setText(_translate("MainWindow", "Finaliza Medicion", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "ECG", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "EMG", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "EDA", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "ACG", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "LUX", None))
        self.Nombre_2.setText(_translate("MainWindow", "Señal : ", None))
        self.menuOpciones.setTitle(_translate("MainWindow", "Opciones", None))
        self.actionVer_historial.setText(_translate("MainWindow", "Ver historial", None))
        self.actionDiagn_stico.setText(_translate("MainWindow", "Diagnóstico", None))

    def nuevaMedicion(self):
        self.graficaSenales.orden_senal = 0
        self.graficaSenales.senal_id = AplicacionBitalino.consultarMaxIdSenal() + 1


    def graficar(self, stream):
        #TODO Agregar parametros para guardar las senales correspondientes al paciente
        self.graficaSenales.graficar(stream)

    def detener(self):
        self.graficaSenales.detener()
class Plot(FigureCanvas):
    def __init__(self,parent=None, width=20, height=20, dpi=100):
        #fig = Figure(figsize=(width, height), dpi=dpi )
        #self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)

        #self.compute_initial_figure()

        #



        self.am=1000
        self.xAchse=pylab.arange(0,self.am,1)
        self.yAchse=pylab.array([0]*self.am)

        self.fig = pylab.figure(1)
        self.ax = self.fig.add_subplot(111)
        self.ax.grid(True)
        self.ax.set_title("ECG")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amplitude")
        self.amplitud = 1.5
        self.ax.axis([0,self.am,-1*self.amplitud,self.amplitud])
        self.line1=self.ax.plot(self.xAchse,self.yAchse,'r-')
        self.manager = pylab.get_current_fig_manager()




        #TODO Crear un controlador y desacoplar los siguientes atributos de la clase Plot
        self.paciente = None
        self.diagnostico_id = None
        self.values=[]
        self.values = [0 for x in range(self.am)]
        self.segmento_senal = []
        self.longitud_segmento = 200
        self.id_senal = None
        self.orden_senal = None
        self.senal_id = None


        #self.q = Queue.Queue()

        #Leer de un archivos los datos de graficacion#
        #datarray = open("..\ecgsyn.dat")
        #for data in datarray:
            #self.q.append(data.split(" ")[1])
        #    self.q.put(data.split(" ")[1])
        #----------------------------------------#




        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def SinwaveformGenerator(self):
      #global values,T1,Konstant,T0,q

      if(not self.q.empty()):
        a = self.q.get()
        #agregando el dato al arreglo para guardar en la base de datos
        self.segmento_senal.append(a)
        #Agregando al values para que sea graficado
        self.values.append(a)
        #verificar si hay que guardar el segmento de la senal
        if(len(self.segmento_senal) == self.longitud_segmento):
            #guardar la senal
            AplicacionBitalino.agregarSenal( self.senal_id, self.orden_senal, self.segmento_senal, self.diagnostico_id)
            self.orden_senal+=1
            self.segmento_senal = []
        #agregando el dato al arreglo para graficar

      else:
          print "is empty"
    def RealtimePloter(self):
      #global values
      CurrentXAxis=pylab.arange(len(self.values)-self.am,len(self.values),1)
      self.line1[0].set_data(CurrentXAxis,pylab.array(self.values[-self.am:]))
      self.ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),-1*self.amplitud,self.amplitud])
      self.manager.canvas.draw()
      #manager.show()
    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')
    def graficar(self, stream):
        print "graficando"
        self.q = stream
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(0)
    def detener(self):
        self.timer.stop()

    def update_figure(self):
        self.RealtimePloter()
        self.SinwaveformGenerator()
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        #l = [random.randint(0, 10) for i in range(4)]

        #self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()
    def set_diagnostico(self, diagnostico_id):
        self.diagnostico_id = diagnostico_id

    def set_paciente(self, paciente):
        self.paciente  = paciente

    #timer = fig.canvas.new_timer(interval=1)
    #timer.add_callback(RealtimePloter, ())
    #timer2 = fig.canvas.new_timer(interval=1)
    #timer2.add_callback(SinwaveformGenerator, ())
    #timer.start()
    #timer2.start()
    #pylab.show()