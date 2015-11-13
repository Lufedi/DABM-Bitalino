from Logica import bitalino


from Logica import *
import Queue
import threading
class Reader(threading.Thread):

    def __init__(self, stream):
        threading.Thread.__init__(self)
        self.N = 100
        self.SampligRate = 1000
        self.device = None
        self.stream = stream
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



    def run(self):
        print "Soy el hilo"

        #print (a.encontrarDispositivos())
        self.conectarseADispositivo("98:D3:31:B2:12:18")
        self.comenzar([0])
        res = [0]
        cont =30
        import time
        while ( cont > 0):
            print "leyendo"
            data=self.leer()
            cont-= 1

            for x in data[:,5]:
                print(x)
                print("----")
                print((x-500)/333)
                self.stream.put((x-500)/333)
            print("dos")
            #res.append(array(data[:,5]))
            time.sleep(2)
            print("termino de leer linea")
        print self.stream
        self.terminar()


import threading

class Adaptador(object):
    def __init__(self):
        self.input = Queue.Queue()
    def comenzarAGraficar(self):
        hilo = Reader(self.getInputStream())
        hilo.start()

    def getInputStream(self):
        return self.input
    def paraDeGraficar(self):
        pass

def testadaptador():

    q = Queue.Queue()
    #datarray = open("..\ecgsyn.dat")
    #for data in datarray:
    #self.q.append(data.split(" ")[1])
    #    q.put(data.split(" ")[1])
    a = Reader(q)
    a.conectarseADispositivo("98:D3:31:B2:12:18")
    a.comenzar([0])
    res = [0]
    cont =5
    import time
    '''while ( cont > 0):
        print "leyendo"
        data=a.leer()
        cont-= 1
        for x in data[:,5]:
            res.append( x)
        print("dos")
        #res.append(array(data[:,5]))
        time.sleep(2)
        print("termino de leer linea")
    '''
    data = a.leer()
    res = data[:,5]


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
#testadaptador()