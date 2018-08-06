import time
import vk_api
from time import sleep
import requests as req
print("Login:")
login = input()
print("Password:")
password = input()
vk = vk_api.VkApi(login = login, password = password)
vk.auth()
a=vk.method('wall.post',{"owner_id":-169775266,"from_group":1,"message":"сообщение, написанное ботом =)","attachments":"photo-169775266_456239017"})
print(a)