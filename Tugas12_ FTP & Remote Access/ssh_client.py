import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost', username='your_username', password='your_password')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read().decode())
ssh.close()
