from hashlib import sha256
import json

valid_car_spe = "!@#$%^&*()_-+={}[]"
valid_car_low = "azertyuiopqsdfghjklmwxcvbn"
valid_car_upper = "AZERTYUIOPQSDFGHJKLMWXCVBN"
valid_digit = "1234567890"
password = ''
list_password = ''
password_checked = False
hashed_password = ''
checking_data = False
running = True      # While Running = True, executes all the functions except 'user_input'


def user_input():       # Saves the user input and transform it into list and string
    global password
    global list_password
    list_password = list(input(
        "Choose a password, it must contain 1 Upper, 1 Low, 1 Digit, 1 Special Character and 8 Character minimum : "))
    password = str(list_password)


def check_password():       # Uses the length of the list and if it's valid proceed to analyse the string
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


def hash_password():     # If the password is valid it hashes it and print the hashed version
    global hashed_password
    if password_checked == True:
        hashed_password = (sha256(password.encode('utf-8')).hexdigest())
        print("Here's your hashed password :")
        print(hashed_password)


def create_json():    # Asks the user if there is already a json file named "Password.json", if not creates it else pass
    if password_checked == True:
        choice_json = str(input("Do you already have a 'Password.json' file ? Y/N : "))
        if "Y" in choice_json:
            pass
        else:
            json_dict = {
                "Password": [

                ]
            }
            with open('Password.json', 'w') as f:
                json.dump(json_dict, f, indent=4)


def checking_password_json():       # Verify if there's the same password in the json file
    global hashed_password
    global checking_data
    with open('Password.json', 'r') as f:
        check_data = json.load(f)
    if hashed_password not in str(check_data):
        checking_data = True
    else:
        print("This password is already taken, please choose another one")


def password_json(filename='Password.json'): # If the password is valid, stores it in Json file and let you assign a name for it
    if checking_data == True:
        global hashed_password
        global running
        password_dict = {
            input("Choose a name for your password : "): hashed_password
        }
        with open(filename, "r+") as f:
            file_data = json.load(f)
            file_data["Password"].append(password_dict)
            f.seek(0)
            json.dump(file_data, f, indent=2)
            running = False


while running == True:
    user_input()
    check_password()
    hash_password()
    create_json()
    checking_password_json()
    password_json()