
# admin details
account_sid = "Enter your account_sid here"
auth_token = "Enter your auth_token here"
service_sid = "Enter your service_sid here"
sender_number = "Enter your sender_number here"
sender_email = "Enter your sender_email here"
sender_password = "Enter your sender_password here"
name = "Enter your name here"


# sql commands
s_check_name = "SELECT name FROM gamer_id WHERE name = %s"  
s_check_password = "SELECT password FROM gamer_id WHERE name = %s"
s_check_email = "SELECT email FROM gamer_id WHERE name = %s"
s_check_ph_no = "SELECT ph_no FROM gamer_id WHERE name = %s"
s_change_password = "UPDATE gamer_id SET password = %s WHERE name = %s"
s_change_email = "UPDATE gamer_id SET email = %s WHERE name = %s"
s_change_ph_no = "UPDATE gamer_id SET ph_no = %s WHERE name = %s"
s_insert = "INSERT INTO gamer_id (email, name, ph_no) VALUES (%s, %s, %s)"
s_print_data = "SELECT * FROM gamer_id WHERE name = %s"
s_entry_fees = "UPDATE gamer_id SET game_point = game_point - 100 WHERE name = %s"
s_winner_price = "UPDATE gamer_id SET game_point = game_point + 500 WHERE name = %s"


# otp verification
def otp_verification(otp1,otp):
    if otp1 == otp:
        return True
    else:
        return False
    