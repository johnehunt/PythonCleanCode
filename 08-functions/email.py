""" Illustrates the idea of default parameter values for functions """

# Import smtplib for the actual sending function
from smtplib import SMTP

# Import the email modules we'll need
from email.message import EmailMessage


def send(message, to, subject, cc=None, bcc=None):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = 'jjh@midmarsh.co.uk'
    msg['To'] = to
    msg['Cc'] = cc
    msg['Bcc'] = bcc

    # Send the message via our own SMTP server.
    with SMTP('localhost') as smtp:
        try:
            smtp.send_message(msg)
        except Exception as error:
            print("Unable to send e-mail: '%s'." % str(error))
        finally:
            smtp.quit()


send("Hi There", 'johnhunt10@gmail.com', 'Welcome')
