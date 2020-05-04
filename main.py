
import smtplib


def send_mail(email, password, to, msg):
    server = smtplib.SMTP('smtp.aol.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    server.sendmail(
        email,
        to,
        msg
    )
    print("message sent!")
    server.quit()


your_email = ""
your_password = ""
email_to = ""
message = f"Subject:testing\n\n " \
          f"This is a test email"

send_mail(your_email, your_password, email_to, message)
