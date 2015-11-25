__author__ = 'Pipe'









from Persistencia.Base import *


for s in Consulta.consularSenalesDelPaciente("1014270615"):
    print s.id


from  Logica.AplicacionBitalino import *

data =  AplicacionBitalino.consultarSenal("1020793766" , 17)


import pylab

pylab.plot(data)
pylab.ylabel("Pulso")
pylab.xlabel("Tiempo")
pylab.show()
