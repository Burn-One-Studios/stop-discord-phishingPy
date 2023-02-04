import requests, datetime

URL_GUARANTEED = "https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/domain-list.json"

URL_SUSPICIOUS = "https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/suspicious-list.json"

CACHE_DURATION = 1000 * 60 * 30 # 30 minutes

cache = dict()

async def update_lists():
    # Update the lists of phishing domains
    global cache
    if ( 
        not cache.get("guaranteed")  
        or not cache.get("suspicious") 
        or not cache.get("last_update") 
        or cache.get("last_update") + CACHE_DURATION < datetime.datetime.now().timestamp()
    ):
        cache["last_update"] = datetime.datetime.now().timestamp()
        cache["guaranteed"] = requests.get(URL_GUARANTEED).json()
        cache["suspicious"] = requests.get(URL_SUSPICIOUS).json()

async def listPhishingDomains():
    # return the list of phishing domains
    await update_lists()
    return cache["guaranteed"]['domains']

async def listSuspiciousDomains():
    # return the list of suspicious domains
    await update_lists()
    return cache["suspicious"]['domains']

async def listAllDomains():
    # return the list of all domains
    await update_lists()
    return cache["guaranteed"]['domains'] + cache["suspicious"]['domains']