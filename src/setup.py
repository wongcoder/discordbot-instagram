
import os

def first_run():
    print('Welcome to the initial setup process.')
    DISCORD_TOKEN = input('Please enter your DISCORD_TOKEN: ')
    GUILD_TOKEN = input('Please enter the guild that you wish this bot to join: ')
    # Get token inputs

    cur_path = os.path.dirname(__file__)
    new_path = os.path.join(cur_path, "../.env")
        

    with open(new_path, 'w+') as f:
        f.write("DISCORD_TOKEN=" + DISCORD_TOKEN + "\n")
        f.write("GUILD_TOKEN=" + GUILD_TOKEN + "\n")
        f.close()
        
    print('Thank you. Stored your variables in .env . If you are unable to connect, either delete the .env file, or edit it.')
    return