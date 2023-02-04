# Stop Discord Phishing

![domains](https://img.shields.io/badge/dynamic/json?color=79BFAA&label=Domains&query=count&url=https%3A%2F%2Fapi.schunk.dev%2Fapi%2Fdomain%2Fcount&style=for-the-badge)
![license](https://img.shields.io/github/license/Burn-One-Studios/stop-discord-phishingPy?color=black&style=for-the-badge)
![stars](https://img.shields.io/github/stars/Burn-One-Studios/stop-discord-phishingPy?style=for-the-badge)
![version](https://img.shields.io/pypi/v/stopPhishing?color=black&style=for-the-badge)


## About this Package

[stop-discord-phishingPy](https://github.com/Burn-One-Studios/stop-discord-phishingPy) works with the [list of phishing Domains](https://github.com/nikolaischunk/discord-phishing-links) to detect [phishing](https://en.wikipedia.org/wiki/Phishing) domains in messages on [Discord](https://discord.com).

This is the unofficial repository & pypi package which provides functionality in detecting phising links.

If you like this project consider giving it a ⭐ and feel free to contribute to this project!

## Source

If you found a domain that is not detected yet, contribute it to the [discord-phishing-links](https://github.com/nikolaischunk/discord-phishing-links) repository!

## Add Package to your Project

```bash
pip install stopPhishing
```

## How to use:

```py
import stopPhishing
```

### Check if String contains a Phishing Link:

```python
TEST_MESSAGE = "this is definitivelynotascamdomain.ru that should be checked";

#Check string on confirmed Phishing Domains
async def checkMessage(TEST_MESSAGE):
  isGrabber = await stopPhishing.checkMessage(message) #True
  print(isGrabber)
  return isGrabber

#Check string on confirmed Phishing Domains & suspicious Domains RECOMMENDED!
async def checkMessageFull(TEST_MESSAGE):
  isGrabber = await stopPhishing.checkMessage(message, true) #True
  print(isGrabber)
  return isGrabber

```

### List all Domains:

```py
async def listPhishingDomains():
  links = await stopPhishing.listPhishingDomains() //[]
  #Now you can do something with Array with all the confirmed Phishing Domains in it
  print(links)
  return links

async def listSuspiciousDomains():
  links = await stopPhishing.listSuspiciousDomains() #[]
  #Now you can do something with Array with all the suspicious Domains in it
  print(links)
  return links

async def listAllDomains():
  links = await stopPhishing.listAllDomains() #[]
  #Now you can do something with Array with all the suspicious and confirmed phishing Domains in it
  print(links)
  return links

```

### Get Domain Count:

```py
#Get the amount of all Phishing and Suspicious Domains
async def getDomainAmount():
  amount = await stopPhishing.domainCount() #Number
  print(amount)
  return amount

#Get the amount of all Phishing Domains
async def getPhishingDomainAmount():
  const amount = await stopPhishing.phishingDomainCount() #Number
  print(amount)
  return amount

#Get the amount of all Suspicious Domains
async def getSuspiciousDomainAmount():
  amount = await stopPhishing.suspiciousDomainCount() #Number
  print(amount)
  return amount

```

## Cache

To prevent an excess of requests and load, we added a Cache of `30 minutes`!

## List of Phishing Domains

Find the complete List of Phishing Domains here: [discord-phishing-links](https://github.com/nikolaischunk/discord-phishing-links)

## Attributions
nikolaischunk - "stop-discord-phishing" project owner and npm package maintainer

mahtoid - code review

## Changelog

#### 0.0.1

- Initial (and Test) Upload
