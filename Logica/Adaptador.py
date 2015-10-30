from Logica import bitalino

__author__ = 'Pipe'

from Logica import *
class Adaptador(object):

    def encontrarDispositivos(self):
        dispositivos =  bitalino.find()
        return  dispositivos
    #retorna el dispositivo ya conectado
    def conectarseADispositivo(self, mac):
        device = bitalino.BITalino(mac)
        device.start(1000, [0])
        print(device.read(15))
        return device
#a = Adaptador()
#print (a.encontrarDispositivos())

#a.conectarseADispositivo("FC:A1:3E:B7:37:FD")