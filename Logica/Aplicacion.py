



from Persistencia.Base import *
from sqlalchemy import func
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,DateTime
import datetime
from sqlalchemy.sql import table, column, select, update, insert, and_

class Aplicacion():
    def __init__(self):
        pass

    def consultarPacientePorId(self, id):
        try:
            c = Consulta()
            c.consultarPacientePorId(id, ti)
        except:
            raise OperationalError

if __name__=="__main__":
    apl=Aplicacion()
