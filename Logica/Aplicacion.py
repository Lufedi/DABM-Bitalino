__author__ = 'MariaAlejandraBlancoLuisFelipeDiaz'
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
        self.add=Agregar()
    def agregaPaciente(self, idP, ti, name, last, gender, birth, age, phone):
        self.add.agregaPaciente(idP, ti, name, last, gender, datetime.datetime.strptime(birth, "%d %b %y").date(), age, phone)

if __name__=="__main__":
    apl=Aplicacion()
    apl.agregaPaciente("1014270644", "CC", "Alejandro", "Negro", "F", "05 Oct 95", 20, "3122984750")
#add.agregaPaciente("1014270644", "CC", "Alejandro", "Negro", "F", datetime.datetime.strptime("05 Oct 95", "%d %b %y").date(), 20, "3122984750")