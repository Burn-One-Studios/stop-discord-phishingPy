from stopPhishing.functions import list

async def checkMessage(message_content : str, scanSuspiciousDomains : bool = False):
    # check if a message contains a phishing link
    # returns True if a phishing link was found, False otherwise
    domains = await list.listPhishingDomains()
    if scanSuspiciousDomains:
        domains += await list.listSuspiciousDomains()
    for domain in domains:
        if domain in message_content:
            return True
    return False

async def checkDomain(domainToCheck : str):
    # check if a domain is a phishing domain
    # returns True if the domain is a phishing domain, False otherwise
    domains = await list.listPhishingDomains()
    for domain in domains:
        if domain == domainToCheck:
            return True
    return False

async def susDomainsChecker(domainToCheck : str):
    # check if a domain is a suspicious domain
    # returns True if the domain is a suspicious domain, False otherwise
    domains = await list.listSuspiciousDomains()
    for domain in domains:
        if domain == domainToCheck:
            return True
    return False