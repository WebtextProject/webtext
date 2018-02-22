#!/usr/bin/python3
import requests, sys
import configparser
from pathlib import Path
from bs4 import BeautifulSoup

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
        data = {},
        )
    return response.status_code

def send_three_webtext(message_text, recipient_number, my_session):
    response = my_session.post('https://messaging.three.ie/messages/send',
                         data={'APIID':'AUTH-WEBSSO',
                               'TargetApp':'o2om_smscenter_new.osp?MsgContentID=-1&SID=_',
                               '_token':'',
	                           'message':message_text,
                               'recipients_contacts[]':'tel:' +
                               recipient_number,
                               'scheduled_datetime':'',
                               'scheduled':''
                         },
                        headers={'Connection':'close'}
        )
    remaining_texts = get_remaining_webtexts(response.text)
    print(remaining_texts + " remaining texts")
    return response.status_code

def get_remaining_webtexts(html_text_to_parse):
    soup = BeautifulSoup(html_text_to_parse, "html.parser")
    elements = soup.find_all('div', class_='user-crumb' )
 
    return elements[0].contents[0].text
    
def send_webtext(username, password, message_text, recipient_number):
    my_session = requests.Session()

    print("logging in to three.ie...")
    assert(three_login(username, password, my_session) == 200)
   # print("loading webtexting page...")
   # assert(go_to_webtexting_page(my_session) == 200)
    print("sending webtext...")
    assert(send_three_webtext(message_text, recipient_number, my_session) == 200)
    return True