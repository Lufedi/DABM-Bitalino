import sys
import random
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt

"""
class MyMplCanvas():
    Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.).'''
    def __init__(self, parent=None, width=5, height=4, dpi=100):


        #self.compute_initial_figure()
        #





    def compute_initial_figure(self):
        pass
"""
class MyMplCanvas(FigureCanvas):
    x, y = 0, 0 ; interval=10 ; xAxe, yAxe=[], []
    arch=open("ecgsyn.dat") ; data=arch.readlines()

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = plt.figure()
        self.axes = self.fig.add_subplot(1,1,1)
        self.axes.hold(False)
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        ani= animation.FuncAnimation(self.fig, self.update_figure, interval=1000)

    def compute_initial_figure(self):
        data1=[]
        for i in range(0, len(self.data)):
            axe=[float(i) for i in self.data[i].strip().split(" ")]
            data1.append(axe)
        self.data=data1
        x, y=self.data[self.x:self.x+self.interval] ,self.data[self.y:self.y+self.interval]
        self.xAxe.append(x) ;  self.yAxe.append(y)
        self.axes.plot(x,y,'b')

    def update_figure(self):
        print("hola")
        if(self.x <len(self.data) and self.y < len(self.data)):
            x, y=self.data[self.x:self.x+self.interval] ,self.data[self.y:self.y+self.interval]
            self.xAxe.append(x) ;  self.yAxe.append(y)
            self.axes.plot(x,y, 'b')
            self.x+=self.interval ; self.y+=self.interval
        else:
            print("Termina")

class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("application main window")

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)

        self.help_menu.addAction('&About', self.about)

        self.main_widget = QWidget(self)

        l = QVBoxLayout(self.main_widget)
        dc = MyMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        l.addWidget(dc)

        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)

        self.statusBar().showMessage("All hail matplotlib!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
  """embedding_in_qt5.py example
  Copyright 2015 BoxControL

  This program is a simple example of a Qt5 application embedding matplotlib
  canvases. It is base on example from matplolib documentation, and initially was
  developed from Florent Rougon and Darren Dale.

  http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

  It may be used and modified with no restriction; raw copies as well as
  modified versions may be distributed without limitation."""
  )

if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 Matplot Example")
    aw.show()
    #sys.exit(qApp.exec_())
    app.exec_()

