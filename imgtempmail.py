from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import ssl
import smtplib
from django.template.loader import render_to_string
from django.utils.html import strip_tags

    
    
def attach_file_to_email(email_message, filename, extra_headers=None):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Set up the input extra_headers for img
      ## Default is None: since for regular file attachments, it's not needed
      ## When given a value: the following code will run
         ### Used to set the cid for image
    if extra_headers is not None:
        for name, value in extra_headers.items():
            file_attachment.add_header(name, value)
    # Attach the file to the message
    email_message.attach(file_attachment)
    
    
    
    
    

def ImgTemplateEmailNotify(receiver:str, subject:str, body:str):
    try:
        email_sender = "toluondrums@gmail.com"
        email_password = "elnm sfgs atad egvw"
        email_receiver = receiver

        subject = subject
        
        html_message = render_to_string('mail_template.html')
        # html_message = render_to_string('mail_template.html', {'context': 'values'})
        # plain_message = strip_tags(html_message)

        body = f"""{body}"""

        emailObj = MIMEMultipart()
        emailObj['From'] = "Grace Forte Academy"
        emailObj['To'] = email_receiver
        emailObj['subject'] = subject
        emailObj.attach(MIMEText(html_message, "html"))
        # attach_file_to_email(emailObj,  {'Content-ID': '<myimageid>'})
        
        with open('logo.png', "rb") as f:
            file_attachment = MIMEApplication(f.read())
            # Add header/name to the attachments    
            file_attachment.add_header(
                "Content-Disposition",
                f"attachment; filename= logo.png",
            )
    # Set up the input extra_headers for img
      ## Default is None: since for regular file attachments, it's not needed
      ## When given a value: the following code will run
         ### Used to set the cid for image
        extra_headers = {'Content-ID': '<myimageid>'}
        if extra_headers is not None:
            for name, value in extra_headers.items():
                file_attachment.add_header(name, value)
        # Attach the file to the message
        emailObj.attach(file_attachment)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, emailObj.as_string())
            return "Notification Successful"
    except Exception as ex:
        return ex
    