




from Logica import bitalino

__author__ = 'Pipe'

from Logica import *
class Adaptador(object):

    def __init__(self):
        self.N = 100
        self.device = None
    def encontrarDispositivos(self):
        dispositivos =  bitalino.find()
        return  dispositivos
    #retorna el dispositivo ya conectado
    def conectarseADispositivo(self, mac):
        self.device = bitalino.BITalino(mac)
        return self.device
    #canales : arreglos de canales que se van a leer de la tarjeta
    def comenzar(self, canales):
        self.device.start(canales)
    def terminar(self, terminar):
        self.stop()
        self.device.close()
    #obtiene N registros en los canales seleccionados
    def leer(self):
        return self.devive.read(self.N)



#a = Adaptador()
#print (a.encontrarDispositivos())

#a.conectarseADispositivo("FC:A1:3E:B7:37:FD")