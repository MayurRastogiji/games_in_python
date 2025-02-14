import smtplib
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from bot_keys import sender_email, sender_password as password, sender_number
import random

otp = random.randint(100000, 999999)

def making_message(name):

    current_time = time.localtime()
    date = time.strftime("%d/%m/%Y", current_time)
    
    global subject_otp, subject_logged_in, html_otp, html_loged_in

    subject_logged_in = "🎉 Successful Login to Your Gaming Account 🎉"
    subject_otp = "🔐 OTP for Verification of Your Gaming Account 🔐"

    html_otp = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{subject_otp}</title>
    </head>

    <body>
        <p> Dear {name},</p>

        <p> We hope this email finds you well! 😊</p>

        <p> your OTP for verification is <b>{otp}<b>.</p>
        <p> Thank you once again for being an integral part of MGH! 🙏</p>
        <p>🔗Follow us via : <a href="https://linktr.ee/mayur.rastogi.cseaiml.2022?utm_source=braze&utm_medium=email&utm_campaign=20230519_Marketing_All_Activation_Triggered_MultiChannel_Global_English_VerticalJourney&utm_content=canvas&utm_term=Day25Email3Free_CTA9">LinkTree</a></p>

        <p> Warm regards, <br>
            Mayur Rastogi</p>
    </body>

    </html>

    """
    html_loged_in = f"""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{subject_logged_in}</title>
    </head>

    <body>
        <p> Dear {name},</p>

        <p> We hope this email finds you well! 😊</p>

        <p> We are writing to confirm that you have successfully logged into your gaming account on {date} at 0{current_time.tm_hour}:{current_time.tm_min}:{current_time.tm_sec}.</p>

        <p> If you have any questions or concerns, please do not hesitate to contact our customer support team at {sender_email} or {sender_number}</p>

        <p> Thank you 🙏 for choosing Mayur's Gaming Hub ! We hope you enjoy 😊 your gaming experience.</p>

        <p> We appreciate your continued support and look forward to having you on board for our future endeavors.</p>

        <p> Thank you once again for being an integral part of MGH! 🙏</p>
        <p>🔗Follow us via : <a href="https://linktr.ee/mayur.rastogi.cseaiml.2022?utm_source=braze&utm_medium=email&utm_campaign=20230519_Marketing_All_Activation_Triggered_MultiChannel_Global_English_VerticalJourney&utm_content=canvas&utm_term=Day25Email3Free_CTA9">LinkTree</a></p>

        <p> Warm regards, <br>
            Mayur Rastogi</p>
    </body>

    </html>

    """
def send_email(subject, receiver_email, html):
    # Create the base text message.
    msg = MIMEMultipart("relative")
    msg["Subject"] = subject
    msg["From"] = formataddr(("Gaming World", sender_email))
    msg["To"] = receiver_email
    
    msg.attach(MIMEText(html, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(sender_email, password)
    except:
        print("Login failed")
        exit()

    # print("Login successful")
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully")



