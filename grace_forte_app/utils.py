import threading
from django.core.mail import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib
from django.template.loader import render_to_string



class EmailSendingThread(threading.Thread):
    def __init__(self, receiver:str, subject:str, body:str, html_message:str, name: str=""):
        self.subject = subject        
        self.email_sender = "dokunmichael@gmail.com"
        self.email_password = "plbn gvdg rtig amac"
        self.email_receiver = receiver
        self.html_message = html_message

        threading.Thread.__init__(self)


    def run(self):        
        try:
            emailObj = MIMEMultipart()
            emailObj['From'] = "GraceForte Academy"
            emailObj['To'] = self.email_receiver
            emailObj['subject'] = self.subject
            emailObj.attach(MIMEText(self.html_message, "html"))
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(self.email_sender, self.email_password)
                smtp.sendmail(self.email_sender, self.email_receiver, emailObj.as_string())
                return "Notification Successful"
            
        except Exception as ex:
            print(ex)

def send_pending_training_mail(receiver, subject, body, name):
    html_message = render_to_string('pending_mail.html', {"name": name, "message": body})
    EmailSendingThread(receiver, subject, body, html_message, name).start()
    
def send_confirmed_training_mail(receiver, subject, body, name, instance):
    amount = f"{instance.expectedAmount:,}"
    html_message = render_to_string('training_confirmation_mail.html', {"name": name, "message": body, "product": instance.enrolledCourse.title, "amount": amount, "ReceiptID": instance.receiptId})
    EmailSendingThread(receiver, subject, body, html_message, name).start()
    
    
