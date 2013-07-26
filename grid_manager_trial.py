#!/usr/bin/python
#Modificaiton  Date: 5/22/2013
import Tkinter
import tkFont
from PIL import Image, ImageTk
import sys

def quit():           #create a event when termination of the event is involved
    import sys
    sys.exit() 


#def callback_start(event):
class Wifi_only(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()    #Label


    

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


# Iperf Type
        self.label3= Tkinter.Label(self, text="Iperf Type")
        self.label3.grid(column=10,row=1,columnspan=10)
        self.mb=Tkinter.Menubutton(self, text= ' Mode ')
        self.mb.grid(column=10, row=2,columnspan=10)
        self.mb.menu=Tkinter.Menu(self.mb, tearoff=0)
        self.mb['menu']=self.mb.menu
        self.tcp=Tkinter.IntVar()
        self.udp=Tkinter.IntVar()
        self.mb.menu.add_checkbutton(label='TCP', variable=self.tcp)
        self.mb.menu.add_checkbutton(label='UDP', variable= self.udp)

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
        self.entry6 = Tkinter.Entry(self)
        self.entry6 = Tkinter.Entry(self)
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

        self.label8= Tkinter.Label(self, text="P2P client address")
        self.label8.grid(column=30,row=3,columnspan=1)
        self.entry8 = Tkinter.Entry(self)
        self.entry8 = Tkinter.Entry(self)
        self.entry8.delete(0,Tkinter.END)
        self.entry8.insert(0, "2.2.2.2")  
        self.entry8.grid(column=31, row=3, columnspan=5)

        self.label9= Tkinter.Label(self, text="TV P2P address")
        self.label9.grid(column=30,row=4,columnspan=1)
        self.entry9 = Tkinter.Entry(self)
        self.entry9 = Tkinter.Entry(self)
        self.entry9.delete(0,Tkinter.END)
        self.entry9.insert(0, "2.2.2.1")  
        self.entry9.grid(column=31, row=4, columnspan=5)


        self.label10= Tkinter.Label(self, text="P2P client Ethernet")
        self.label10.grid(column=30,row=5,columnspan=1)
        self.entry10 = Tkinter.Entry(self)
        self.entry10 = Tkinter.Entry(self)
        self.entry10.delete(0,Tkinter.END)
        self.entry10.insert(0, "192.168.1.202")  
        self.entry10.grid(column=31, row=5, columnspan=5)

# Start and the stop button
        self.btn = Tkinter.Button(self, text=" START", width=10, command=self.callback) #Create a  new button widget
        self.btn.grid(column=50, row= 3, columnspan=1)
        #self.btn.bind("<Button-1>",callback)
    
        self.btn = Tkinter.Button(self, text=" STOP",width=10,  command=self.callback_quit) #Create a  new button widget
        self.btn.grid(column=50, row= 4, columnspan=1)
        #self.btn.bind("<Button-1>",  callback_Stop)

        self.btn = Tkinter.Button(self, text=" CLEAR", width=10, command=self.callback_clear) #Create a  new button widget
        self.btn.grid(column=50, row= 5, columnspan=1)


    def callback_quit(self):
        self.sys.quit()    


    def callback(self):
        print self.entry1.get()
        print self.entry2.get()
        #print self.entry3.get()
        print self.entry4.get()
        print self.entry5.get()
        print self.entry6.get()
        print self.entry7.get()
        print self.entry8.get()
        print self.entry9.get()
        print self.entry10.get()



    def callback_clear(self):
        self.entry1.delete(0, Tkinter.END)
        self.entry2.delete(0, Tkinter.END)
        #self.entry3.delete(0, Tkinter.END)
        self.entry4.delete(0, Tkinter.END)
        self.entry5.delete(0, Tkinter.END)
        self.entry6.delete(0, Tkinter.END)
        self.entry7.delete(0, Tkinter.END)
        self.entry8.delete(0, Tkinter.END)
        self.entry9.delete(0, Tkinter.END)
        self.entry10.delete(0, Tkinter.END)
        
        #self.btn.bind("<Button-1>",  callback_Clear)



        self.label= Tkinter.Label(self, text="Iperf vs Time plot")
        self.label.grid(column=15, row= 19, columnspan=1)

# Inserting the Canvas
        self.graph1 = Tkinter.Canvas(self, width=200, height=100)
        self.graph1.grid(column=10, row=20, columnspan=10)
        self.graph1.create_rectangle(10, 25, 150, 75, fill="blue")

if __name__ == "__main__":
    app = Wifi_only(None)
    app.title('WiFi Measurements')
    app.mainloop()
