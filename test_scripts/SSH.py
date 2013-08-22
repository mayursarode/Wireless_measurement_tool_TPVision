import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.201', username= 'wireless', password='wireless',port=22)
ssh.stdin, ssh.stdout, ssh.stderr = ssh.exec_command("ls")
type(ssh.stdin)
ssh.stdout.readlines()
