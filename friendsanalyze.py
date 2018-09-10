import vk_api

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def main():
    login, password = "yourlogin", "yourpassword"
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

    a=vk_session.method('friends.get',{"user_id":yourid,"fields":"nickname,online"})
    b=str(a["items"])
  

if __name__ == '__main__':
    main()