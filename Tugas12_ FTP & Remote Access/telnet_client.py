import telnetlib

tn = telnetlib.Telnet('localhost')
tn.read_until(b"login: ")
tn.write(b"your_username\n")
tn.read_until(b"Password: ")
tn.write(b"your_password\n")
print(tn.read_all().decode('utf-8'))
