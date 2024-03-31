import smtplib
import ssl

def myEmail(message):
    smtp_server = "smtp.gmail.com"
    port=587
    sender_email="shaurya.attal@gmail.com"
    password="zpxdcnikucnqsayz"

    reciever_email="yamunaakritigowda@gmail.com"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        print("Logging in...")
        server.sendmail(sender_email, reciever_email, message)
        print("Email sent!")

    except Exception as e:
        print(e)