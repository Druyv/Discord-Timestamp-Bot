import discord
import datetime as dt

TOKEN = "BotTokenHere"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')
    # Zo kun je in je console zien dat de bot online gegaan is
    # Maar je kunt hier natuurlijk laten doen wat je wilt

@client.event
async def on_message(message):
    if message.author == client.user:
        # Zodat de bot niet op zichzelf reageert
        return
    
    if message.content.startswith('!tz '):
        msg = message.content.split()
        timestamp = f'{msg[1]} {msg[2]}' if len(msg) > 2 else f'{msg[1]}'
        await message.channel.send(get_discord_posix_timestamps(timestamp, msg[3])) if len(msg) > 2 else message.channel.send(get_discord_posix_timestamps(timestamp))


modifiers = ['t','D','f','F','R']
timezones = {'CAT':-1,
            'BET':-3,
            'AGT':-3,
            'PRT':-4,
            'IET':-5,
            'EST':-5,
            'CST':-6,
            'MST':-7,
            'PNT':-7,
            'PST':-8,
            'AST':-9,
            'HST':-10,
            'MIT':-11,
            'NST':12,
            'SST':11,
            'AET':10,
            'JST':9,
            'CTT':8,
            'VST':7,
            'BST':6,
            'PLT':5,
            'NET':4,
            'EAT':3,
            'ART':2,
            'EET':2,
            'ECT':1,
            'UTC':0,
            'GMT':0
}

def calc_time_diff(timezone):
    zone, diff = timezone.upper().split('+') if '+' in timezone else timezone.split('-')
    return int(diff) + timezones[zone]

def convert_iso2posix(iso_timestamp):
	return int(dt.datetime.timestamp(dt.datetime.fromisoformat(iso_timestamp)))
	
def get_discord_posix_timestamps(iso_timestamp, timezone = None):
    posix_timestamp = convert_iso2posix(iso_timestamp)

    if timezone:
        posix_timestamp = posix_timestamp - (3600*calc_time_diff(timezone))
	
    return "".join([f'`<t:{posix_timestamp}:{mod}>`\n<t:{posix_timestamp}:{mod}>\n\n' for mod in modifiers])


client.run(TOKEN)