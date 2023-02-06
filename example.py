import stopPhishing

TEST_MESSAGE = "this is definitivelynotascamdomain.ru that should be checked"

#Check string on confirmed Phishing Domains
async def checkMessage(TEST_MESSAGE):
  isGrabber = await stopPhishing.checkMessage(TEST_MESSAGE) #True
  print(f"checkMessage: {isGrabber}")
  return isGrabber

#Check string on confirmed Phishing Domains & suspicious Domains RECOMMENDED!
async def checkMessageFull(TEST_MESSAGE):
  isGrabber = await stopPhishing.checkMessage(TEST_MESSAGE, True) #True
  print(f"checkMessageFull: {isGrabber}")
  return isGrabber

async def listPhishingDomains():
  links = await stopPhishing.listPhishingDomains() #[]
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

async def getDomainAmount():
    amount = await stopPhishing.allDomainCount() #Number
    print(amount)
    return amount

#Get the amount of all Phishing Domains
async def getPhishingDomainAmount():
    amount = await stopPhishing.phishingDomainCount() #Number
    print(amount)
    return amount

#Get the amount of all Suspicious Domains
async def getSuspiciousDomainAmount():
    amount = await stopPhishing.suspiciousDomainCount() #Number
    print(amount)
    return amount

async def main():
  await checkMessage(TEST_MESSAGE)
  await checkMessageFull(TEST_MESSAGE)
  await listPhishingDomains()
  await listSuspiciousDomains()
  await listAllDomains()
  await getDomainAmount()
  await getPhishingDomainAmount()
  await getSuspiciousDomainAmount()

if __name__ == "__main__":
    # running the script directly normally runs under a asynic function with a await
    import asyncio
    asyncio.run(main())