import paramiko
import os
import sys
import string
import commands

a7='192.168.1.100'
cmd_sr = "iperf -t 60 -i 0.5" + " -c " + a7 # The TV side
cmd_si= "iperf -s -w 512k"                 # The client side
#cmd = "iperf -c 192.168.1.100 -t 60 -i 0.5"
#a=os.system('cmd_ si')
a=commands.getoutput('cmd_si')
#print a
#cmd="ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.200', username='wireless',password='wireless',port=22) 
stdin, stdout, stderr = ssh.exec_command(cmd_sr)
output= stdout.readlines()
a1= len(output)
i=1
while (i<a1):
    print output[i]
    i=i+1
    
#print len[output]
#print output
#if output='\n'
    
#string.split(data, '\n')
ssh.close()
