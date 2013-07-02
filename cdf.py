#!/usr/bin/env python

import os, sys, string

fname="/home/wireless/Documents/Wireless_measurement_tool_TPVision/test_scripts/raw_values.txt"
cdffname="/home/wireless/Documents/Wireless_measurement_tool_TPVision/test_scripts/output.txt"
prev=-1
count=-1
totalPercentage=0.0
traceLen=10
fd1=open(fname)
fd2=open(cdffname, "w")
for line in fd1:
        strs=line.split()
        #print strs
        cur=int(strs[0])
        print cur
        if cur!=prev:
                if prev>=0:
                        pctg=1.0*count/traceLen
                        totalPercentage+=pctg
                        fd2.write(str(prev)+" "+str(totalPercentage)+"\n")
                prev=cur
                count=0
        count+=1
if prev>=0:
        pctg=1.0*count/traceLen
        totalPercentage+=pctg
        fd2.write(str(prev)+" "+str(totalPercentage)+"\n")

fd2.close()
fd1.close()
