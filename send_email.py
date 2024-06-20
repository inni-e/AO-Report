# Module to send email

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def send_email(to_email, test_name, student_name):
    server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
    server.starttls()
    server.login('donotreply@alphaonecollege.com.au', 'alexxiao123')
    msg = MIMEMultipart()
    msg['From'] = 'donotreply@alphaonecollege.com.au'
    msg['To'] = to_email
    msg['Subject'] = 'Alpha One {} Report'.format(test_name)
    
    # email text
    with open('pdf_resources/email_intro.txt', 'rb') as fh:
        text = fh.read().decode('latin-1')
    msg.attach(MIMEText(text, 'plain'))
    
    pdf_name = '{}.pdf'.format(student_name)
    binary_pdf = open(pdf_name, 'rb')
    payload = MIMEBase('application', 'octate-stream', Name = pdf_name)
    payload.set_payload((binary_pdf).read())
    encoders.encode_base64(payload)
    
    payload.add_header('Content-Decomposition', 'attachment', filename = pdf_name)
    msg.attach(payload)
    binary_pdf.close()
    
    server.send_message(msg)
    server.quit()


