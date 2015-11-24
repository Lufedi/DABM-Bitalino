



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



    #devuelve un arreglo con los datos de la senal pedida para el paciente
    @classmethod
    def cargarSenal(self, paciente_id, senal_id):
        try:
            return (Consulta()).consultarSenal(paciente_id, senal_id)
        except:
            raise OperationalError
    @classmethod
    def agregarSenal(self,  orden , data, paciente):
        try:
            print str(orden) +  " " + paciente
            Agregar.agregarSenal( orden, data, paciente)
        except :
            raise OperationalError
    @classmethod
    def consultarSenal(self, paciente_id, senal_id):
        try:
            r = []
            for d in (Consulta()).consultarSenal(paciente_id, senal_id):
                s = d.data
                for c in s.strip('[').strip(']').split(','):
                    r.append(int(c))
            return r
        except:
            raise OperationalError

    @classmethod
    def consultarMaxIdSenal(self):
        return Consulta.consularIdUltimaSenal()
