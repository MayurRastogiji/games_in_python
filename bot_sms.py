from twilio.rest import Client
from bot_keys import account_sid, auth_token, service_sid
import random

# generate a random code
otp = random.randint(100000, 999999)
message = f"your OTP for verification your number in MTH is {otp}"
client = Client(account_sid, auth_token)

verification = client.verify \
    .v2 \
    .services(service_sid) \
    .verifications \
    .create(to='+917037386808', channel='sms')


print(verification.sid)