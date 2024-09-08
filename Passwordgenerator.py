import random
import string

def generate_password(length):
    # Define character sets: lowercase, uppercase, digits, and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from the set
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

# Get the desired password length from the user
password_length = int(input("Enter the desired length of the password: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Generated password: {generated_password}")