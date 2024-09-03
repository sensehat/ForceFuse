#!/usr/bin/python3
import argparse
from ssh import ssh_brute
from ftp_brute_force import Anon_login, Port_21, Brute_force

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
    parser.add_argument("-o", type=str, dest="option", help="--option", default=None)
    
    args = parser.parse_args()

    target = args.target
    username = args.username
    wordlist = args.wordlist
    check = args.check
    anon = args.anon
    option = args.option

    if anon:
        Anon_login(anon)
    elif target and username and wordlist:
        if option == '1':
            ssh_brute(target, username, wordlist)
        elif option == '2':
            Brute_force(target, username, wordlist)
    elif check:
        Port_21(check)
    else:
        print("[-] Not a valid option, please refer to -h for help")

if __name__ == "__main__":
    main()
