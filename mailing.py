import smtplib
import datetime

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from logger import log

class sPiMailing:
    def __init__(self, user_name, user_email):
        self.email = 'sPiCameraProject@gmail.com' # email account of the service
        self.password = 'MSProject123'

        self.client = [user_name, user_email] # email accounts of the initial user user
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()

        self.smtp.login(self.email, self.password)

    def sendEmail(self, subject, text):

        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.client[1]
        msg['Subject'] = subject
        attachment = open('intruder.jpg','rb')
        msg.attach(MIMEText(text,'plain'))

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= intruder.jpg")
        msg.attach(part)

        self.smtp.sendmail(self.email, self.client[1],  msg.as_string())
        log('Mail sent')

    def notifyWhileAway(self):
        subject = 'Someone at the front door!'
        text = 'Hello {0}!\n\n\tAt {1} sPi system has detected someone at the front door while you are away. We\'ve attatched a picture of the individual.\nBest regards the sPi team!'.format(self.client[0].split()[0], datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.sendEmail(subject, text)

    def notifyWhileInDnd(self):
        subject = 'Someone was at your front door.'
        text = 'Hello {0}!\n\n\tAt {1} sPi system has detected someone at the front door during your do not disturb hours. We\'ve attatched a picture of the individual.\n\nBest regards the sPi team!'.format(self.client[0].split()[0], datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.sendEmail(subject, text)

    def kill(self):
        self.smtp.quit()
        log('Mailing service is shut down ...')

# part of it inspired by https://github.com/samlopezf/Python-Email
