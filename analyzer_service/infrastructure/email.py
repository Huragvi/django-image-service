import smtplib
from email.mime.text import MIMEText

from analyzer_service.domain.interfaces import EmailGateway


class SMTPEmailGateway(EmailGateway):
    def __init__(self, host: str, port: int, username: str, password: str, from_email: str) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.from_email = from_email

    def send(self, recipient: str, subject: str, body: str) -> None:
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = self.from_email
        message["To"] = recipient

        with smtplib.SMTP(self.host, self.port) as server:
            if self.username:
                server.starttls()
                server.login(self.username, self.password)
            server.sendmail(self.from_email, [recipient], message.as_string())
