# phele apne default browser me jake whatsapp web login kr lio

import pywhatkit as pw
import random

otp = random.randint(100000, 999999)

def send_message(phone, name):
    message = f"Greetings {name},\n OTP for verification your number in MTH is {otp}"
    pw.sendwhatmsg_instantly(phone, message, 15, True, 3)
    print(f"message sent to {phone}")

def send_message_loged_in(phone, name):
    message = f"Greetings {name},\n You have successfully logged into your gaming account\nWelcome back Champ!"
    pw.sendwhatmsg_instantly(phone, message, 15, True, 3)
    print(f"message sent to {phone}")

def send_password(phone, name, password):
    message = f"Greetings {name},\n Your password for MTH account is {password}"
    pw.sendwhatmsg_instantly(phone, message, 15, True, 3)
    print(f"message sent to {phone}")

def send_profile(name, balance, ph_no):
    message = f"Greetings {name},\n Your Balance in your MTH account is {balance}"
    pw.sendwhatmsg_instantly(ph_no, message, 15, True, 3)
    print(f"message sent to {ph_no}")
