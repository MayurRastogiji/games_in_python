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

# send_message("+919193107757", "Lucky Tomar")
# otp_i = int(input("Enter the OTP: "))
# if otp == otp_i:
#     print("OTP verified")



# dictionary to store phone number for sending messages
# dict_phone = {
#     "mayur": "+917037386808",
#     "parth": "+919084774537",
#     "kartikey": "+918864997581",
#     "kartik": "+918449725011"
# }

# # list of groups to send messages
# lst_grp = ["BWx06GyYaho4a5m6hkwa88", "Iy4EKy7F94JKDDRUUOP4b2"]

# # sending message to all the contacts in the dictionary
# print("Sending message to contacts")
# for name, phone in dict_phone.items():
#     message = f"hello {name}"
#     pw.sendwhatmsg_instantly(phone, message, 15 , True, 3)
#     print(f"message sent to {name}")

# # sending message to all the groups in the list
# print("Sending message to groups")
# for group in lst_grp:
#     message = "hello all"
#     pw.sendwhatmsg_to_group_instantly(group, message, 15, True, 3)
#     print(f"message sent to {group}")
