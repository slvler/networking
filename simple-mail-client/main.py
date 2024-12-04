import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#smpt server config
server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
server.starttls()
server.login("###########", "######################")

#message
msg = MIMEMultipart()
msg['From'] = 'test_user@test_user'
msg['To'] = 'test@test'
msg['Subject'] = "test subject"

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = '####.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

#email send
server.sendmail('mail', 'mail2', text)




