from Tkinter import * #importing the Tkinter libraries
import tkFont
from PIL import Image,ImageTk

def quit():
    import sys
    sys.exit()

class WIFI:
    def __init__(self, master):
        myfont = tkFont.Font(family="arial", size=10, weight=tkFont.BOLD)
        frame=Frame(master)
        frame.pack(expand=YES)
        border_frame=Frame(frame, borderwidth=40)
        border_frame.pack(expand=YES,side= BOTTOM)
        

# using the entry Widget
## Start attenuation
        self.lb2 = Label(frame, text="Start Atten. (dB)", font=myfont) # Creating a label
        self.lb2.grid(row=0, column=0)
        #self.lb2.pack(side=TOP)
        #self.e2=Entry(frame)
        #self.e2.pack(side=TOP)
        #self.e2.delete(0,END)
        #self.e2.insert(0," 0.0")
## Step size
        self.lb3 = Label(frame, text="Step Size (dB)", font=myfont) # Creating a label
        self.lb3.pack(side=TOP)
        self.e3=Entry(frame)
        self.e3.pack(side=TOP)
        self.e3.delete(0,END)
        self.e3.insert(0," 0.0")
        
## End Attenuation
        self.lb4 = Label(frame, text="End Attenuation(dB)", font=myfont) # Creating a label
        self.lb4.pack(side=TOP)
        self.e4=Entry(frame)
        self.e4.pack(side=TOP)
        self.e4.delete(0,END)
        self.e4.insert(0," 0.0")
                

#Using the Menubutton option # updating the displayed text ; not implemented
        self.mb=Menubutton(frame, text= ' Iperf Type ', relief=RAISED)
        self.mb.pack(side=BOTTOM)
        self.mb.menu=Menu(self.mb, tearoff=0)
        self.mb['menu']=self.mb.menu
        self.tcp=IntVar()
        self.udp=IntVar()
        self.mb.menu.add_checkbutton(label='TCP', variable=self.tcp)
        self.mb.menu.add_checkbutton(label='UDP', variable= self.udp)

#Using the radio button ## the mouse click option doesnot work
        v=IntVar()
        self.rad= Radiobutton(master,text='Disable attenuator', variable=v,value=1)
        self.rad.pack(anchor=W)


# using the Canvas widget to plot graphs
        #self.canv=Canvas(frame,width=200, height=100)
        #self.canv.pack()
        #self.canv.create_line(0,0,200,100)
        
root=Tk()
root.title('WI-FI measurements')
root.geometry("600x600")
WIFI(root)
root.mainloop()
