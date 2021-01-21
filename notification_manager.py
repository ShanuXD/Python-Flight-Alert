import requests
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
        # print(message.sid)