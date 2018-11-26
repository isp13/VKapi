import vk_api
def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def main():
    login, password = input(), input()
    vk_session = vk_api.VkApi(
        login, password,
        # 2-factor auth
        auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    a=vk_session.method('friends.get',{"user_id":97282679,"fields":"nickname,online,photo_id"})


    for item in a['items']:
    	id=str(item['id'])
    	firstname=str(item['first_name'])
    	secondname=str(item['last_name'])
    	online=str(item['online'])
    	print(firstname+" "+secondname+" online: "+online +"photo_id "+ photo_id)


if __name__ == '__main__':
    main()