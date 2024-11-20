
# admin details
account_sid = "AC014295a5e958b71ec7e3c40a15646317"
auth_token = "5875ff002e63af14f2d819cbcd7d50e2"
service_sid = "VA5313a3f5e9ddeb6afb440c6a616cfdef"
sender_number = "+917037386808"
sender_email = "mayurrastogi2004@gmail.com"
sender_password = "mctg vwfz udku ojsn"
name = "Mayur Rastogi"


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
    