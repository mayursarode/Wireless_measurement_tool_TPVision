#!/usr/bin/python
#Modificaiton  Date: 5/22/2013
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

########################## Function to Quit the UI###################################################

def callback_quit():           #create a event when termination of the event is involved
        os.exit() 
############################## End###################################################################
    
########################### Function to create Iperf for Scenario 1##################################
def Wifi_SSH(a7,a9):
        print a7
        print a9
        cmd_sr = "iperf -t 6 -i 0.5" + " -c " + a7 # The TV side
        cmd_si= "iperf -s -w 512k"                 # The client side
        os.system('cmd_ si')
         #cmd="ls"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.1.100', username='wireless',password='wireless',port=22)  
        stdin, stdout, stderr = ssh.exec_command(cmd_sr)
        print stdout.readlines()
        #string.split(data, '\n')
        ssh.close()
#################################END#################################################################

        #def callback_start(event):
        
class Wifi_only(Tkinter.Tk):
    def __init__(self,parent):

        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()    #Label
        print "step"

## Plotting the graph
        
        x=[]
        y=[]
        f=open("shieldroom_20mhz_external_TCP_0dB.txt")
        while 1:
            line=f.readline()
            ## Extracting seconds
            a14= line.find('-',0)
            a15= line.find('sec',0)
            d=line[a14+1:a15]
            size=len(d)
            #print size
            if size < 8 and size >0 :
              x.append((d))  
            if not line:
                break
            ## Extracting the Data rate
            a16=line.find('Mbits/sec') or line.find('Kbits/sec') or line.find('bits/sec')
            if (line.find('Mbits/sec')!= -1):
                a16=line.find('Mbits/sec')
                d1=float(line[a16-5:a16])
                y.append((d1))
            elif(line.find('Kbits/sec')!= -1):
                a16=line.find('Kbits/sec')
                d1=float(line[a16-5:a16])*0.001
                y.append((d1))
            elif (line.find('bits/sec')!= -1):
                a16=line.find('bits/sec')
                d1=float(line[a16-5:a16])*0.000001
                y.append((d1))
        
        x1=((''.join(x)))
        x_flt = [float(n) for n in x1.split()]
        #print x_flt
        #print y
        fig= plt.figure(figsize=(6,5), dpi=100)
        #ax=subplot(1,1,1)
        plt.plot(x_flt, y)
        plt.title('Iperf time plot')
        plt.xlabel('Time [sec]')
        plt.ylabel ('Throughput [Mbps]')
        self.dataplot = FigureCanvasTkAgg(fig, master=self)
        self.dataplot.show()
        self.dataplot.get_tk_widget().grid(column=20,row=20,columnspan=1)
        #dataplot.show()
        f.close()
       

# Attenuation Block
        self.label1= Tkinter.Label(self, text="Attenuator Settings ")
        self.label1.grid(column=2,row=1,columnspan=1,sticky='EW')

        self.label1=Tkinter.Label(self, text="Start Atten. (dB)")
        self.label1.grid(column=1,row=2,columnspan=1,sticky='EW')
        
        # text Box
        self.entry1 = Tkinter.Entry(self)
        self.entry1.delete(0,Tkinter.END)
        self.entry1.insert(0, "0.0")
        #start_attn=self.entry.get()
        #print start_attn
        self.entry1.grid(column=2, row=2, columnspan=1)

        #Label
        self.label2=Tkinter.Label(self, text="Step (dB)")
        self.label2.grid(column=1,row=3,columnspan=1,sticky='EW')
        self.entry2 = Tkinter.Entry(self)
        self.entry2.delete(0,Tkinter.END)
        self.entry2.insert(0, "0.0")
        #stop_attn=self.entry.get()
        self.entry2.grid(column=2, row=3, columnspan=1)

        self.var_iperf=Tkinter.StringVar(self)
        self.var_iperf.set("TCP")
        #self.var.get()
        self.option= Tkinter.OptionMenu(self, self.var_iperf, "TCP", "UDP");
        self.option.grid(column=10, row=2, columnspan=10)
    
        
        self.label4=Tkinter.Label(self, text= 'Start time')
        self.label4.grid(column=10,row=3,columnspan=1)
        self.entry4 = Tkinter.Entry(self)
        self.entry4.delete(0,Tkinter.END)
        self.entry4.insert(0, "5")  
        self.entry4.grid(column=11, row=3, columnspan=5)
        

        self.label5=Tkinter.Label(self, text= 'Run Time')
        self.label5.grid(column=10,row=4,columnspan=1)
        self.entry5 = Tkinter.Entry(self)
        self.entry5.delete(0,Tkinter.END)
        self.entry5.insert(0, "125")  
        self.entry5.grid(column=11,row=4,columnspan=5)


# File name to store the raw data
        self.label6= Tkinter.Label(self, text="Give path and filename to read and write")
        self.label6.grid(column=20,row=1,columnspan=1)
        self.entry6 = Tkinter.Entry(self, width=40)
        self.entry6.delete(0,Tkinter.END)
        self.entry6.insert(0, "C:/Doucments/measurements")  
        self.entry6.grid(column=20, row=2, columnspan=10)

# IP addresses
        self.label7= Tkinter.Label(self, text="IP addresses of the Devices")
        self.label7.grid(column=30,row=1,columnspan=15)
        self.label7= Tkinter.Label(self, text="TV Wifi address")
        self.label7.grid(column=30,row=2,columnspan=1)
        self.entry7 = Tkinter.Entry(self)
        self.entry7 = Tkinter.Entry(self)
        self.entry7.delete(0,Tkinter.END)
        self.entry7.insert(0, "192.168.1.100")  
        self.entry7.grid(column=31,row=2,columnspan=5)

        self.label8= Tkinter.Label(self, text="TV P2P address")
        self.label8.grid(column=30,row=3,columnspan=1)
        self.entry8 = Tkinter.Entry(self)
        self.entry8 = Tkinter.Entry(self)
        self.entry8.delete(0,Tkinter.END)
        self.entry8.insert(0, "2.2.2.1")  
        self.entry8.grid(column=31, row=3, columnspan=5)

        self.label9= Tkinter.Label(self, text="Client Wifi address")
        self.label9.grid(column=30,row=4,columnspan=1)
        self.entry9 = Tkinter.Entry(self)
        self.entry9 = Tkinter.Entry(self)
        self.entry9.delete(0,Tkinter.END)
        self.entry9.insert(0, "192.168.1.101")  
        self.entry9.grid(column=31, row=4, columnspan=5)

        self.label10= Tkinter.Label(self, text="Client P2P address")
        self.label10.grid(column=30,row=5,columnspan=1)
        self.entry10 = Tkinter.Entry(self)
        self.entry10 = Tkinter.Entry(self)
        self.entry10.delete(0,Tkinter.END)
        self.entry10.insert(0, "2.2.2.2")  
        self.entry10.grid(column=31, row=5, columnspan=5)
   
     

        self.label11= Tkinter.Label(self, text="P2P client Ethernet")
        self.label11.grid(column=30,row=6,columnspan=1)
        self.entry11 = Tkinter.Entry(self)
        self.entry11 = Tkinter.Entry(self)
        self.entry11.delete(0,Tkinter.END)
        self.entry11.insert(0, "192.168.1.202")  
        self.entry11.grid(column=31, row=6, columnspan=5)

# Start and the stop button
        self.btn = Tkinter.Button(self, text=" START", width=10, command=self.callback,) #Create a  new button widget
        self.btn.grid(column=50, row= 3, columnspan=1)
        #self.btn.bind("<Button-1>",callback)
    
        self.btn = Tkinter.Button(self, text=" STOP",width=10,  command=callback_quit) #Create a  new button widget
        self.btn.grid(column=50, row= 4, columnspan=1)
        self.btn.bind("<Button-1>",  callback_quit)

        self.btn = Tkinter.Button(self, text=" CLEAR", width=10, command=self.callback_clear) #Create a  new button widget
        self.btn.grid(column=50, row= 5, columnspan=1)

# Drop down Menu to select the measurement type
        self.var=Tkinter.StringVar(self)
        self.var.set("Wifi only")
        self.var.get()

        self.option= Tkinter.OptionMenu(self, self.var, "Wifi only    ", "Wifi with P2P GO" ," Wifi with P2P GO with traffic");
        self.option.grid(column=2, row=5, columnspan=50)
          

    def callback_quit(self):
        self.sys.quit()    


    def callback(self):
        a1=self.entry1.get() ## Set attenuation
        a2=self.entry2.get() ##Set attenuation step
        #print self.entry3.get()
        a4=self.entry4.get() ## Start time
        a5= self.entry5.get() ##Run time
        a6=self.entry6.get() ## path
        a7=self.entry7.get() ## TV wifi address
        a8=self.entry8.get() ##TV P2P address
        a9=self.entry9.get() ##Client Wifi address
        a10=self.entry10.get() ##Client P2P address
        a11=self.entry10.get()## p2P client Ethernet
        a12= self.var.get() 
        a13=self,
        #print a10
        if a12 == "Wifi only":
           Wifi_SSH(a7,a9)
        #else:
         #  exit()
      

    def callback_clear(self):
        self.entry1.delete(0, Tkinter.END)
        self.entry2.delete(0, Tkinter.END)
        self.entry4.delete(0, Tkinter.END)
        self.entry5.delete(0, Tkinter.END)
        self.entry6.delete(0, Tkinter.END)
        self.entry7.delete(0, Tkinter.END)
        self.entry8.delete(0, Tkinter.END)
        self.entry9.delete(0, Tkinter.END)
        self.entry10.delete(0, Tkinter.END)
        self.entry11.delete(0, Tkinter.END)

        self.label= Tkinter.Label(self, text="Iperf vs Time plot")
        self.label.grid(column=15, row= 19, columnspan=1)

# Inserting the Canvas
        

if __name__ == "__main__":
    app = Wifi_only(None)
    app.title('WiFi Measurements')
    #Inserting TPVision Label
    path= 'C:\Users\mayur.sarode\Pictures\TpVision-logo.png'
    img =ImageTk.PhotoImage(Image.open(path))
    panel = Tkinter.Label(app, image = img)
    panel.grid(column=50, row=40, columnspan=10)
    app.mainloop()
