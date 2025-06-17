from ftplib import FTP

ftp = FTP('localhost')
ftp.login()
ftp.retrlines('LIST')
ftp.quit()
