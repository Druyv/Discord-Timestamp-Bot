timezones ={'CAT':-1,
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
    
modifiers =['t','D','f','F','R']
    
def get_discord_posix_timestamps(iso_timestamp, timezone = None, verbose = True):
    posix_timestamp = tsu.convert_iso2posix(iso_timestamp)

    if timezone:
        posix_timestamp = posix_timestamp - (3600*tsu.calc_time_diff(timezone))
	
    if verbose:
        return "".join([f'`<t:{posix_timestamp}:{mod}>`\n<t:{posix_timestamp}:{mod}>\n\n' for mod in modifiers])
    else:
        return "".join([f'`<t:{posix_timestamp}:{mod}>`' for mod in modifiers])