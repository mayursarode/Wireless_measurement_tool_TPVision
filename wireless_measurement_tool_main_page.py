# Header files and constants
from Tkinter import * #importing the Tkinter libraries
import tkFont
from PIL import Image,ImageTk
import urllib2
import webbrowser
import os

new=2
url="http://192.168.1.1"

def quit():           #create a event when termination of the event is involved
    import sys; sys.exit()

def callback_Wifi_measurement(event):
            root1=Tk()
            frame=Frame(root1,width=1000, height=1000)
            frame.pack()
            root1.mainloop()

def callback_Video_benchmarking(event):
            root2=Tk()
            frame=Frame(root2,width=1000, height=1000)
            frame.pack()
            root2.mainloop()

def callback_Raw_data(event):
            root3=Tk()
            frame=Frame(root3,width=1000, height=1000)
            frame.pack()
            root3.mainloop()

def callback_Processed_data(event):
            root4=Tk()
            frame=Frame(root4,width=1000, height=1000)
            frame.pack()
            root4.mainloop()

def callback_wireshark_sniff(event):
            #root5=Tk()
            #frame=Frame(root5,width=1000, height=1000)
            #frame.pack()
            #root5.mainloop()
            os.startfile("C:\Program Files (x86)\Wireshark\wireshark.exe") #change the path name if required on another host system
            root.mainloop()
            
def callback_AP_settings(event):

            webbrowser.open(url, new=new)
            root.mainloop()

class Wireless:
    
    def __init__(self, master):
        myfont = tkFont.Font(family="arial", size=15, weight=tkFont.BOLD)
        myfont_head = tkFont.Font(family="arial", size=24, weight=tkFont.BOLD)
        frame=Frame(master)
        frame.pack(expand=YES)

        
        self.lbl = Label(frame, text="WIRELESS MEASUREMENT TOOL V2.0", font=myfont_head) # Creating a label
        self.lbl.pack(side=TOP)#Placing the label in the window
        #lbl.grid(row=1, column=1)
        self.btn = Button(frame, text="WI-FI measurements ", command=quit,font=myfont) #Create a  new button widget
        self.btn.bind("<Button-1>",  callback_Wifi_measurement)      
        self.btn.pack(side=BOTTOM,padx=10, pady=10)  #Placing the button on the widget

        
        self.btn2 = Button(frame, text="Video benchmarking ", command=quit,font=myfont) #Create a  new button widget
        self.btn2.bind("<Button-1>",  callback_Video_benchmarking)      
        self.btn2.pack(side=BOTTOM,padx=10, pady=10)  #Placing the button on the widget

        self.btn3 = Button(frame, text="Raw data ", command=quit,font=myfont) #Create a  new button widget
        self.btn3.bind("<Button-1>",  callback_Raw_data)      
        self.btn3.pack(side=BOTTOM, padx=10, pady=1)  #Placing the button on the widget

        self.btn4 = Button(frame, text="Processed Data ", command=quit,font=myfont) #Create a  new button widget
        self.btn4.bind("<Button-1>",  callback_Processed_data)      
        self.btn4.pack(side=BOTTOM, padx=10, pady=10)  #Placing the button on the widget

        self.btn5 = Button(frame, text="Wireshark sniff ", command=quit,font=myfont) #Create a  new button widget
        self.btn5.bind("<Button-1>",  callback_wireshark_sniff)      
        self.btn5.pack(side=BOTTOM, padx=10, pady=10)  #Placing the button on the widget

        
        self.btn6 = Button(frame, text="Access Point Settings ", command=quit,font=myfont) #Create a  new button widget
        self.btn6.bind("<Button-1>",  callback_AP_settings)      
        self.btn6.pack(side=BOTTOM, padx=10, pady=10)  #Placing the button on the widget


root = Tk( )          #creates a window called TK root widget
root.title('TPVision') #GUI title
root.geometry("600x600")
#inserting TpVision Logo
path= 'C:\Users\mayur.sarode\Pictures\TpVision-logo.png'
img =ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side=BOTTOM,padx=1, pady=1, fill="both")
w=Wireless(root)
root.mainloop( )


