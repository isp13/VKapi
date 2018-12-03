import vk_api
import time
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

    while True:
        a=vk_session.method('messages.send',{"user_id":215025432,"message":"message example"})
        time.sleep(10)
        tmp+=1


if __name__ == '__main__':
    main()