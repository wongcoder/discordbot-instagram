# discordbot-instagram
Make a Discord bot that'll auto paste a link that matches a tag or a description

![Sample Image](https://raw.githubusercontent.com/wongcoder/discordbot-instagram/master/sample_images/sample.png)

# Deploying to AWS
When you're deploying to AWS, make sure you create a .env.
Get into your EC2 instance, clone and pipinstall, then run the bot.

# Dependencies
Since I'm too small brane to realize how to use Pipfiles in the same way we use node_modules, I manually write it out. Please submit a PR with a pull request if you want to spend your time changing it.

`git clone https://github.com/wongcoder/discordbot-instagram.git`
`pip install requests discord.py tinydb python-dotenv asyncio`

