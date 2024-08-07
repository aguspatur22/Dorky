import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailLog:
    def __init__(self,
                 name='Dorky',
                 me='your-email@example.com',
                 recipients=['recipient@example.com'],
                 subject='[{0}] Dork Report',
                 body='Here is the dork report:\n\n{0}',
                 mail_server='smtp.example.com',
                 smtp_port=587,
                 email_user='your-email@example.com',
                 email_password='your-email-password'):
        self.name = name
        self.me = me
        self.recipients = recipients
        self.subject = subject
        self.body = body
        self.mail_server = mail_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def get_subject(self, slug=""):
        return self.subject.format(self.name, slug)

    def create_mime_multipart(self, subject):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.me
        msg['To'] = ', '.join(self.recipients)
        return msg

    def set_body(self, msg, body):
        msg.attach(MIMEText(body, 'plain'))
        return msg

    # Add port to the send_mail method if needed and uncomment the login line
    def send_mail(self, msg):
        with smtplib.SMTP(self.mail_server) as server:
            server.starttls()
            #server.login(self.email_user, self.email_password)
            server.sendmail(self.me, self.recipients, msg.as_string())

    def send_report(self, dork_urls):
        subject = self.get_subject()
        body = self.body.format('\n'.join(dork_urls))
        mail_base = self.create_mime_multipart(subject)
        mail = self.set_body(mail_base, body)
        self.send_mail(mail)
