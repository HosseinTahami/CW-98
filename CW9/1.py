import re

def is_validate(password):
    validate_reg = '(?=.*?[A-Z])(?=.*?[a-z])(?=.+*?[0-9]).{8,}'
    if re.match(validate_reg, password) :
        return True
    return False 

password = input("Enter your password: ")

is_validate(password)

