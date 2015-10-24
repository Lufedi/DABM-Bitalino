__author__ = 'MariaAlejandraLuisFelipe'
from sqlalchemy import func
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,DateTime
import datetime
from sqlalchemy.sql import table, column, select, update, insert, and_

engine = create_engine('sqlite:///BaseDeDatos.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Paciente(Base):
    __tablename__ = 'paciente'
    id = Column(String, primary_key=True)
    ti=Column(String)
    nombres=Column(String)
    apellidos=Column(String)
    genero=(String)
    fechaNacimiento=Column(Date)
    edad=Column(Integer)
    telefono=Column(String)
    fechaIngreso=Column(String)

    def __init__(self, idP, ti, name, lastname, gen, birth,phone, age):
        self.id=idP ; self.ti=ti ; self.nombres=name
        self.apellidos=lastname ; self.genero=gen
        self.fechaNacimiento=birth ; self.telefono=phone
        self.edad = age ; self.fechaIngreso=func.current_date()

    def __repr__(self):
       return "<Auto('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.ti,
                                                                              self.nombres, self.apellidos, self.genero,
                                                                              self.fechaNacimiento, self.edad,
                                                                              self.telefono, self.fechaIngreso)

class Agregar():
    def agregaPaciente(self, idP, ti, name, lastname, gen, birth,phone, age):
        Base.metadata.create_all(engine)
        paciente=Paciente(idP, ti, name, lastname, gen, birth,phone, age)
        session.add(paciente)
        session.commit()






