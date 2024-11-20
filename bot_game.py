import bot_mail
import bot_keys
import bot_whatsapp
import bot_db as db
from main import speakandprint

def verify_email(email):
    bot_mail.send_email(bot_mail.subject_otp, email, bot_mail.html_otp)
    speakandprint("enter the otp : \n")
    otp = int(input())
    if bot_keys.otp_verification(bot_mail.otp, otp):
        speakandprint("Your email is verified")
    else:
        speakandprint("Your email is not verified")
        exit()

def verify_number(phone, name):
    bot_whatsapp.send_message(phone, name)
    if bot_keys.otp_verification(bot_whatsapp.otp, int(input(print("enter the otp : \n")))):
        speakandprint("Your number is verified")
    else:
        speakandprint("Your number is not verified")
        exit()

def change_password(name):
    speakandprint("Enter your new password : \n")
    new_password = input()
    speakandprint("Confirm your new password : \n")
    confirm_password = input()
    while new_password != confirm_password:
        speakandprint("passwords do not match")
        speakandprint("create your new password : \n")
        new_password = input()
        speakandprint("confirm your password : \n")
        confirm_password = input()
    db.change_password(new_password, name)
    speakandprint("Password changed successfully")

def send_password_via_whatsapp(name):
    speakandprint("Enter your number to get your password")
    number = input()
    number = "+91" + number
    if db.check_ph_no(number, name):
        password = db.get_password(name)
        bot_whatsapp.send_password(number, name, password[0][0])
        speakandprint("Your password is sent to your whatsapp number")
    else:
        speakandprint("Your number is not registered")
        exit()


# db.change_password("Shivi@123", "badi didi")
# db.print_data("badi didi", 2)


