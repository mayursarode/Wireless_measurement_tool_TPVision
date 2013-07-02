#Post processing with UI functionality
# This code asks from the user, the file name, the attenuation steps, and produces
# an output of a excel sheet with the 90%, 50 % and 10% cdf values
#!/usr/bin/python
#Modificaiton  Date: 6/7/2013
# Adding the file handling option
# Added directory creation command
# Added UDP fucntionality
# Header files and constants
import Tkinter  #importing the Tkinter libraries
import tkFont
from PIL import Image,ImageTk
import urllib2
import webbrowser
import os
import subprocess
import xlwt

def quit():           #create a event when termination of the event is involved
    import sys; sys.exit()
####################################################################################    

class Post_processing(Tkinter.Tk):
    
    def __init__(self, parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
    # Attenuation Block
        
        self.label_att=Tkinter.Label(self, text="Start Atten. (dB)")
        self.label_att.grid(column=1,row=2,columnspan=1,sticky='EW')
        self.entry_att = Tkinter.Entry(self)
        self.entry_att.delete(0,Tkinter.END)
        self.entry_att.insert(0, "0")
        self.entry_att.grid(column=2, row=2, columnspan=1)

        #Step Attenuation size
        self.label_st=Tkinter.Label(self, text="Step (dB)")
        self.label_st.grid(column=1,row=3,columnspan=1,sticky='EW')
        self.entry_st = Tkinter.Entry(self)
        self.entry_st.delete(0,Tkinter.END)
        self.entry_st.insert(0, "3")
        self.entry_st.grid(column=2, row=3, columnspan=1)

        # Stop  Attenuation
        self.label_stt=Tkinter.Label(self, text="Stop (dB)")
        self.label_stt.grid(column=1,row=4,columnspan=1,sticky='EW')
        self.entry_stt = Tkinter.Entry(self)
        self.entry_stt.delete(0,Tkinter.END)
        self.entry_stt.insert(0, "6")
        self.entry_stt.grid(column=2, row=4, columnspan=1)

        self.label_pwd= Tkinter.Label(self, text="Folder Iperf Data")
        self.label_pwd.grid(column=1,row=5,columnspan=1)
        self.entry_pwd = Tkinter.Entry(self, width=80)
        self.entry_pwd.delete(0,Tkinter.END)
        self.entry_pwd.insert(0, "/home/wireless/Documents/Wireless_measurement_tool_TPVision/Final_code/measurement_6-11-2013/")  
        self.entry_pwd.grid(column=2, row=5, columnspan=10)

        self.label_pwdxl= Tkinter.Label(self, text=" Path of the Excel File")
        self.label_pwdxl.grid(column=1,row=6,columnspan=1)
        self.entry_pwdxl = Tkinter.Entry(self, width=80)
        self.entry_pwdxl.delete(0,Tkinter.END)
        self.entry_pwdxl.insert(0, "/home/wireless/Documents/Wireless_measurement_tool_TPVision/test_scripts/test.xls")  
        self.entry_pwdxl.grid(column=2, row=6, columnspan=10)

        

        self.btn = Tkinter.Button(self, text=" START", width=10, command=self.callback)#Create a  new button widget
        #self.btn.bind("<Button-1>",  callback))
        self.btn.grid(column=5, row= 3, columnspan=1)

    def callback(self):
        a_att = self.entry_att.get() #start attenuation
        a_st= self.entry_st.get()    # Step attenuation
        a_stt=self.entry_stt.get()   # Stop attenuation
        a_pwd=self.entry_pwd.get()
        a_pwdxl=self.entry_pwdxl.get()
        ##print a_st
        #print a_stt
        #print a_pwd
        c,d,traceLen=cdf_calculation(a_pwd, int(a_st), int(a_stt),int(a_att))
        print c
        print d
        write_excel(a_pwdxl, c,d,traceLen)

def write_excel(a_pwd, c,d,traceLen):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('sheet 1')
        #Now that the sheet is created, it’s very easy to write data to it.
        # indexing is zero based, row then column
        sheet.write(0,1,a_pwd)  

        #When you’re done, save the workbook (you don’t have to close it like you do with a file object)
        wbk.save(a_pwd)


def cdf_calculation(a_pwd, a_st, a_stt,a_att):
        x=[]  ###local variable
        y=[]  ###Local variables
        while a_att<=a_stt:
            fopen=a_pwd+"shieldroom_20mhz_external_TCP_"+ str(a_att) +"dB.txt"
            print fopen
            fd1=open(fopen)
            a_att=a_att+a_st
            while 1:
                line=fd1.readline()
                print line
                a14= line.find('-',0)
                a15= line.find('sec',0)
                d=line[a14+1:a15]
                size=len(d)
                if size < 8 and size >0 :
                  x.append((d))  
                if not line:
                    break
######################## Extracting the Data rate##############################################
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
            fd1.close()
            a=x_flt
            b=y
            c=[]
            d=[]
            prev=-1
            count=-1
            totalPercentage=0.0
            traceLen= len(a)
            b=bubble_sort(b, traceLen)
            i=1
            j=0
            while j < len(a):
                    cur=int(b[j])
                    if cur!=prev:
                            if prev>=0:
                                    pctg=1.0*count/traceLen
                                    totalPercentage+=pctg
                                    c.append(str(prev))
                                    d.append(str(int(totalPercentage*100)))
                                    i=i+1
                            prev=cur
                            count=0
                    count+=1
                    j=j+1
            if prev>=0:
                    pctg=1.0*count/traceLen
                    totalPercentage+=pctg
                    c.append(str(prev))
                    d.append(str(int(totalPercentage*100)))  
            print c
            print d
            del x[:]
            del y[:]
            del a[:]
            del b[:]
            del c[:]
            del d[:]         
        return(c,d,traceLen)
              
def bubble_sort(b, traceLen):
    t=0
    k=0
    i=0
    j=0
    #print traceLen
    while (k < traceLen -1):
        for i in range (0, traceLen-1):
             if (b[i]> b[i+1]):
                t=b[i]
                b[i]=b[i+1]
                b[i+1]=t
        k=k+1
    return(b)
    
############################################################################################
if __name__ == "__main__":
    root=Post_processing(None)
    root.title('Post Processing Tab') #GUI title
    path= '/home/wireless/Documents/Wireless_measurement_tool_TPVision/TPvision-logo.tiff'
    img =ImageTk.PhotoImage(Image.open(path))
    panel = Tkinter.Label(root, image = img)
    panel.grid(column=2, row=10, columnspan=10)
    root.mainloop( )
