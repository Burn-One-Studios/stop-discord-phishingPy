from stopPhishing.functions import list

async def phishingDomainCount():
    # return the amount of phishing domains
    domains = await list.listPhishingDomains()
    return len(domains)

async def suspiciousDomainCount():
    # return the amount of suspicious domains
    domains = await list.listSuspiciousDomains()
    return len(domains)

async def allDomainCount():
    # return the amount of all domains
    domains = await list.listAllDomains()
    return len(domains)