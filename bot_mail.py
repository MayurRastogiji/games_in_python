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
    # rec_email = "mayurrastogiji@gmail.com"
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

# send_email(subject_otp, rec_email, html_otp)

# import os
# import smtplib
# from email.utils import formataddr
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.base import MIMEBase
# from pathlib import Path
# from email import encoders
# import pandas as pd
# from dotenv import load_dotenv 

# # Email file path
# file_path = '   '
# # Email file sheet name
# sheet_name = 'Sheet1'

# PORT = 587
# EMAIL_SERVER = "smtp.gmail.com"

# # Load the environment variables
# current_dir = Path(_file).resolve().parent if "file_" in locals() else Path.cwd()
# envars = current_dir / ".env"
# load_dotenv(envars)

# # Read environment variables
# sender_email = os.getenv("EMAIL")
# password_email = os.getenv("PASSWORD")
 
# def send_email(subject, receiver_email, image_path):
#     # Create the base text message.
#     msg = MIMEMultipart("relative")
#     msg["Subject"] = subject
#     msg["From"] = formataddr(("Intellia Society", sender_email))
#     msg["To"] = receiver_email

#     html = f"""\
# <!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{subject}</title>
# </head>

# <body>
#     <p> Dear Volunteers,</p>

#     <p> We hope this email finds you well! 😊</p>

#     <p> On behalf of Team Intellia, we would like to extend our heartfelt gratitude to each and every one of you for
#         participating in and making Jalsa 2.0 an unforgettable experience 🤩. Your enthusiasm, dedication, and
#         contributions
#         played a pivotal role in the event's success.</p>

#     <p> As a token of appreciation, we would like to offer you a certificate of participation 🎓. You can download your
#         certificate from: <br>

#         <a href="https://drive.google.com/drive/folders/1suSxGuow6mfq72dC1JfwXl9m_OnXUp4x?usp=sharing">Download
#             Certificate</a>
#     </p>

#     <p> We appreciate your continued support and look forward to having you on board for our future endeavors.</p>

#     <p> Thank you once again for being an integral part of Jalsa 2.0! 🙏</p>
#     <p>🔗Follow us via : https://linktr.ee/intelliasociety</p>

#     <p> Warm regards, <br>
#         Team Intellia</p>
#     <p style="margin: 0;"><img src="cid:image1" style="width: 80px;"></p>
# </body>

# </html>
#     """
    
#     # Attach the HTML version
#     msg.attach(MIMEText(html, "html"))

#      # Attach the image
#     try:
#         with open(image_path, 'rb') as img:
#             img_data = img.read()
#             image = MIMEImage(img_data)
#             image.add_header('Content-ID', '<image1>')
#             image.add_header('Content-Disposition', 'inline', filename=os.path.basename(image_path))
#             msg.attach(image)
#     except Exception as e:
#         print(f"Failed to read/attach image {image_path}: {e}")
        
#     # Attach the PDF as a downloadable link
#     # try:
#     #     with open(pdf_path, 'rb') as pdf_file:
#     #         pdf_part = MIMEBase('application', 'octet-stream')
#     #         pdf_part.set_payload(pdf_file.read())
#     #         encoders.encode_base64(pdf_part)
#     #         pdf_part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(pdf_path)}"')
#     #         msg.attach(pdf_part)
#     # except Exception as e:
#     #     print(f"Failed to read/attach PDF {pdf_path}: {e}")

#     # Send the email
#     with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
#         server.starttls()
#         server.login(sender_email, password_email)
#         server.sendmail(sender_email, receiver_email, msg.as_string())

# def read_excel_file(file_path, sheet_name=None):
#     try:
#         # Read the Excel file
#         return pd.read_excel(file_path, sheet_name=sheet_name)
#     except FileNotFoundError:
#         print(f"Error: File not found at {file_path}")
#         return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None

# if _name_ == "_main_":
#     df = read_excel_file(file_path, sheet_name)
#     if df is not None:
#         for _, row in df.iterrows():
#             send_email(
#                 subject="🎉 Thank You for Making Jalsa 2.0 a Success! 🎉",
#                 receiver_email=row['email'],
#                 image_path="intellia_logo.png" ,
#                 # pdf_path="selected_volunteers.pdf"
#             )
#             print(f"Sent to {row['email']} successfully")

