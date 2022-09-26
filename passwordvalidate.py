import string
import random
from random import randint

# Initializations of important data used within functions.

forbidden_char = (" @#")
special_char = ("!-$%&'()*+,./:;<=>?_[]^`{|}~")
decimal_digit = ("0123456789")
upper_char = (string.ascii_uppercase)
lower_char = (string.ascii_lowercase)
valid_chars = (special_char + decimal_digit + upper_char + lower_char)

# Function which checks the validity and security of inputted passwords.

def validate(password):

    # Initializations of digit, special character, uppercase character, and lowercase character count.

    digits = 0
    specials = 0
    uppers = 0
    lowers = 0

    # Loop which checks if each required character is present within password input
    # if present, character counts increases by an increment of 1

    for char in password:
        if char in forbidden_char:
            return 'Invalid'
        elif char in special_char:
            specials += 1
        elif char in upper_char:
            uppers += 1
        elif char in lower_char:
            lowers += 1
        elif char in decimal_digit:
            digits += 1
    
    # Main loop which analyzes if inputted password is secure, insecure, or invalid
    # based upon necessary conditions.

    while len(password) >= 8:
        if specials >= 1 and uppers >= 1 and lowers >= 1 and digits >= 1:
            return 'Secure'
        else:
            return 'Insecure'
    else:
        return 'Invalid'

# Function which generates randomized password meeting security conditional.

def generate(n):

    # Initializations of important data used within function

    random_pass = []
    secure_password = ""

    # Loop that generates a guaranteed secure randomized password using the 'random' library,
    # then appending and joining the randomly chosen elements to a list and variable, 
    # respectively, then returning the password if the input is more than or equal to 8.

    if n >= 8:
        while validate(secure_password) != 'Secure':
            for i in range(n):
                random_pass.append(random.choice(valid_chars))
            secure_password = "".join(random_pass)
        return secure_password    

# If conditional used for checking functions and inputs.

if __name__ == "__main__":
    print(validate("HACKING!"))
    print(validate(generate(9)))
    pass
