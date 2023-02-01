from hashlib import sha256
import json

valid_car_spe = "!@#$%^&*()_-+={}[]"
valid_car_low = "azertyuiopqsdfghjklmwxcvbn"
valid_car_upper = "AZERTYUIOPQSDFGHJKLMWXCVBN"
valid_digit = "1234567890"


def user_input():
    list_password = list(input("Choose a password, it must contain 1 Upper, 1 Low, 1 Digit, 1 Special Character and 8 Character minimum"))
    password = str(list_password)
    size_password = len(list_password)

    if size_password >= 7:      # Check if the input's length is right

        for space_car in list_password:         # Check if there's a space in the password
            space_car = space_car.isspace()
            if space_car == 0:
                continue
            elif space_car == 1:
                print("No space allowed, try again")
                user_input()
            else:
                break

        if not any(car_upper in valid_car_upper for car_upper in list_password):
            print("Upper not OK")
            user_input()

        if not any(car_low in valid_car_low for car_low in list_password):
            print("Low not OK")
            user_input()

        if not any(digit in valid_digit for digit in list_password):
            print("Digit not OK")
            user_input()

        if any(car_spe in valid_car_spe for car_spe in list_password):      # Check if there's at least 1 Special Character
            enc_password = (sha256(password.encode('utf-8')).hexdigest())      # Hash the password and take the json form

            with open("Password.json", "a") as f:       # Open json file to write password and encrypted password
                json.dump(enc_password, f)
                f.write("\n")

            json_enc_password = json.dumps(enc_password)        # Take the encrypted password's string from json file
            print("Here's your encrypted password :")
            return print(json_enc_password)     # Print the encrypted password's string from json file

        else:
            print("Car_spe not valid, try again")
            user_input()

    else:       # If the length is not right, try again
        print("Length not valid, try again")
        user_input()


user_input()