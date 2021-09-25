# Discord-Timestamp-Bot

Discord has these very useful Unix timestamps, but generating can be a bit of a pain. You'd have to go somewhere to calculate the Unix timestamp, look up what formatting you want and then build the timestamp. But no longer, because this bot can do it for you! 

Simply feed it a date in ISO format (YYYY-MM-DD [HH:MM]) and augment it with your timezone (like PST+3, or UTC-2) if necessary, and the bot gives you a handy dandy overview of copy/pastable configurations for your timestamps, ready to paste into Discord :) 

I don't personally have this bot hosted anywhere, but feel free to use the sourcecode to host it yourself. All you need to do is [install the discord API module](https://discordpy.readthedocs.io/en/latest/intro.html) and create your own bot through the [Discord Developer Portal](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal). 

The actual generation of the timestamps doesn't use anything Discord specific, so the code can be used without actually hosting a bot there. You won't be able to see the results of what you made if you use it outside of Discord, though, so picking the right style can be harder.

![Bot output](resources/timestamp.png?raw=true "Bot Output")
