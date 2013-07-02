#!/usr/bin/env python
import os, sys, string
import numpy as np
import math
def print_graph():
        x=[]  ###local variable
        y=[]  ###Local variables
        fd1=open("/home/wireless/Documents/Wireless_measurement_tool_TPVision/Final_code/shieldroom_20mhz_external_TCP_0dB.txt")
        while 1:
            line=fd1.readline()
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
        fd1.close()
        return(x_flt, y)

a=[]
b=[]
x,y=print_graph()
#print x
#print y
prev=-1
count=-1
totalPercentage=0.0
traceLen= len(x)
i=1
j=0
while j < len(x):
        cur=int(y[j])
        if cur!=prev:
                if prev>=0:
                        pctg=1.0*count/traceLen
                        totalPercentage+=pctg
                        a.append(str(prev))
                        b.append(str(totalPercentage))
                        i=i+1
                prev=cur
                count=0
        count+=1
        j=j+1
              
if prev>=0:
        pctg=1.0*count/traceLen
        totalPercentage+=pctg
        a.append(str(prev))
        b.append(str(totalPercentage))
print a
print b

##Extracting the data rate


