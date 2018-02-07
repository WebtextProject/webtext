#!/usr/bin/python3
import requests, sys
import configparser
from pathlib import Path

def three_login(username, password, my_session):
    #Log in using data from file
    response = my_session.post('https://login.three.ie/', 
        data = {'username': username,
            'password': password,
            'section':'section'
            }
        )
    return response.status_code

def go_to_webtexting_page(my_session):
    response = my_session.get('https://messaging.three.ie/messages/send',
        data = {'APIID':'AUTH-WEBSSO',
            'TargetApp':'o2om_smscenter_new.osp?MsgContentID=-1&SID=_'},
        )
    return response.status_code

def send_three_webtext(message_text, recipient_number, my_session):
    response = my_session.post('https://messaging.three.ie/messages/send',
                         data={'_token':'setjL1s5ha4NoyxrjqHPcaPfbWjSKx5IrK3A9Z4H',
	                           'message':message_text,
                               'recipients_contacts[]':'tel:' +
                               recipient_number,
                               'scheduled_datetime':'',
                               'scheduled':''
                         }
        )
    return response.status_code
    

def send_webtext(username, password, message_text, recipient_number):
    my_session = requests.Session()

    assert(three_login(username, password, my_session) == 200)
    assert(go_to_webtexting_page(my_session) == 200)
    assert(send_three_webtext(message_text, recipient_number, my_session) == 200)
    
    return True