import smtplib


def send_email(message):

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login("YOUR_EMAIL","APP_PASSWORD")

    server.sendmail(
        "YOUR_EMAIL",
        "WIFE_EMAIL",
        message
    )

    server.quit()
