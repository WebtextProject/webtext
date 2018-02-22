#!/usr/bin/python3
import requests, sys, json

def eir_login(username, password, my_session):
    #Log in using data from file
    response = my_session.post('https://my.eir.ie/rest/brand/3/portalUser/authenticate', 
        data = {"emailAddress": username,
                "password": password
                }
        )
    return response.status_code

def get_mobile_num(my_session):
    response = my_session.get('https://my.eir.ie/rest/secure/brand/3/portalUser/lines')
    json_data = json.loads(response.text)
    number =  (json_data['data']['pairingsList'][0]['number'])
    return '+353' + number[1:]
    

def send_eir_webtext(message_text, recipient_number, my_session, my_number):
    response = my_session.post('https://my.eir.ie/mobile/webtext/mobileNumbers/' + my_number + '/messages',
                         json={"content": message_text,"recipients":[recipient_number]}
        )
    print(response.text)
    return response.status_code

def send_webtext(username, password, message_text, recipient_number):

    my_session = requests.Session()

    assert(eir_login(username, password, my_session) == 200)

    my_number = get_mobile_num(my_session)

    assert(send_eir_webtext(message_text, recipient_number, my_session, my_number) == 201)

    return True