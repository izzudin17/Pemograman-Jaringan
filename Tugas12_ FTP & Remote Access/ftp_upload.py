from ftplib import FTP

ftp = FTP('localhost')
ftp.login()
with open('data.txt', 'rb') as f:
    ftp.storbinary('STOR data.txt', f)
ftp.quit()
