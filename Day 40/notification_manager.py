""" Import the required modules """
import os
from twilio.rest import Client

""" TWILIO ACCOUNT DETAILS """
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


class NotificationManager:  # Create a class for notification
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, alert_message):  # send the message to mobile
        message = self.client.messages \
            .create(
            body=alert_message,
            from_='+14632238856',
            to='+919986998881'
        )

        return message.status
