#!/usr/bin/env python

import os, sys, string

if len(sys.argv)!=3:
        print "USAGE: ./a.out fname fileLen"
        exit (0)

fname=sys.argv[1]
traceLen=int(sys.argv[2])

cdffname=fname+".cdf"
prev=-1
count=-1
totalPercentage=0.0
fd1=open(fname)
fd2=open(cdffname, "w")
for line in fd1:
        strs=line.split()
        cur=int(strs[0])
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
