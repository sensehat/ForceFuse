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
""")
    
    parser = argparse.ArgumentParser(description="A Python SSH and FTP brute force tool.")
    
    parser.add_argument("-t", "--target", type=str, help="Target IP address", required=True)
    parser.add_argument("-u", "--username", type=str, help="Username for login", required=True)
    parser.add_argument("-w", "--wordlist", type=str, help="Path to wordlist file", required=True)
    parser.add_argument("-o", "--option", type=str, choices=['ssh', 'ftp'], help="Choose 'ssh' or 'ftp' brute force", required=True)
    parser.add_argument("-c", "--check", type=str, help="Check if port 21 is open for FTP")
    parser.add_argument("-a", "--anon", type=str, help="Check for anonymous login on FTP")
    
    args = parser.parse_args()

    target = args.target
    username = args.username
    wordlist = args.wordlist
    option = args.option
    check = args.check
    anon = args.anon

    if option == 'ssh':
        print("[*] Starting SSH brute force attack...")
        ssh_brute(target, username, wordlist)
    elif option == 'ftp':
        if anon:
            Anon_login(anon)
        elif check:
            Port_21(check)
        else:
            print("[*] Starting FTP brute force attack...")
            Brute_force(target, username, wordlist)
    else:
        print("[-] Invalid option, please choose 'ssh' or 'ftp'.")

if __name__ == "__main__":
    main()
