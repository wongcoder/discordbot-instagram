import os
from dotenv import load_dotenv

def first_run():
    print('Welcome to the initial setup process.')
    DISCORD_TOKEN = input('Please enter your DISCORD_TOKEN: ')
    USER_ID = input('Please enter your user ID that you want the bot to respond to: ')
    COOKIE = input('Please enter a session cookie that you received from instagram (ignore the session part): ')
     # Get token inputs

    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, "../.env")
        

    with open(new_path, 'w+') as f:
        f.write("DISCORD_TOKEN=" + DISCORD_TOKEN + "\n")
        f.write("USER_ID=" + USER_ID + "\n")
        f.write("COOKIE=" + COOKIE + "\n")
        f.close()
        
    print('Thank you. Stored your variables in .env . If you are unable to connect, either delete the .env file, or edit it.')
    return

def get_env():
    DISCORD_TOKEN = 'Token is out of scope, try to debug' # init as empty
    load_dotenv()

    if not os.getenv('DISCORD_TOKEN'):
        # run initial setup
        print('Was this function called?')
        first_run()
        load_dotenv() # reinit .env

    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    USER_ID = int(os.getenv('USER_ID'))
    return DISCORD_TOKEN, USER_ID

if __name__ == "__main__":
    print('Unit test/integration for get_env()')
    print('First, delete dot env')
    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, "../.env")
    os.remove(new_path)

    print('Make sure it asks you for a prompt')
    DISCORD_TOKEN, USER_ID, COOKIE = get_env()
    print('Okay, now checking if empty')
    print(DISCORD_TOKEN)
    print(USER_ID)
    print(COOKIE)
