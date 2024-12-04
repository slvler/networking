import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from smail import sign_message


KEY_FILE = "private_key.pem"
CERT_FILE = "certificate.pem"

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

#message
msg = MIMEMultipart('related')
msg.attach(MIMEText(message, 'plain', _charset="UTF-8"))
msg['From'] = 'test_user@test_user'
msg['To'] = 'test@test'
msg['Subject'] = "test subject"


signed_msg = sign_message(msg, KEY_FILE, CERT_FILE)


text = signed_msg.as_string()

with smtplib.SMTP("####################", 99999999) as server:
    server.starttls()
    server.login("###########", "######################")
    server.sendmail(sender, receiver, signed_msg)


print("send mail")