__author__ = 'Pipe'




from Persistencia.Base import *
import pylab

#for s in Consulta.consularSenalesDelPaciente("1014270615"):
#    print s.id


for d in Consulta.consultarDiagnosticosPaciente("51669907"):
    print d.id


"""from  Logica.AplicacionBitalino import *
data =  AplicacionBitalino.consultarSenal( 43)

pylab.plot(data)
pylab.ylabel("Pulso")
pylab.xlabel("Tiempo")
pylab.show()

"""
#Agregar.agregarDiagostico("sadfsadfsadf", "1020793766")
