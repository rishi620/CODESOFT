import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Define possible characters for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure a random order
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    length = int(input("Enter the password length: "))
    print(f"Generated password: {generate_password(length)}")
