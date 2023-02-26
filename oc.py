import random
import re
import smtplib
from colorama import Fore

def is_valid_email():
    lines = open('outlooks.txt').read().splitlines()
    acc = random.choice(lines)

    email = acc.split(":")[0]
    password = acc.split(":")[1]
    try:
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        print(f"{email}:{password} | VALID")
        with open('outlooks.txt') as f:
            f.write(f"{email}:{password}\n")
    except:
        print(f"{email}:{password} | INVALID")
        with open("outlooks.txt", "r") as f:
            lines = f.readlines()
        with open("outlooks.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != acc:
                    f.write(line)

while True:
    is_valid_email()