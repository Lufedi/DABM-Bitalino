__author__ = 'Pipe'









from Persistencia.Base import *


for s in Consulta.consularSenalesDelPaciente("1014270615"):
    print s.id


from  Logica.AplicacionBitalino import *

print AplicacionBitalino.consultarSenal("51669907" , 38)