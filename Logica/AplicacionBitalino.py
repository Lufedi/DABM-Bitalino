from Persistencia.Base import *
from sqlalchemy import func
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,DateTime
import datetime
from sqlalchemy.sql import table, column, select, update, insert, and_

class AplicacionBitalino():
    diagnostico_id = None
    def __init__(self):
        pass

    @classmethod
    def consultarDiagnosticosPaciente(self, pacienteId):
        print pacienteId + "consultado"
        return Consulta.consultarDiagnosticosPaciente(pacienteId)
    @classmethod
    def actualizarDiagnostico(self, comentarios, idP):
        Agregar.actualizarDiagnostico(AplicacionBitalino.diagnostico_id, comentarios, idP)
    @classmethod
    def consultarMaxIdDiagnostrico(self):
        return Consulta.consultarMaxIdDiagnostrico()

    @classmethod
    def importarPacientes(self, path):
        arch=open(path) ; errores=[]
        for line in arch.readlines():
            datosPaciente=line.strip().split(";")
            try:
                birth=datetime.datetime.strptime(datosPaciente[5], "%d/%m/%y").date()
                if(self.validaDatos(datosPaciente[0], datosPaciente[2], datosPaciente[3], datosPaciente[6], datosPaciente[7], birth.year)):
                    self.agregarPaciente(datosPaciente[0], datosPaciente[1], datosPaciente[2],
                                    datosPaciente[3], datosPaciente[4], datosPaciente[5], datosPaciente[6], datosPaciente[7])
                else:
                    errores.append(str(datosPaciente[1]+" "+datosPaciente[0]))
            except:
                errores.append(str(datosPaciente[1]+" "+datosPaciente[0]))
        return errores

    @classmethod
    def validaDatos(self, idP, name, last, age, phone, year):
            r=True
            try:
                int(idP)
                r=len(name.strip())>0 and len(last.strip())>0 and age>=0 and len(phone.strip())>0 and year+int(age)== datetime.datetime.now().year; int(phone)
                return (r)
            except:
                return False

    @classmethod
    def consultarPacientePorId(self, id, ti):
        try:
                return (Consulta()).consultarPacientePorId(id, ti)
        except:
            raise OperationalError

    @classmethod
    def agregarPaciente(self, idP, ti, name, last, gender, date, age, phone):
        if( Consulta.consultarPacientePorId(idP, ti) == None):
            Agregar.agregaPaciente(idP, ti, name, last, gender, datetime.datetime.strptime(date, "%d/%m/%y").date(), age, phone)
        else:
            raise Exception("El paciente ya existe")

    @classmethod
    def agregarDiagnostico(self, comentarios, paciente):
        Agregar.agregarDiagostico(comentarios, paciente)

    @classmethod
    def consultaDiagnostico(self, paciente):
        Consulta.consultaDiagnostico(paciente)

    #devuelve un arreglo con los datos de la senal pedida para el paciente
    @classmethod
    def cargarSenal(self, paciente_id, senal_id):
        try:
            return (Consulta()).consultarSenal(paciente_id, senal_id)
        except:
            raise OperationalError

    @classmethod
    def agregarSenal(self,id,   orden , data, diagnostico_id):
        Agregar.agregarSenal(id,  orden, data, diagnostico_id)


    @classmethod
    def consultarSenal(self, senal_id):

        r = []
        for d in Consulta.consultarSenal( senal_id):
            s = d.data
            for c in s.strip('[').strip(']').split(','):
                c = c.strip().strip("'")
                r.append(float(c))
        return r

    @classmethod
    def consultarMaxIdSenal(self):
        return Consulta.consularIdUltimaSenal()

    @classmethod
    def consularSenalesDelPaciente(self, paciente_id):
        return Consulta.consularSenalesDelPaciente(paciente_id)

    @classmethod
    def consultarSenalesDelDiagnostico(self, diagnostico_id):
        return  Consulta.consultarSenalesDelDiagnostico(diagnostico_id)


