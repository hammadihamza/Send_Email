import smtplib
import ssl
from email.message import EmailMessage


subject = "Test Email"
body = "Hello there! This is email sent using python!"
sender_email = "Your_Email@gmail.com"
receiver_email = "Receiver_Email@gmail.com"

PWD = input("-> ")

MSG = EmailMessage()
MSG["From"] = sender_email
MSG["To"] = receiver_email
MSG["Subject"] = subject
MSG.set_content(body)

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, PWD)
    server.sendmail(sender_email, receiver_email, MSG.as_string())


print("Success")


