import smtplib
import ssl

# Method for sending specific message to email with email credentials
def send_email(config, subject, message):
    try:
        # Merge message
        message = "Subject: " + subject + "\n" + message
        # Create ssl context and send email
        context = ssl.create_default_context()
        with smtplib.SMTP(config["email"]["server"], config["email"]["port"]) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(config["email"]["sender_email"], config["email"]["sender_password"])
            for receiver_mail in config["email"]["receiver_emails"]:
                server.sendmail(config["email"]["sender_email"], receiver_mail, message)
        return True, "Email sent."
    except Exception as ex:
        return False, str(ex)
