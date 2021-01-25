import smtplib
from twilio.rest import Client

ACCOUNT_SID = "------------TWILIO ACCOUNT SID-------------"
AUTH_TOKEN = "------------TWILIO AUTH TOKEN-------------"
MY_NUMBER = "+91XXXXXXXXXXX"
TWILIO_NUMBER = "XXXXXXXXXXXXXXX"


class NotificationManager:

    def sendMsg(self, msg):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages \
            .create(
            body=msg,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )
    def sendMail(self, msg, send_to, link):
        my_email = "------your email------------"
        password = "--------password-------------"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_to,
            msg=f"Subject:New Low Price Flight!\n\n{msg}\n{link}".encode('utf-8'))

        connection.close()
