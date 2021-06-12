import os
import requests
from colorama import Fore
try:
    os.system('clear')
    os.system('toilet -f mono12 -F gay Nedpy')
    print('               this is tool for check site situation')
    print(' ')
    k = input('Enter your site ------>>>>> ')
    s = requests.get('https://' + f'{k}')
    f = s.status_code
    os.system(f'figlet {f}')
    if f == 403 or f == 503 or f == 500 or f == 400:
        print('site is offline or destroyed!!')
    elif f == 200:
        print('site is good!!')
except:
    os.system('figlet 504')
    print('make sure the adress of site is ok')
    print('the request to site dont response it may cause 503 Error or your conecction or maybe youre ip baned for site!!')

print('  ')
ko = input('Do you want to use tool again?  y/n ----->>>> ')
if ko == 'yes' or ko == 'y':
    os.system('python situation.py')
elif ko == 'no' or ko == 'n':
    os.system('clear')
    os.system('figlet bye')
else:
    print(Fore.RED + 'something went wrong!!')
