__author__ = 'MariaAlejandraLuisFelipe'
from sqlalchemy import func, ForeignKey
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,DateTime
import datetime
from sqlalchemy.sql import table, column, select, update, insert, and_
from sqlalchemy import func


engine = create_engine('sqlite:///../Persistencia/BaseDeDatos.db', echo=True)
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
    orden =  Column(Integer,primary_key = True)
    data =  Column(String)
    diagnostico_id = Column(String, ForeignKey('diagnosticos.id'),primary_key = True, nullable=False)


    def __init__(self, id, orden, data, diagnostico_id):
        self.id = id
        self.orden = orden
        self.data =  data
        self.diagnostico_id = diagnostico_id


class Aplicacion(Base):
    __tablename__ = 'aplicacion'
    idtarjeta = Column(String, primary_key=True)

    def __init__(self, idtarjeta):
        self.idtarjeta = idtarjeta

class Diagnostico(Base):
    __tablename__ = 'diagnosticos'
    id = Column(Integer, primary_key= True, autoincrement=True)
    fecha = Column(Date)
    comentarios = Column(String, nullable=True)
    paciente = Column(String, ForeignKey('paciente.id') )

    def __init__(self, diag, paciente):
        self.fecha= func.current_date()
        self.comentarios= diag
        self.paciente = paciente

class Agregar():

    def __init__(self):
        pass
    @classmethod
    def agregaPaciente(self, idP, ti, name, lastname, gen, birth,phone, age):
        Base.metadata.create_all(engine)
        paciente=Paciente(idP, ti, name, lastname, gen, birth,phone, age)
        session.add(paciente)
        session.commit()
    @classmethod
    def agregarSenal(self, id,  orden , data, diagnostico_id):
        Base.metadata.create_all(engine)
        #p =  session.query(Paciente).filter(Paciente.id == pacienteId).all()
        #print (str(p) + ' - ' + str(pacienteId))
        print "id"
        print id
        print "orden"
        print orden
        print "data"
        print data
        print "pacienteId"
        print diagnostico_id

        senal = Senal(id,  orden, str(data), diagnostico_id)
        senal.diagnostico_id = diagnostico_id
        session.add(senal)
        session.commit()

    @classmethod
    def agregarAplicacion(self, idtarjeta):
        Base.metadata.create_all(engine)
        app = Aplicacion(idtarjeta)
        session.add(app)
        session.commit()

    @classmethod
    def agregarDiagostico(self, comentarios, paciente):
        Base.metadata.create_all(engine)
        dia = Diagnostico(comentarios, paciente)
        session.add(dia)
        session.commit()


class Consulta(object):
    def __init__(self):
        pass

    @classmethod
    def consultarDiagnosticosPaciente(self, paciente):
        return session.query(Diagnostico).filter(Diagnostico.paciente == paciente).all()
    @classmethod
    def consultarMaxIdDiagnostrico(self):
        res  =  session.query(func.max(Diagnostico.id)).first()[0]
        if res == None:
            res = 0
        return res
    @classmethod
    def consularIdUltimaSenal(self):
        res =  session.query(func.max(Senal.id)).first()[0]
        if res == None:
            res = 0
        return res
    @classmethod
    def consultarIdUltimoDiagnostico(self):
        res =  session.query(func.max(Diagnostico.id)).first()[0]
        if res == None:
            res = 0
        return res
    @classmethod
    def consultarPacientePorId(self, id, ti):
        try:
            return session.query(Paciente).filter(and_(Paciente.id == id), Paciente.ti == ti).first()
        except :
            raise OperationalError

    @classmethod
    def consultarPacientes(self):
        try:
            return  session.query(Paciente).filter().all()
        except:
            return 0

    @classmethod
    def consultarSenal(self, senal_id):

        return session.query(Senal).filter( Senal.id == senal_id ).order_by(Senal.orden).all()

    @classmethod
    def consularSenalesDelPaciente(self, paciente_id):
        try:
            return session.query(Senal).filter(Senal.paciente_id == paciente_id).group_by(Senal.id).all()
        except:
            raise OperationalError

    @classmethod
    def consultaDiagnostico(self, paciente_id):
        try:
            return session.query(Diagnostico).filter(Diagnostico.paciente==paciente_id).order_by(Diagnostico.fecha).all()
        except:
            raise OperationalError



