import os

import discord
import asyncio
from instascraper import get_latest_post
from dotenv import load_dotenv
from setup import first_run

# Helper function to create an interval similar to Javascript
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# fetch token
token = 'Token is out of scope, try to debug' # init as empty
load_dotenv()
if not os.getenv('DISCORD_TOKEN'):
    # run initial setup
    first_run()

    load_dotenv() # reinit .env
    token = os.getenv('DISCORD_TOKEN')
else:
    token = os.getenv('DISCORD_TOKEN')
print(token) # technically an unsafe operation but okay

# Init Discord client
client = discord.Client()
latestPost = None

def formatPost(post):
    text = post['edge_media_to_caption']['edges'][0]['node']['text']
    url = 'https://www.instagram.com/p/' + post['shortcode'] + '/'
    return text, url

class MyClient(discord.Client):
    # load script
    async def on_ready(self):
        print(f'{client.user} has connected to Discord!')
        async for guild in client.fetch_guilds(limit=150):
            print(guild.name)

    async def on_message(self, message):
        if message.author.id == self.user.id: # avoids self reply
            return 

        channel = message.channel
        if message.content.startswith('$fetch') and channel.permissions_for(message.author).administrator == True :
            
            await message.channel.send('Please enter the hashtag.')

            def is_same_author(m):
                return m.author == message.author

            try:
                hashtag = await self.wait_for('message', check=is_same_author, timeout=5.0)
            except asyncio.TimeoutError:
                return await channel.send('Sorry, you took too long.')
            
            instarole = 'Please add an instasquad role to be mentioned.'
            for role in message.guild.roles:
                print(role.name)
                if role.name == 'instasquad':
                    instarole = role.mention

            async def poller():
                global latestPost
                post = get_latest_post(hashtag.content)
                text, url = formatPost(post)

                # don't forget to repoll!f
                while not self.is_closed():
                    if latestPost != post:
                        latestPost = post 
                        await message.channel.send(instarole + text + url)
                    await asyncio.sleep(60)
                
            self.bg_task = self.loop.create_task(poller())

            # await message.channel.send('Did it work?')
        elif message.content == 'bad word':
            await message.channel.send('Hey thats racist you cant say that!')
        else:
            pass
    

client = MyClient()
client.run(token)
