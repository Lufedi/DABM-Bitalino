



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
    def __init__(self):
        pass

    @classmethod
    def consultarPacientePorId(self, id, ti):
        try:
                return (Consulta()).consultarPacientePorId(id, ti)
        except:
            raise OperationalError

    @classmethod
    def agregarPaciente(self, idP, ti, name, last, gender, date, age, phone):
        Agregar.agregaPaciente(idP, ti, name, last, gender, date, age, phone)

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
    def agregarSenal(self,id,   orden , data, paciente):
        try:
            print str(orden) +  " " + paciente
            Agregar.agregarSenal(id,  orden, data, paciente)
        except :
            raise OperationalError

    @classmethod
    def consultarSenal(self, paciente_id, senal_id):

        r = []
        for d in Consulta.consultarSenal(paciente_id, senal_id):
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