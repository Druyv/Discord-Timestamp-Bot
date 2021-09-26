import discord
import datetime as dt
import timestamp_utils as tsu

TOKEN = "BotTokenHere"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!tz '):
        msg = message.content.split()
        timestamp = f'{msg[1]} {msg[2]}' if len(msg) > 2 else f'{msg[1]}'
        await message.channel.send(tsu.get_discord_posix_timestamps(timestamp, msg[3], verbose!='-v' in message.content)) if len(msg) > 2 else message.channel.send(get_discord_posix_timestamps(timestamp, verbose!='-v' in message.content))

client.run(TOKEN)