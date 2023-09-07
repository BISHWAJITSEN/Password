import random
import string

def generate_password(length):
    # Define the character sets for different complexity levels
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure at least one character from each set in the password
    password = (
        random.choice(lower_chars)
        + random.choice(upper_chars)
        + random.choice(digits)
        + random.choice(special_chars)
    )

    # Generate the remaining characters
    remaining_length = length - len(password)
    all_chars = lower_chars + upper_chars + digits + special_chars
    password += ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
