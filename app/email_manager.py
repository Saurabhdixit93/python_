import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

def manage_email(action, to=None, subject=None, body=None):
    if action == "read":
        return read_emails()
    elif action == "send":
        return send_email(to, subject, body)
    else:
        return {"error": "Invalid action"}

def connect_email():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    return mail

def read_emails():
    mail = connect_email()
    mail.select("inbox")
    _, search_data = mail.search(None, 'ALL')
    email_list = []
    for num in search_data[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, bytes_data = data[0]
        email_list.append(bytes_data.decode("utf-8"))
    return {"emails": email_list}

def send_email(to, subject, body):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server.sendmail(EMAIL, to, msg.as_string())
    return {"status": "Email sent successfully"}
