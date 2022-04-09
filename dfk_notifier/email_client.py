import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

# Method for sending specific message to email with email credentials
def send_email(config, subject, message, file_content=None):
    try:
        # Message content
        msg = MIMEMultipart()
        msg['From'] = config["email"]["sender_email"]
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        if file_content:
            file = MIMEBase('application', "octet-stream")
            file.set_payload(file_content)
            encoders.encode_base64(file)
            file.add_header('Content-Disposition',
                            'attachment; filename=logs.txt')
            msg.attach(file)

        # Create ssl context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP(config["email"]["server"], config["email"]["port"]) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(config["email"]["sender_email"], config["email"]["sender_password"])
            for receiver_mail in config["email"]["receiver_emails"]:
                server.sendmail(config["email"]["sender_email"], receiver_mail, msg.as_string())
        return True, "Email sent."
    except Exception as ex:
        return False, str(ex)


if __name__ == "__main__":
    import argparse
    import logging
    import json

    # Parse and load configuration
    parser = argparse.ArgumentParser(description="DFK-hero-notification scripts")
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()
    try:
        with open(args.config, "r") as conf_in_file:
            configuration = json.load(conf_in_file)
    except Exception as ex:
        logging.error("There was problem with opening configuration file, exiting...")
        exit(1)

    send_email(configuration, "Test email", "Test content")
