import re
import random
import smtplib
from email.mime.text import MIMEText
from time import sleep

# Watermark indicating program creator
# networkchristo - Security Program

# List to store registered users
user_list = [{'username': 'networkchristo', 'first_name': 'admin', 'last_name': 'admin', 'age': 30, 'email': 'admin@example.com', 'password': 'secureAdminPass123'}]

def is_valid_password(password):
    """Check if the password is valid."""
    common_passwords = ['12345678', 'password', '123456789', 'qwerty']
    if password in common_passwords:
        print("This password is commonly used. Please choose another password.")
        return False
    elif len(password) < 8:
        print("Password should be at least 8 characters long.")
        return False
    else:
        return True

def is_valid_email(email):
    """Check if the email format is valid."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def send_verification_code(email):
    """Send a verification code to the user's email."""
    verification_code = random.randint(100000, 999999)
    
    # Email content
    sender_email = 'your_email@gmail.com'  # Replace with your email address
    subject = 'Verification Code for Two-Step Verification'
    body = f'Your verification code is: {verification_code}'
    
    # Create MIMEText object
    msg = MIMEText(body, 'plain')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email
    
    # Send email using Gmail SMTP
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, 'your_gmail_password')  # Replace it using your account password
        
        smtp_server.sendmail(sender_email, [email], msg.as_string())
        smtp_server.quit()
        
        print(f"Verification code sent to {email}. Please check your email.")
        return verification_code
    except Exception as e:
        print(f"Failed to send email: {e}")
        return None

def login():
    """Function for user login."""
    username = str(input("Enter your username: ")).lower()
    password = str(input("Enter your password: "))
    
    for user in user_list:
        if user['username'] == username and user['password'] == password:
            print("Password verified. Proceeding to two-step verification.")
            code = send_verification_code(user['email'])
            if code:
                entered_code = int(input("Enter the verification code sent to your email: "))
                if entered_code == code:
                    print(f"Welcome {username}!")
                    return
                else:
                    print("Invalid verification code.")
                    return
            else:
                print("Failed to send verification code. Please try again later.")
                return
    print("Invalid username or password.")
    return

def register():
    """Function for user registration."""
    first_name = str(input("What is your first name: "))
    last_name = str(input("What is your last name: "))
    age = int(input("Enter your age: "))
    email = str(input("Enter your valid email: "))
    
    if not is_valid_email(email):
        print("Invalid email format.")
        return
    
    username = str(input("Enter your username (Username will be lowercase): ")).lower()
    
    if any(user['username'] == username for user in user_list):
        print("This username is taken. Choose another one.")
        return
    
    password = str(input("Enter your password: "))
    
    if not is_valid_password(password):
        return

    # Add the new user to the user list
    user_list.append({'username': username, 'first_name': first_name, 'last_name': last_name, 'age': age, 'email': email, 'password': password})
    
    print("Registration successful! Please check your email for verification.")
    sleep(2)

def main():
    """Main function to handle the program flow."""
    name = str(input("Enter your name: ")).lower()
    
    if name == "christo":
        print(f"Welcome to the Security Program, {name}")
        action = str(input("Would you like to (login/register): ")).lower()
        if action == "login":
            login()
        elif action == "register":
            register()
        else:
            print("Invalid action. Exiting program.")
            exit()
    else:
        print("You are not authorized and this name is not found in our database.")
        ask = str(input(f"Your name '{name}' is not found in our database. Would you like to add this name to our database (Type Yes or No): ")).lower()
        if ask == "yes":
            register()
        elif ask == "no":
            print("Program exiting...")
            exit()
        else:
            print("I did not understand what you have said.")
            exit()

if __name__ == "__main__":
    main()
