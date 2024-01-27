import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():10

try:
        # Prompt the user to specify the desired length of the password
        password_length = int(input("Enter the desired length of the password: "))
        
        # Generate the password
        password = generate_password(password_length)
        
        # Display the generated password
        print("Generated Password:", password)
except ValueError:
        print("Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
