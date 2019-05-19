import smtplib
import datetime

class sPiMailing:
    def __init__(self, user_name, user_email):
        self.email = 'sPiCameraProject@gmail.com' # email account of the service
        self.password = 'MSProject123'

        self.cleints = [] # email accounts of the initial user user
        self.cleints.append([user_name, user_email])
        self.smtp = smtplib.SMTP('smtp.gmail.com', 587)

        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.ehlo()

        self.smtp.login(email, password)

    def sendEmail(self, user, subject, text):
        for email in self.cleints:
            header = 'To: ' + user + '\nFrom: ' + self.email + 'Subject: ' + subject
            self.smtp.sendmail(self.email, user, self.header + '\n' + text)

    def notifyWhileAway():
        subject = 'Someone at the front door!'
        for client in self.clients:
            text = 'Hello %s!\n\n\tAt %s sPi system has detected someone at the front door while you are away.' + \
                ' We\'ve attatched a picture of the individual.\n\nBest regards the sPi team!' \
                % (client[0], datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
            self.sendEmail(client[1], subject, text)

    def __del__(self)
        s.quit()