import imaplib
import email

imap_server = "##########.######.######.##"
email_address = "########"
password = "###########"


imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")
_, msg = imap.search(None, "ALL")


for m in msg[0].split():
    _, data = imap.fetch(m, "(RFC822)")
    #print(data)

    message = email.message_from_bytes(data[0][1])
    print(f"number: {m}")
    print(f"from: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"Date: {message.get('Date')}")