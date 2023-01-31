from hashlib import sha256
import json


def user_input():
    valid_car_spe = "!@#$%^&*()_-+={}[]"
    list_password = list(input("Choose a password, it must contain 1 Upper, 1 Low, 1 Digit, 1 Special Character and 8 Character minimum"))
    password = str(list_password)
    size_password = len(list_password)

    if size_password >= 7:      # Check if the input's length is right

        for space in list_password:     # Check if there's no space
            space = space.isspace()
            if space == 0:
                print("Space OK")
                break
            elif space == 0:
                continue
            else:
                print("Space not valid, try again")
                user_input()

        for maj in list_password:       # Check if there's at least 1 Maj Character
            maj = maj.isupper()
            if maj == 1:
                print("Maj OK")
                break
            elif maj == 0:
                continue
            else:
                print("Maj not valid, try again")
                user_input()

        for low in list_password:       # Check if there's at least 1 Low Character
            low = low.islower()
            if low == 1:
                print("Low OK")
                break
            elif low == 0:
                continue
            else:
                print("Low not valid, try again")
                user_input()

        for digit in list_password:     # Check if there's at least 1 Number
            digit = digit.isdigit()
            if digit == 1:
                print("Digit OK")
                break
            elif digit == 0:
                continue
            else:
                print("Digit not valid, try again")
                user_input()

        if any(car_spe in valid_car_spe for car_spe in list_password):      # Check if there's at least 1 Special Character
            enc_password = (sha256(password.encode('utf-8')).hexdigest())     # Hash the password
            with open("Password.json", "w") as f:
                json.dump(enc_password, f)
            json_enc_password = json.dumps(enc_password)
            print("Here's your encrypted password :")
            return print(json_enc_password)
        else:
            print("Car_spe not valid, try again")
            user_input()

    else:       # If the length is not right, try again
        print("Password not valid, try again")
        user_input()


user_input()