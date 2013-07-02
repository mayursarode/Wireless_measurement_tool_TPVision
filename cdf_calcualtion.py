#!/usr/bin/env python
import os, sys, string
     
prev=-1
count=-1
totalPercentage=0.0
traceLen=10
fd1=open("/home/wireless/Documents/Wireless_measurement_tool_TPVision/raw_values.txt")
fd2=open("/home/wireless/Documents/Wireless_measurement_tool_TPVision/cdf.txt", "w")
array=[]
x=[]
i=1
while 1:
    lines=fd1.readline()
    array=[float(x) for x in lines.split()]
    print array
    x[i]=map(float, array)
    if not lines:
        break


