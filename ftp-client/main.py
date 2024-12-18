from ftplib import FTP


host = "johndoe.net"
user = "johndoe"
password = "johndoe"

with FTP(host) as ftp:

    ftp.login(user=user, passwd=password)
    print(ftp.welcome)

    with open('text.txt', "wb") as f:
        ftp.retrbinary("RETR " + "mytest.txt", f.write, 1024)
        ftp.storbinary('STOR ' + 'upload.txt', f)


    ftp.quit()
