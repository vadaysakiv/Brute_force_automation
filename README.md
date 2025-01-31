

LDAP - Authentication Bypass
![image](https://github.com/user-attachments/assets/a0fd483a-517c-4619-aa79-7f2efe0ff8cb)
no username and password known 

for wrong creds and password got "Login Failed!" as the response by burp response
![image](https://github.com/user-attachments/assets/f7032b9b-bd29-47ec-825d-2e8e884c53b7)


for user admin and password = *
**ldap code for that **(&(uid=admin)(userPassword=*))****
![image](https://github.com/user-attachments/assets/1b736446-9cf9-4ff4-bbee-b835b3458b87)
![image](https://github.com/user-attachments/assets/1a5dbb05-81bb-4949-a8df-43b90a012f02)

by running the username=* and password * 
![image](https://github.com/user-attachments/assets/ec85470c-e06a-4ee6-b183-5d8d2b132ea7)
this is our desired output for it 
even though using * for username and password will login with first valid username , but for this script let find the valid username 








**python testing_brute_force_unknown_user_pass.py http://94.237.54.116:52908/**
![image](https://github.com/user-attachments/assets/7f7ab654-6ed9-4e3f-9128-bba5df9ccbbf)

![image](https://github.com/user-attachments/assets/7bfc4474-c39f-4f36-9081-ac094b66e3e2)
![image](https://github.com/user-attachments/assets/df1e1577-739e-4cf1-8975-a04b604cf7b6)

![image](https://github.com/user-attachments/assets/949e2cb2-2f11-43c0-a313-c65276d8234e)

**tested for LDAP - Data Exfiltration & Blind Exploitation**

if username is known , using code:ldap (&(uid=admin)(|(description=*)(password=invalid)))
running brute for description by description_brute.py
![image](https://github.com/user-attachments/assets/39f26375-9aab-4497-8243-30798218f2c8)
