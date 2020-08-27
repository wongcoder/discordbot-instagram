# discordbot-instagram
Make a Discord bot that'll auto paste a link that matches a tag or a description.

Here's it working in action!

![Sample Image](https://raw.githubusercontent.com/wongcoder/discordbot-instagram/master/sample_images/sample.png)

# Deploying to AWS
Get into your EC2 instance, pip install, `git clone https://github.com/wongcoder/discordbot-instagram.git`, then run the bot using `python3 ./src/bot.py`.

The workflow has dramatically been simplified. Now, you should just have to clone the project, and make sure you have `pipenv` installed.

After that, you just need to run:

`pipenv install`

and then

`pipenv run bot`.

For more information, check out the Pipfile.

# Dependencies
The workflow is streamlined thanks to the use of pipenv. This is no longer needed.
Instead of this:
~~`pip install requests discord.py tinydb python-dotenv asyncio`~~

Just run: `pipenv install`, as mentioned above.

# How It Works

It avoids the Instagram API, and instead goes through the hidden API (?__a=1) which would require a nasty amount of OAuth (just saying, they could totally reduce how intensive my calls are if they made certain aspects about the API open...)

Since instagram really hates you though, you need to specify multiple cookies.

# Cookies

In order to scale this, and use an appropriate amount of time, we specify multiple accounts. These multiple accounts are randomized. I recommend about 10 to start out with, but you can go ahead and use something like 3 or 5. Just specify them in the .env like so:

`COOKIE=cookie1, cookie2, cookie3`.

If you do not know what I am talking about, look up how to acquire your sessionid, or open a github issue.

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

Unit tests
  - Finally added the basic framework for unit tests.

Cookie rotation
  - Added the abiltiy to rotate cookies to avoid Instagram getting angry!
