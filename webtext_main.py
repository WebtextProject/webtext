#!/usr/bin/python3

NETWORK = 'NAME_OF_NETWORK' 

import sys
import configparser
from pathlib import Path
exec('from ' + NETWORK + ' import send_webtext')

#open ini file containing login details
path = str(Path.home()) + '/.webtext.ini'
config = configparser.ConfigParser()
config.read(path)

if(NETWORK not in config):
    #Must create .ini file
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

send_webtext(username, password, message_text, recipient_number)
