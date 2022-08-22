from twilio.rest import Client
from datetime import datetime, timedelta
from config.twilio_api_key import *


class TwilioHelper:
    ACCOUNT_SID = SECRET_ACCOUNT_SID
    AUTH_TOKEN = SECRET_AUTH_TOKEN

    TWILIO_PHONE_NUMBER = SECRET_TWILIO_PHONE_NUMBER
    TWILIO_WHATSAPP_NUMBER = SECRET_TWILIO_WHATSAPP_NUMBER

    MY_MOBILE_NUMBER = SECRET_MY_MOBILE_NUMBER
    MY_WHATSAPP_NUMBER = SECRET_MY_WHATSAPP_NUMBER

    client_obj = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms():
        TwilioHelper.client_obj.messages.create(
            to=TwilioHelper.MY_MOBILE_NUMBER,
            from_=TwilioHelper.TWILIO_PHONE_NUMBER,
            body='You have successfully registered for the Twilio APIs demo app'
        )

    def send_Otp():
        client_obj = Client(TwilioHelper.ACCOUNT_SID, TwilioHelper.AUTH_TOKEN)
        service_obj = client_obj.verify.services.create(
            friendly_name='Demo Verify Service'
        )
        TwilioHelper.VERIFICATION_SERVICE_ID = service_obj.sid
        client_obj.verify.services(TwilioHelper.VERIFICATION_SERVICE_ID).verifications.create(
            to=TwilioHelper.MY_MOBILE_NUMBER,
            channel='sms'
        )

    def check_Otp(Otp):
        client_obj = Client(TwilioHelper.ACCOUNT_SID, TwilioHelper.AUTH_TOKEN)
        verification_check = client_obj.verify.services(TwilioHelper.VERIFICATION_SERVICE_ID)\
            .verification_checks.create(to=TwilioHelper.MY_MOBILE_NUMBER, code=Otp)
        if verification_check.status == "approved":
            return True
        return False

    def send_whatsapp_message():
        client_obj = Client(TwilioHelper.ACCOUNT_SID, TwilioHelper.AUTH_TOKEN)
        ETA_date = datetime.now()+timedelta(days=3)
        client_obj.messages.create(
            from_='whatsapp:'+TwilioHelper.TWILIO_WHATSAPP_NUMBER,
            body='Your Demo App order of 1 Unicorn has been shipped and should be delivered on '\
                +ETA_date.strftime("%B %d, %Y")+'.',
            to='whatsapp:'+TwilioHelper.MY_WHATSAPP_NUMBER
        )