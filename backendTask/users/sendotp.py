from django.conf import settings
from twilio.rest import Client
import random 

# send otp from twilio 
class messagehandler:
    phone_no=None
    otp=None

    def __init__(self,phone_no,otp) -> None:
        self.phone_no=phone_no
        self.otp=otp

    def send_otp_on_phone(self):
        client=Client(settings.ACCOUNT_SID,settings.AUTH_TOKEN)   
        message=client.messages.create(
            body=f'hi this is your otp {self.otp}',
            to=self.phone_no,
            from_="+13343266940"
        )
        # return self.otp for testing