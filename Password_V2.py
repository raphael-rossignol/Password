from hashlib import sha256
import json

valid_car_spe = "!@#$%^&*()_-+={}[]"
valid_car_low = "azertyuiopqsdfghjklmwxcvbn"
valid_car_upper = "AZERTYUIOPQSDFGHJKLMWXCVBN"
valid_digit = "1234567890"
password = ''
list_password = ''
password_checked = False
enc_password = ''


def user_input():       # Save the user input and transform it into list and string
    global password
    global list_password
    list_password = list(input(
        "Choose a password, it must contain 1 Upper, 1 Low, 1 Digit, 1 Special Character and 8 Character minimum : "))
    password = str(list_password)


user_input()


def check_password():       # Use the length of the list and if it's valid proceed to analyse the string
    global password_checked
    global password
    size_password = len(list_password)
    if size_password >= 7:

        while not any(car_upper in valid_car_upper for car_upper in password) or \
            not any(car_low in valid_car_low for car_low in password) or \
            not any(digit in valid_digit for digit in password) or \
            not any(car_spe in valid_car_spe for car_spe in password):
            print("Password not valid, try again")
            user_input()
        else:
            password_checked = True

    else:
        print("Password not valid, try again")
        user_input()


check_password()


def encrypt_password():     # If the password is valid it encrypts it and print the encrypted version
    global enc_password
    if password_checked == True:
        enc_password = (sha256(password.encode('utf-8')).hexdigest())
        print("Here's your encrypted password :")
        return print(enc_password)


encrypt_password()


def password_json():        # If the password is valid, stores it in Json file and let you assign a name in it
    global enc_password
    if password_checked == True:
        password_dict = {
            input("Choose a name for your password : "): enc_password
        },
        with open("Password.json", "w") as f:
            json.dump(password_dict, f, indent=2)


password_json()