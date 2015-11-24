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
birth = "10/06/94"

agregaPaciente("1020793768" , "CC" , "luis" , "felipe" , "M" , datetime.datetime.strptime(birth, "%d/%m/%y").date(), "300210593", 21)