# -*- vk sending messages on replies -*-
import time
import vk_api
from time import sleep
import requests as req
 
print("Login:")
login = input()
print("Password:")
password = input()
print("User's id to answer:")
userid=input()
print("message to send:")
mess=input()
 
vk = vk_api.VkApi(login = login, password = password)
#vk_api.VkApi(token = 'a02d...e83fd') app login
vk.auth()
 
messages = vk.method('messages.get', {"count":1})
last = messages['items'][0]['id']
 
while True:
    try:
        messages = vk.method('messages.get', {"last_message_id":last})
        lastmessinfo=vk.method('messages.get', {"count":1})
        fromid=lastmessinfo['items'][0]['user_id']
    except Exception as e:
        print(e)
        sleep(4)
        continue
    if not messages['items']: # if no messages
        sleep(4)
        continue
    last = messages['items'][0]['id']
    for message in messages['items']:
    	if (fromid==userid):
    		vk.method('messages.send', {"user_id" :userid,'message':mess})
    sleep(4)