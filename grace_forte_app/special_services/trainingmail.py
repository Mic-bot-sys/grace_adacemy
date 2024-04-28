from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import smtplib
from django.template.loader import render_to_string
from django.utils.html import strip_tags



html = '''
    <html>
        <body>
            <h1>Daily S&P 500 prices report</h1>
            <p>Hello, welcome to your report!</p>
        </body>
    </html>
    '''
    
    
# @shared_task
def TrainingTemplateEmailNotify(receiver:str, subject:str, body:str, name: str=""):
    try:
        email_sender = "dokunmichael@gmail.com"
        email_password = "plbn gvdg rtig amac"
        email_receiver = receiver

        subject = subject
        
        html_message = render_to_string('pending_mail.html', {"name": name, "message": body})
        # html_message = render_to_string('mail_template.html', {'context': 'values'})
        # plain_message = strip_tags(html_message)

        emailObj = MIMEMultipart()
        emailObj['From'] = "GraceForte Academy"
        emailObj['To'] = email_receiver
        emailObj['subject'] = subject
        emailObj.attach(MIMEText(html_message, "html"))
        # emailObj.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, emailObj.as_string())
            return "Notification Successful"
    except Exception as ex:
        return ex
    

# @shared_task
def ConfirmedTrainingTemplateEmailNotify(receiver, subject, body, name, instance):
    try:
        email_sender = "dokunmichael@gmail.com"
        email_password = "plbn gvdg rtig amac"
        email_receiver = receiver

        subject = subject
        amount = f"{instance.expectedAmount:,}"
        html_message = render_to_string('training_confirmation_mail.html', {"name": name, "message": body, "product": instance.enrolledCourse.title, "amount": amount, "ReceiptID": instance.receiptId})

        emailObj = MIMEMultipart()
        emailObj['From'] = "GraceForte Academy"
        emailObj['To'] = email_receiver
        emailObj['subject'] = subject
        emailObj.attach(MIMEText(html_message, "html"))
        # emailObj.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, emailObj.as_string())
            return "Notification Successful"
    except Exception as ex:
        return ex
    