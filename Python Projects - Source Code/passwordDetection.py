# Strong Pssword Detection

import re

def is_strong_password(password):
    # Check if the password is at least eight characters long
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    uppercase_regex = re.compile(r'[A-Z]')
    if not uppercase_regex.search(password):
        return False

    # Check for at least one lowercase letter
    lowercase_regex = re.compile(r'[a-z]')
    if not lowercase_regex.search(password):
        return False

    # Check for at least one digit
    digit_regex = re.compile(r'\d')
    if not digit_regex.search(password):
        return False

    # If all conditions are met, the password is strong
    return True

# Set a maximum number of attempts
max_attempts = 3

# Prompt the user for a strong password within a limited number of attempts
for attempt in range(1, max_attempts + 1):
    user_password = input(f"Attempt {attempt}/{max_attempts}: Enter a password: ")

    if is_strong_password(user_password):
        print("Password is strong. Good job!")
        break
    else:
        print("Password is not strong. Please try again.")

# Notify the user if the maximum number of attempts is reached
else:
    print(f"Maximum number of attempts ({max_attempts}) reached. Exiting.")

