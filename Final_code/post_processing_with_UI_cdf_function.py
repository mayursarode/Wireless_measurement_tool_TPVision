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
from scipy import interpolate,linspace
import tkFileDialog
import statsmodels.api as sm

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

        self.button_pwd= Tkinter.Button(self, text="Folder Iperf Data",command=self.open_dir_raw)
        self.button_pwd.grid(column=1,row=5,columnspan=1)
        self.entry_pwd = Tkinter.Entry(self, width=40)
        self.entry_pwd.delete(0,Tkinter.END)
        self.entry_pwd.insert(0, "/home/wireless/Documents/scenario3")  
        self.entry_pwd.grid(column=2, row=5, columnspan=10)

        self.button_pwdxl= Tkinter.Button(self, text=" Path of the Excel File", command=self.open_dir_exl)
        self.button_pwdxl.grid(column=1,row=6,columnspan=1)
        self.entry_pwdxl = Tkinter.Entry(self, width=40)
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
        cdf_calculation(a_pwdxl,a_pwd, int(a_st), int(a_stt),int(a_att))

    def open_dir_raw(self):
        self.entry_pwd.delete(0,Tkinter.END)
        dirname=tkFileDialog.askdirectory(parent=self,initialdir="/", title='Please select a Direcotry')
        self.entry_pwd.insert(0, dirname)  
        


    def open_dir_exl(self):
        self.entry_pwdxl.delete(0,Tkinter.END)
        dirname=tkFileDialog.askdirectory(parent=self,initialdir="/", title='Please select a Direcotry')
        self.entry_pwdxl.insert(0, dirname)  
        

#def write_excel(a_pwd, c,d,traceLen,ex_c):
        
ex_c=2
def cdf_calculation(a_pwdxl,a_pwd, a_st, a_stt,a_att):
        x=[]  ###local variable
        y=[]  ###Local variables
        global ex_c
        wbk = xlwt.Workbook(encoding="utf-8")
        sheet = wbk.add_sheet('sheet 1')
        while a_att<=a_stt:
            fopen=a_pwd+"/shieldroom_20mhz_external_TCP_"+ str(a_att) +"dB.txt"
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
            b=bubble_sort(b, traceLen) ## Bit rate
            c=a
            d=sm.distributions.ECDF(x)
            print c #bitrate
            print d  #cdf
            c_10= cdf_10(c,d)
            c_50= cdf_50(c,d)
            c_90= cdf_90(c,d)
            print c_10
            print c_50
            print c_90
            #cdf_50(c,d)
            #cdf_90(c,d)
            #sheet.write( 1,12,label='10% cdf')
            #sheet.write( 1,14,label='50% cdf')
            #sheet.write( 1,16,label='90% cdf')
            sheet.write(ex_c,12,c_10)
            sheet.write(ex_c,14,c_90)
            sheet.write(ex_c,16,c_50)
            ex_c=ex_c+a_st
            del x[:]
            del y[:]
            del a[:]
            del b[:]
            del c[:]
            del d[:]   
        #print ex_c
        #Now that the sheet is created, it’s very easy to write data to it.
        # indexing is zero based, row then column
        #When you’re done, save the workbook (you don’t have to close it like you do with a file object)
        wbk.save(a_pwdxl)

def cdf_10(c,d):
    for i in range(0,len(d)):
        if int(d[i]) ==10:
            #print "true"
            #print c[i]
            return (c[i])
            break
        elif int(d[i])>10:
            c1=int(c[i-1])
            c2=int(c[i+1])
            d1=int(d[i-1])
            d2=int(d[i+1])
            c_10=((d2-10)*c1+(10-d1)*c2)/((d2-10)+(10-d1))
            return(c_10)
            break
       
def cdf_50(c,d):
    for i in range(0,len(d)):
        if int(d[i]) ==50:
            #print "true"
            #print c[i]
            return (c[i])
            break
        elif int(d[i])>50:
            c1=int(c[i-1])
            c2=int(c[i+1])
            d1=int(d[i-1])
            d2=int(d[i+1])
            c_50=((d2-50)*c1+(50-d1)*c2)/((d2-50)+(50-d1))
            return(c_50)
            break

def cdf_90(c,d):
    for i in range(0,len(d)):
        if int(d[i]) ==90:
            #print "true"
            #print c[i]
            return (c[i])
            break
        elif int(d[i])>90:
            c1=int(c[i-1])
            c2=int(c[i+1])
            d1=int(d[i-1])
            d2=int(d[i+1])
            c_90=((d2-90)*c1+(90-d1)*c2)/((d2-90)+(90-d1))
            return(c_90)
            break  
  
    
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
