from sqlalchemy.sql.base import _from_objects

__author__ = 'MariaAlejandraLuisFelipe'
from PyQt5 import QtCore, QtGui, QtWidgets
from Vista.agregarpacienteGUI import Ui_MainWindow
from Logica.Aplicacion import *

class MainWindows(QtWidgets.QMainWindow):
    tids=["CC", "CE", "TI", "Registro Civil"]
    def __init__(self, *args, **kwargs):
        super(MainWindows, self).__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ti.
        self.ui.send.clicked.connect(self.enviarPaciente())

    def enviarPaciente(self):
        id=self.ui.idp.toPlainText()
        Aplicacion.agregaPaciente()


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp = MainWindows()
    pp.show()
    sys.exit(app.exec_())

