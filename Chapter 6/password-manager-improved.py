#The Code seems to be badly written, I will see if it can be improved

import pyperclip
import sys
passwords = {1: 
             {'account_name': 'something.com', 'email': "shailendra@something.com", 'password': "Ajdjwad"},
            2: 
             {'account_name': 'other.com', 'email': "shailendra@other.com", 'password': "Other"}}

def pass_locker():
    password = ''
    if len(sys.argv) < 2:
        print("Usage: python pw.py <account-name>")
        sys.exit()
    account_name = sys.argv[1]
    for x in passwords:
        if (account_name == passwords[x]['account_name']):
            password = passwords[x]['password']
            pyperclip.copy(password)
            print("Password copied to clipboard.")
            if(password != ''): break
            
    if (password == ''):
        print("Account doesn't exist.")

pass_locker()