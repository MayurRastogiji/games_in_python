import mysql.connector as mysql
import bot_keys
import pyttsx3
import bot_whatsapp
engine = pyttsx3.init()

def speakandprint(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

db = mysql.connect(
    host="localhost", 
    user="root", 
    password="Enter Your Password Here",
    database= "Enter Your Database Name Here")
# print(db.connection_id)

cursor = db.cursor()

def winner_price(name):
    cursor.execute(bot_keys.s_winner_price, (name,))
    db.commit()

def entry_fees(name):
    cursor.execute(bot_keys.s_entry_fees, (name,))
    db.commit()

def print_data(name, n):
    cursor.execute(bot_keys.s_print_data, (name,))
    result = cursor.fetchall()
    if n == 1:
        bot_whatsapp.send_profile(result[0][1], result[0][2], result[0][3])
    print("------------------------------------")
    speakandprint(f"Your Email: {result[0][0]} \nYour Name: {result[0][1]} \nYour Balance: {result[0][2]}")
    print("------------------------------------")

def insert_data(email, name, ph_no):
    cursor.execute(bot_keys.s_insert, (email, name, ph_no))
    db.commit()

def check_name(name):
    cursor.execute(bot_keys.s_check_name, (name,))
    result = cursor.fetchall()
    if len(result) > 0:
        return True
    else:
        return False
    
def check_email(name):
    cursor.execute(bot_keys.s_check_email, (name,))
    result = cursor.fetchall()
    return result

def get_ph_no(name):
    cursor.execute(bot_keys.s_check_ph_no, (name,))
    result = cursor.fetchall()
    return result

def check_ph_no(number, name):
    cursor.execute(bot_keys.s_check_ph_no, (name,))
    result = cursor.fetchall()
    if result[0][0] == number:
        return True
    else:
        return False

def check_password(name, password):
    cursor.execute(bot_keys.s_change_password, (name,))
    result = cursor.fetchall()
    if result[0][0] == password:
        return True
    else:
        return False
    
def get_password(name):
    cursor.execute(bot_keys.s_check_password, (name,))
    result = cursor.fetchall()
    return result

def change_password(password, name):
    cursor.execute(bot_keys.s_change_password, (password, name))
    db.commit()
    
def change_email(email, name):
    cursor.execute(bot_keys.s_change_email, (email, name))
    db.commit()

def change_ph_no(ph_no, name):
    cursor.execute(bot_keys.s_change_ph_no, (ph_no, name))
    db.commit()



# print(type(check_email("mayur rastogi")[0][0]))

# print(check_ph_no("mayur rastogi")[0][0])