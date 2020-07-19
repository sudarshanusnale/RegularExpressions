#Email validation
#valid email format is xxx@xxx.xx Ex. ssu@gmail.com

import re

def email_validation():
    while True:
        email = input("Enter the email: ")
        if re.search("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email):
            print("It is a valid email address")
            break
        else:
            print('It is not a valid email address')

email_validation()