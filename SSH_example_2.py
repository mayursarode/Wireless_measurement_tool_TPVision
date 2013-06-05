import paramiko
import os
import sys
import string

cmd = "iperf -c 192.168.1.100 -t 6 -i 0.5"
#cmd="ls"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.100', username='wireless',password='wireless',port=22) 
stdin, stdout, stderr = ssh.exec_command(cmd)
print stdout.readlines()
#string.split(data, '\n')
ssh.close()
