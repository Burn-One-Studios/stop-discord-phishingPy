from stopPhishing.functions.amount import allDomainCount, phishingDomainCount, suspiciousDomainCount
from stopPhishing.functions.check import checkDomain, checkMessage, susDomainsChecker
from stopPhishing.functions.list import listAllDomains, listPhishingDomains, listSuspiciousDomains

__version__ = '0.1.0'

__all__ = [
    'allDomainCount',
    'checkDomain',
    'checkMessage',
    'listAllDomains',
    'listPhishingDomains',
    'listSuspiciousDomains',
    'phishingDomainCount',
    'suspiciousDomainCount',
    'susDomainsChecker',
]