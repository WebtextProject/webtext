#!/usr/bin/python3

NETWORK = 'eir' 

import sys, re
import configparser
from pathlib import Path
exec('from ' + NETWORK + ' import send_webtext')

#open ini file containing login details
path = str(Path.home()) + '/.webtext.ini'
config = configparser.ConfigParser()
config.read(path)

if(NETWORK not in config):
    #Must create .ini file (or add network details to it)
    config_username = input( NETWORK + ' username: ')
    config_password = input( NETWORK + ' password: ')

    config[NETWORK] = { 'username' : config_username,
                        'password' : config_password }

    with open(path, 'w') as configfile:
        config.write(configfile)



username = config[NETWORK]['username']
password = config[NETWORK]['password']

if len(sys.argv) < 3:
    recipient_number = input("Enter recipient number: ")
    message_text = input("Enter message text: ")

else:
    #get message text from command line args
    message_text = sys.argv[1]
    recipient_number = sys.argv[2]

#check if recipient starts with a digit
if not recipient_number[0].isdigit():
    #look up alias in contacts
    if not config.has_option('contacts', recipient_number):
        print("Cannot find contact:" + recipient_number +" in config file\nexiting")
        sys.exit()
    else:
        recipient_number = config['contacts'][recipient_number]

send_webtext(username, password, message_text, recipient_number)
