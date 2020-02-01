import os

import discord
import asyncio
from instascraper import get_latest_post
from setup import get_env

DISCORD_TOKEN, USER_ID = get_env()

# Init Discord client
client = discord.Client()

# globals
latest_url = 'None'
QUERYING_SPEED = 5

def formatPost(post):
    text = post['edge_media_to_caption']['edges'][0]['node']['text']
    url = 'https://www.instagram.com/p/' + post['shortcode'] + '/'
    author = post['owner']['id']
    return text, url, author

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
        if message.content.startswith('$fetch') and (channel.permissions_for(message.author).administrator == True or message.author.id == USER_ID) :
            print('evaluate as true')
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
                # don't forget to repoll!f
                while True:
                    global latest_url
                    post = get_latest_post(hashtag.content)
                    text, url, author = formatPost(post)
                    text = text[:1900]
                    if latest_url != url and author != '4939318395':
                        print('current latesttext ' + latest_url)
                        print('new post? ' + text)
                        print('author? ' + author)
                        latest_url = url
                        await message.channel.send(instarole + "\n" + text + " " + url)
                    await asyncio.sleep(QUERYING_SPEED)
            self.bg_task = self.loop.create_task(poller())

            # await message.channel.send('Did it work?')
        elif message.content == '$test':
            await message.channel.send('I am still functional! Thanks for checking on me, uwu')
        elif message.content == 'gods lesson':
            await message.channel.send('Step 1: Dump your girl(s). Step 2: Acquire god pussy. Let it be put on the record.')
        elif message.content == 'fuck squiggles':
            await message.channel.send('LOL I HAVE NO WORDS FOR THAT CUNT')
        elif message.content == 'who is squiggles':
            await message.channel.send('Processing...')
            await message.channel.send('Here are your results: Squiggle, a massive fucking dumb cunt.')
        else:
            pass
    

client = MyClient()
client.run(DISCORD_TOKEN)
