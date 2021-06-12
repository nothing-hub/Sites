
import requests
import os
from pyfiglet import Figlet
os.system('cls')
print('''
 ▄▄▄   ▄▄                  ▄▄
 ███   ██                  ██
 ██▀█  ██   ▄████▄    ▄███▄██  ██▄███▄   ▀██  ███
 ██ ██ ██  ██▄▄▄▄██  ██▀  ▀██  ██▀  ▀██   ██▄ ██
 ██  █▄██  ██▀▀▀▀▀▀  ██    ██  ██    ██    ████▀
 ██   ███  ▀██▄▄▄▄█  ▀██▄▄███  ███▄▄██▀     ███
 ▀▀   ▀▀▀    ▀▀▀▀▀     ▀▀▀ ▀▀  ██ ▀▀▀       ██
                               ██          ███''')
print('''                        this a tool for check site standing
                                 telegram id : @Nedpy ''')
print('   ')
try:
    ko = input('Enter your site ---------->>>>> ')
    l = requests.get('https://' + f'{ko}')
    lo = l.status_code
    f = Figlet(font='banner3-D')
    print(f.renderText(f'{lo}'))
# sugestion
    if lo < 400:
        print('situation of site host is good !! \nthe best standeng is 200')
    elif lo >= 400:
        print('host is not ok!!\ngoogle the Error')
except:
    f = Figlet(font='slant')
    print(f.renderText('503 504'))
    print('''maybe yore site adrees is wrong
    or your Error is 504 and 503 that care Error''')
ll = input('Do you want to use this tool again ? y/n --------->>>>>')
if ll == 'y' or ll == 'yes':
 os.system('python situation.py')
elif ll == 'n' or ll == 'no':
 f = Figlet(font='banner3-D')
 print(f.renderText('bye'))
 
