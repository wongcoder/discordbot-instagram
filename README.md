# discordbot-instagram
Make a Discord bot that'll auto paste a link that matches a tag or a description.

Here's it working in action!

![Sample Image](https://raw.githubusercontent.com/wongcoder/discordbot-instagram/master/sample_images/sample.png)

# Deploying to AWS
When you're deploying to AWS, make sure you create a .env.
Get into your EC2 instance, pip install, `git clone https://github.com/wongcoder/discordbot-instagram.git`, then run the bot using `python3 ./src/bot.py`.

# Dependencies
Since I'm too small brane to realize how to use Pipfiles in the same way we use node_modules, I manually write it out. Please submit a PR with a pull request if you want to spend your time changing it. Otherwise, take the L and just use 

`pip install requests discord.py tinydb python-dotenv asyncio`

# How it works

It avoids the Instagram API, which would require a nasty amount of OAuth (just saying, they could totally reduce how intensive my calls are if they made certain aspects about the API open...)

First, it calls a GET request. The program that we're usings, requests, happens to have a built in JSON formatter, which it then returns the JSON as a dict. Then it's just a matter of breaking down that dict into usable data!

# Usage

- `$fetch` asks you to enter a hashtag that you would like to subscribe to. After that, it looks for latest posts and will keep querying every 5 seconds, or whatever is set in `QUERYING_TIME`.

- `$block` asks you to enter a URL. The URL should be an instagram post from a user that you want blocked. 
  - Make sure the formatting is correct.
    - CORRECT: https://www.instagram.com/p/B8BOw-0Beqd/
    - INCORRECT:  https://www.instagram.com/p/B8BOw-0Beqd

# TODO:

Refactor (Separate out tasks)
  - Tasks can generally be made globally. then I can just call self.bg_task later.

Multi Server Support
  - You can definitely connect the bot to more than one server, but the latestText can only have one. This means that you're going to have a conflict of latestText if you have it running on two different servers. One of the ways we can solve this issue is via TinyDB, and storing it alongside.

## Completed:
Add a block list 
  - This can be accomplished with TinyDB and performing an author lookup before sending.
  - Task has been completed. Now in integration testing (AKA LIVE)
Prevent reposts
  - Reposts occur if the previous latest post was removed.

  
