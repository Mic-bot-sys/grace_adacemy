from email.message import EmailMessage
import ssl
import smtplib


def EmailNotification(receiver:str, subject:str, body:str):
    try:
        email_sender = "toluondrums@gmail.com"
        email_password = "uwxneygtvnptudbp"
        email_receiver = receiver

        subject = subject

        body = f"""{body}"""

        emailObj = EmailMessage()
        emailObj['From'] = email_sender
        emailObj['To'] = email_receiver
        emailObj['subject'] = subject
        emailObj.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, emailObj.as_string())
            return "Notification Success"
    except Exception as ex:
        return ex
    
receiver = "oladokun7141@gmail.com"
subject = "BOOKING NOTIFICATION!!!"
body = "A Client just booked a Session. Kindly Visit your Dashboard for confirmation"

# result = BookingNotification(receiver, subject, body)
# print(result)