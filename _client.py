import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def br():
    browser = await launch({
        'defaultViewport': {'width': 1920, 'height': 1080},
        'args': ["--fast-start", '--start-maximized','--disable-infobars',"--disable-notifications",],
        'headless': False,
        'ignoreDefaultArgs': ["--enable-automation"],
        "ignoreHTTPSErrors": True
        })
    page = list(await browser.pages())[0]
    await page.evaluateOnNewDocument('navigator.mediaDevices.getUserMedia = navigator.webkitGetUserMedia = navigator.mozGetUserMedia = navigator.getUserMedia = webkitRTCPeerConnection = RTCPeerConnection = MediaStreamTrack = undefined')
    await stealth(page)  
    return page, browser



async def main():
    page, browser = await br()

    await page.goto('https://whoer.net/ru')
    await page.waitFor(100000) 
    await browser.close()

asyncio.run(main())