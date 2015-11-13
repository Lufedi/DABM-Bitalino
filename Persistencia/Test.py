__author__ = 'Pipe'

from Base import *

engine = create_engine('sqlite:///../Persistencia/BaseDeDatos.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

def agregaPaciente( idP, ti, name, lastname, gen, birth,phone, age):
    Base.metadata.create_all(engine)
    paciente=Paciente(idP, ti, name, lastname, gen, birth,phone, age)
    session.add(paciente)
    session.commit()
import datetime
agregaPaciente("1020793766" , "CC" , "luis" , "felipe" , "M" , datetime.datetime.now(), "300210593", 21)