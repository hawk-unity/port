import socket
import os
os.system("clear")
import colorama
from colorama import Fore, Back, Style, init
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
print("""
     _                    _         
    | |__   __ ___      _| | __ _
    | '_ \ / _` \ \ /\ / / |/ /| |_
    | | | | (_| |\ V  V /|   <_   _|
    |_| |_|\__,_| \_/\_/ |_|\_\|_|

              ^port tarama^
      """)
host = input(Fore.RED + "LÜTFEN İP ADRESİNİ GİRİNİZ : ")
port = int(input(Fore.RED + "TARATILACAK PORT ADRESİNİ GİRİNİZ : "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print(Fore.GREEN + "BU PORT KAPALI")
    else:
        print(Fore.GREEN + "BU PORT AÇIK")

portScanner(port)
