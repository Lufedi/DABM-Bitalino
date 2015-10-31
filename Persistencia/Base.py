__author__ = 'MariaAlejandraLuisFelipe'
from sqlalchemy import func, ForeignKey
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,DateTime
import datetime
from sqlalchemy.sql import table, column, select, update, insert, and_

engine = create_engine('sqlite:///Persistencia/BaseDeDatos.db', echo=True)
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
class Senal(Base):
    __tablename__ = 'senales'
    id =  Column(Integer, primary_key = True )
    orden =  Column(Integer)
    data =  Column(String)
    paciente_id = Column(String, ForeignKey('paciente.id'))

    def __init__(self, id, orden, data, paciente):
        self.id = id
        self.orden = orden
        self.data =  data
        self.paciente = paciente


class Aplicacion(Base):
    __tablename__ = 'aplicacion'
    idtarjeta = Column(String, primary_key=True)

    def __init__(self, idtarjeta):
        self.idtarjeta = idtarjeta

class Diagnostico(Base):
    __tablename__ = 'diagnosticos'
    id = Column(Integer, primary_key= True, autoincrement=True)
    fecha = Column(Date)
    comentarios = Column(String)
    paciente = Column(String, ForeignKey('paciente.id') )

    def __init__(self,  fecha, comentarios, paciente):
        self.fecha = fecha
        self.comentarios = comentarios
        self.paciente =  paciente


class Agregar():
    def agregaPaciente(self, idP, ti, name, lastname, gen, birth,phone, age):
        Base.metadata.create_all(engine)
        paciente=Paciente(idP, ti, name, lastname, gen, birth,phone, age)
        session.add(paciente)
        session.commit()

    def agregarSenal(self, id, orden , data, paciente):
        Base.metadata.create_all(engine)
        senal = Senal(id, orden, data, paciente)
        session.add(senal)
        session.commit()

    def agregarAplicacion(self, idtarjeta):
        Base.metadata.create_all(engine)
        app = Aplicacion(idtarjeta)
        session.add(app)
        session.commit()

    def agregarDiagostico(self, fecha, comentarios, paciente):
        Base.metadata.create_all(engine)
        dia = Diagnostico(fecha, comentarios, paciente)
        session.add(dia)
        session.commit()
