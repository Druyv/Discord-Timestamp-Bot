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