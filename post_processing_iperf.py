#Post processing of results
#Plotting the iperf measurements wrt time for each attenuation level
#Date 6/3/2013
import Tkinter
import tkFont
from PIL import Image, ImageTk
import sys
import paramiko
import sys
import Image, ImageTk
import os
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from pylab import *


master=Tk()
master.title("Matplotlib embedded in Tkinter")
#Opeining the file with contains the iperf raw data
# Open the file which contains the iperf file
f=open("shieldroom_20mhz_external_TCP_0dB.txt")
x=[]
y=[]

while 1:
    line=f.readline()
    ## Extracting seconds
    a1= line.find('-',0)
    a2= line.find('sec',0)
    d=line[a1+1:a2]
    size=len(d)
    #print size
    if size < 8 and size >0 :
      x.append((d))  
    if not line:
        break
## Extracting the Data rate
    a3=line.find('Mbits/sec') or line.find('Kbits/sec') or line.find('bits/sec')
    if (line.find('Mbits/sec')!= -1):
        a3=line.find('Mbits/sec')
        d1=float(line[a3-5:a3])
        y.append((d1))
    elif(line.find('Kbits/sec')!= -1):
        a3=line.find('Kbits/sec')
        d1=float(line[a3-5:a3])*0.001
        y.append((d1))
    elif (line.find('bits/sec')!= -1):
        a3=line.find('bits/sec')
        d1=float(line[a3-5:a3])*0.000001
        y.append((d1))
        
x1=((''.join(x)))
x_flt = [float(n) for n in x1.split()]

fig= plt.figure()
#ax=subplot(1,1,1)
plt.plot(x_flt, y)
plt.title('Iperf time plot')
plt.xlabel('Time [sec]')
plt.ylabel('Throughput [Mbps]')
plt.show()
f.close()
