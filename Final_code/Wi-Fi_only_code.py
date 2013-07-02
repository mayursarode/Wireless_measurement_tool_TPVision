#!/usr/bin/python
#Modificaiton  Date: 6/7/2013
# Adding the file handling option
# Added directory creation command
# Added UDP fucntionality
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
import commands
import serial
import time
########################## Function to Quit the UI###################################################

def callback_quit():           #create a event when termination of the event is involved
        os._exit(0) 
############################## End###################################################################


def print_graph(raw_f, self):
        x=[]  ###local variable
        y=[]  ###Local variables
        #f=open("/home/wireless/Documents/Wireless_measurement_tool_TPVision/shieldroom_20mhz_external_TCP_0dB_n.txt")
        f=open(raw_f,"r")
        while 1:
            line=f.readline()
            a14= line.find('-',0)
            a15= line.find('sec',0)
            d=line[a14+1:a15]
            size=len(d)
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
        fig= plt.figure(figsize=(6,4), dpi=100)
        #ax=subplot(1,1,1)
        plt.plot(x_flt, y)
        plt.title('Iperf time plot')
        plt.xlabel('Time [sec]')
        plt.ylabel ('Throughput [Mbps]')
        self.dataplot = FigureCanvasTkAgg(fig, master=self)
        self.dataplot.show()
        self.dataplot.get_tk_widget().grid(column=20,row=20,columnspan=1)
        #dataplot.show()
        del x[:]
        del y[:]
        f.close()


        
# Add the code to  store the iperf results in seperate files

def change_attn(a2):
        s_att= serial.Serial(port='/dev/ttyS0',baudrate=9600, bytesize=8, parity='N', stopbits=1,timeout=1)
        s_w1= 'sa1 '+ str(a2)
        s_w2= 'sa2 '+ str(a2)
        s_w3= 'sa3 '+ str(a2)
        s_w4= 'sa4 '+ str(a2)
        
        s_att.write(s_w1)
        s_read=s_att.readline()
        print(s_read)        
        s_att.write(s_w2)
        s_read=s_att.readline()
        print(s_read)        
        s_att.write(s_w3)
        s_read=s_att.readline()
        print(s_read)        
        s_att.write(s_w4)
        s_read=s_att.readline()
        print(s_read)
        
########################### Function to create TCP Iperf for Wifi only##################################
def Wifi_SSH_TCP(raw_f,attn,a5,a7,a9,a_window):
        #print a5 # Run time
        #print a7 # TV wifi address
        #print a9 # Client Wifi address
        print raw_f
        f_raw=open(raw_f,"w")
        cmd_sr = "iperf -i 0.5" + " -c " + a7  + " -t " + a5  # The TV side
        cmd_si= "iperf -s -w "+ a_window                            # The client side
        commands.getoutput(cmd_si)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=a9, username='wireless',password='wireless',port=22)  
        stdin, stdout, stderr = ssh.exec_command(cmd_sr)
        #sprint stdout.readlines()
        #string.split(data, '\n')
        output= stdout.readlines()
        a1= len(output)
        i=1
        while (i<a1):
            print output[i]
            f_raw.write(output[i])
            i=i+1
            
        f_raw.close()
        ssh.close()

#################################END#######################################################################
#############################################Function to create UDP Iperf for WIfi only
def Wifi_SSH_UDP(raw_f,attn,a5,a7,a9,a_udp):
        print raw_f
        f_raw=open(raw_f,"w")
        cmd_sr = "iperf" + " -c " + a7 +" -i 0.5" + " -u  -b "+ a_udp + " -t " + a5   # The TV side
        cmd_si= "iperf -s -u -i 0.5 "                       #  The client side
        print cmd_sr
        print cmd_si
        commands.getoutput(cmd_si)
        time.sleep(20)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=a9, username='wireless',password='wireless',port=22)  
        stdin, stdout, stderr = ssh.exec_command(cmd_sr)
        #print stdout.readlines()
        #string.split(data, '\n')
        output= stdout.readlines()
        #print output
        a1= len(output)
        i=1
        while (i<a1):
            print output[i]
            f_raw.write(output[i])
            i=i+1 
        f_raw.close()
        ssh.close()

#def callback_start(event):        
class Wifi_only(Tkinter.Tk):
        
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()    #Label

##################################################### Plotting the graph######################################################################
        
####################################### end of plotting thr graph##############################################################################

        # Attenuation Block
        self.label1= Tkinter.Label(self, text="Attenuator Settings ")
        self.label1.grid(column=2,row=1,columnspan=1,sticky='EW')
        self.label1=Tkinter.Label(self, text="Start Atten. (dB)")
        self.label1.grid(column=1,row=2,columnspan=1,sticky='EW')
        self.entry1 = Tkinter.Entry(self)
        self.entry1.delete(0,Tkinter.END)
        self.entry1.insert(0, "0")
        self.entry1.grid(column=2, row=2, columnspan=1)

        #Step Attenuation size
        self.label2=Tkinter.Label(self, text="Step (dB)")
        self.label2.grid(column=1,row=3,columnspan=1,sticky='EW')
        self.entry2 = Tkinter.Entry(self)
        self.entry2.delete(0,Tkinter.END)
        self.entry2.insert(0, "3")
        self.entry2.grid(column=2, row=3, columnspan=1)

        # Stop  Attenuation
        self.label3=Tkinter.Label(self, text="Stop (dB)")
        self.label3.grid(column=1,row=4,columnspan=1,sticky='EW')
        self.entry3 = Tkinter.Entry(self)
        self.entry3.delete(0,Tkinter.END)
        self.entry3.insert(0, "60")
        self.entry3.grid(column=2, row=4, columnspan=1)

        # Iperf Type
        self.var_iperf=Tkinter.StringVar(self)
        self.var_iperf.set("TCP")
        self.option= Tkinter.OptionMenu(self, self.var_iperf, "TCP", "UDP");
        self.option.grid(column=10, row=2, columnspan=10)
    
        #Iperf Start Time
        self.label4=Tkinter.Label(self, text= 'Start time [sec]')
        self.label4.grid(column=10,row=3,columnspan=1)
        self.entry4 = Tkinter.Entry(self)
        self.entry4.delete(0,Tkinter.END)
        self.entry4.insert(0, "5")  
        self.entry4.grid(column=11, row=3, columnspan=5)
        
        # Iperf Stop Time
        self.label5=Tkinter.Label(self, text= 'Run Time [sec]')
        self.label5.grid(column=10,row=4,columnspan=1)
        self.entry5 = Tkinter.Entry(self)
        self.entry5.delete(0,Tkinter.END)
        self.entry5.insert(0, "6")  
        self.entry5.grid(column=11,row=4,columnspan=5)


        # Iperf UDP Bandwidth
        self.label_udp=Tkinter.Label(self, text= ' UDP Bandwidth ')
        self.label_udp.grid(column=10,row=5,columnspan=1)
        self.entry_udp= Tkinter.Entry(self)
        self.entry_udp.delete(0,Tkinter.END)
        self.entry_udp.insert(0, "10m")  
        self.entry_udp.grid(column=11,row=5,columnspan=5)


     # TCP/IP Window size
        self.label_window=Tkinter.Label(self, text= 'Window size ')
        self.label_window.grid(column=10,row=6,columnspan=1)
        self.entry_window= Tkinter.Entry(self)
        self.entry_window.delete(0,Tkinter.END)
        self.entry_window.insert(0, "512k")  
        self.entry_window.grid(column=11,row=6,columnspan=5)


        # File name to store the raw data
        self.label6= Tkinter.Label(self, text="Give path and filename to read and write")
        self.label6.grid(column=20,row=1,columnspan=1)
        self.entry6 = Tkinter.Entry(self, width=40)
        self.entry6.delete(0,Tkinter.END)
        self.entry6.insert(0, "/home/wireless/Documents/Wireless_measurement_tool_TPVision/measurement_6-10-2013/")  
        self.entry6.grid(column=20, row=2, columnspan=10)

        # IP addresses
        self.label7= Tkinter.Label(self, text="IP addresses of the Devices")
        self.label7.grid(column=30,row=1,columnspan=15)
        self.label7= Tkinter.Label(self, text="AP Wifi address")
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

        self.label9= Tkinter.Label(self, text="TV Wifi address")
        self.label9.grid(column=30,row=4,columnspan=1)
        self.entry9 = Tkinter.Entry(self)
        self.entry9 = Tkinter.Entry(self)
        self.entry9.delete(0,Tkinter.END)
        self.entry9.insert(0, "192.168.1.200")  
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
        self.btn = Tkinter.Button(self, text=" START", width=10, command=self.callback) #Create a  new button widget
        self.btn.grid(column=50, row= 3, columnspan=1)
        #self.btn.bind("<Button-1>",callback)
    
        self.btn = Tkinter.Button(self, text=" STOP",width=10,  command=callback_quit) #Create a  new button widget
        self.btn.grid(column=50, row= 4, columnspan=1)
        self.btn.bind("<Button-1>",  callback_quit)

        self.btn = Tkinter.Button(self, text=" CLEAR", width=10, command=self.callback_clear) #Create a  new button widget
        self.btn.grid(column=50, row= 5, columnspan=1)

# Drop down Menu to select the measurement type
        self.var_exp=Tkinter.StringVar(self)
        self.var_exp.set("Wifi only")
        self.option= Tkinter.OptionMenu(self, self.var_exp, "Wifi only    ", "Wifi with P2P GO" ," Wifi with P2P GO with traffic");
        self.option.grid(column=2, row=5, columnspan=50)
          
    def callback_quit(self):
        self.sys.quit()    

    def callback(self):
        a1=self.entry1.get() ## Set attenuation
        a2=self.entry2.get() ##Set attenuation step
        a3=self.entry3.get() ## Stop attenuation
        a4=self.entry4.get() ## Start time
        a5= self.entry5.get() ##Run time
        a6=self.entry6.get() ## path
        a7=self.entry7.get() ## TV wifi address
        a8=self.entry8.get() ##TV P2P address
        a9=self.entry9.get() ##Client Wifi address
        a10=self.entry10.get() ##Client P2P address
        a11=self.entry10.get()## p2P client Ethernet
        a_udp=self.entry_udp.get()
        a_window=self.entry_window.get()
        a12=self.var_iperf.get()
        print a12
        a13= self.var_exp.get()    ## Experiment Option
        
        attn=int(a1)
        attn_st=int(a2)
        try:
                os.makedirs(a6)
        except OSError:
                pass
        
        if a13 == "Wifi only" and a12=="TCP":
           while(attn <= int(a3)):
              raw_f=a6+"shieldroom_20mhz_external_TCP_"+str(attn)+"dB.txt"
              Wifi_SSH_TCP(raw_f,attn,a5,a7,a9,a_window)
              change_attn(attn)
              attn=attn+attn_st
              print print_graph(raw_f,self)
        elif a13=="Wifi only" and a12=="UDP":
           while(attn <= int(a3)):
              raw_f=a6+"shieldroom_20mhz_external_UDP_"+str(attn)+"dB.txt"
              Wifi_SSH_UDP(raw_f,attn,a5,a7,a9,a_udp)
              change_attn(attn)
              attn=attn+attn_st
              print print_graph(raw_f,self)
        else:
              callback_quit()

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
    path= "/home/wireless/Documents/Wireless_measurement_tool_TPVision/TPvision-logo.tiff"
    img =ImageTk.PhotoImage(Image.open(path))
    panel = Tkinter.Label(app, image = img)
    panel.grid(column=50, row=40, columnspan=10)
    app.mainloop()
