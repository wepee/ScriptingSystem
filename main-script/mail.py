# -*-coding:Latin-1 -*
import json
import smtplib, ssl
from email.message import EmailMessage

with open('./config.json', 'r') as file:
    data = json.load(file)

def mail(objet, to, corps):
    msg = EmailMessage()
    msg.set_content(corps)
    msg["Subject"] = objet
    msg["From"] = data["mail"]["login"]
    msg["To"] = to

    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.ionos.fr", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(data["mail"]["login"], data["mail"]["password"])
        smtp.send_message(msg)