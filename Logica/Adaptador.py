from Logica import bitalino


from Logica import *
class Adaptador(object):

    def __init__(self):
        self.N = 100
        self.device = None

    #Retorna una lista de los dispositivos que encuentra por bluetooth
    def encontrarDispositivos(self):
        dispositivos =  bitalino.find()
        return  dispositivos

    #Se crea la conexion con el dispositivo
    #Retorna el dispositivo ya conectado
    def conectarseADispositivo(self, mac):
        self.device = bitalino.BITalino(mac)
        return self.device

    # prende la tareja y empieza a recibir senales en los canales que se le indiquen
    # canales : arreglos de canales que se van a leer de la tarjeta
    def comenzar(self, canales):
        self.device.start(canales)

    #Apaga los sensores de lectura de la tarjeta
    def terminar(self, terminar):
        self.stop()
        self.device.close()

    #obtiene N registros en los canales seleccionados
    def leer(self):
        return self.devive.read(self.N)

#a = Adaptador()
#print (a.encontrarDispositivos())
#a.conectarseADispositivo("FC:A1:3E:B7:37:FD")