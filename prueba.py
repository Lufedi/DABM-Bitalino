__author__ = 'Pipe'




import pylab
from pylab import *
import Queue
import time
am=1000
xAchse=pylab.arange(0,am,1)
yAchse=pylab.array([0]*am)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("ECG")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,am,-1.5,1.5])
line1=ax.plot(xAchse,yAchse,'r-')
manager = pylab.get_current_fig_manager()

values=[]
values = [0 for x in range(am)]



'''def SinwaveformGenerator(arg):
  global values,T1,Konstant,T0
  #ohmegaCos=arccos(T1)/Ta
  #print "fcos=", ohmegaCos/(2*pi), "Hz"

  Tnext=((Konstant*T1)*2)-T0
  if len(values)%100>70:
    values.append(random()*2-1)
  else:
    values.append(Tnext)
  T0=T1
  T1=Tnext'''


q = Queue.Queue()
datarray = open("ecgsyn.dat")
for data in datarray:
  q.append(data.split(" ")[1])


def SinwaveformGenerator(arg):
  global values,T1,Konstant,T0,q
  values.append(q.popleft())

def RealtimePloter(arg):
  global values
  CurrentXAxis=pylab.arange(len(values)-am,len(values),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[-am:]))
  ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),-1.5,1.5])
  manager.canvas.draw()
  #manager.show()

timer = fig.canvas.new_timer(interval=1)
timer.add_callback(RealtimePloter, ())
timer2 = fig.canvas.new_timer(interval=1)
timer2.add_callback(SinwaveformGenerator, ())
timer.start()
timer2.start()
pylab.show()



