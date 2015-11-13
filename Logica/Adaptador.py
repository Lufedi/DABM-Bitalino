from Logica import bitalino


from Logica import *
class Adaptador(object):

    def __init__(self):
        self.N = 25
        self.SampligRate = 1000
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
    def comenzar(self,  canales):
        self.device.start(self.SampligRate , canales)

    #Apaga los sensores de lectura de la tarjeta
    def terminar(self):
        self.device.stop()

    #obtiene N registros en los canales seleccionados
    def leer(self):
        return self.device.read(self.N)


def testadaptador():
    a = Adaptador()
    #print (a.encontrarDispositivos())
    a.conectarseADispositivo("98:D3:31:B2:12:18")
    a.comenzar([0])
    res =[]
    cont =20
    import time
    while ( cont != 0):
        data=a.leer()
        cont-= 1
        res.append(data[:,5])
        time.sleep(1000)
        print("termino de leer linea")


    #SeqN = data[0,:]
    #D0 = data[1,:]
    #D1 = data[2,:]
    #D2 = data[3,:]
    #D3 = data[4,:]
    #A0 = data[5,:]
    #A3 = data[6,:]
    #for d in data:
    #    print d
    #print"donde"
    #EMG = data[:,5]
    print res

    #print SeqN
    #print D0
    #print D1
    #print D2
    #print D3
    #print A0
    #print A3
    #print "conected"
    import pylab
    pylab.xlabel("X")
    pylab.ylabel("Y")
    pylab.plot(res)
    pylab.show()

    a.terminar()
