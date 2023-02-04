from stopPhishing.functions import list

async def checkMessage(message_content : str, scanSuspiciousDomains : bool = False):
    """
    Check if a message contains a phishing domain
    :param: message_content: str - the message to check
    :param: scanSuspiciousDomains: bool - whether to scan suspicious domains or not (default: False)
    :returns: bool - True if the message contains a phishing domain, False otherwise
    """
    domains = await list.listPhishingDomains()
    if scanSuspiciousDomains:
        domains += await list.listSuspiciousDomains()
    for domain in domains:
        if domain in message_content:
            return True
    return False

async def checkDomain(domainToCheck : str):
    """
    Check if a domain is a phishing domain
    :param: domainToCheck: str - the domain to check
    :returns: bool - True if the domain is a phishing domain, False otherwise
    """
    domains = await list.listPhishingDomains()
    for domain in domains:
        if domain == domainToCheck:
            return True
    return False

async def susDomainsChecker(domainToCheck : str):
    """
    Check if a domain is a suspicious domain
    :param: domainToCheck: str - the domain to check
    :returns: bool - True if the domain is a suspicious domain, False otherwise
    """
    domains = await list.listSuspiciousDomains()
    for domain in domains:
        if domain == domainToCheck:
            return True
    return False