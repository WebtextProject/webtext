#!/usr/bin/python3
import sys
import configparser
from pathlib import Path
from three import send_webtext

#open ini file containing login details
path = str(Path.home()) + '/.webtext.ini'
config = configparser.ConfigParser()
config.read(path)

if('three' not in config):
    #Must create .ini file
    three_username = input('three username: ')
    three_password = input('three password: ')

    config['three'] = {'username':three_username,
                   'password':three_password}

    with open(path, 'w') as configfile:
        config.write(configfile)

username = config['three']['username']
password = config['three']['password']

if len(sys.argv) < 3:
    #command line args not supplied - use interactive mode
    print("Command line argument usage: three [message text] [number]\n")
    print("Using interactive mode.\n")
    recipient_number = input("Enter recipient number: ")
    message_text = input("Enter message text: ")

else:
    #get message text from command line args
    message_text = sys.argv[1]
    recipient_number = sys.argv[2]

send_webtext(username, password, message_text, recipient_number)
