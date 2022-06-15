import asyncio
import pyppeteer
from pyppeteer_stealth import stealth

import json
import traceback
import requests
import os
from time import sleep, time
import random
from user_agent import generate_user_agent, generate_navigator
import shutil


pyppeteer.PUPPETEER_PRODUCT = 'firefox'

async def br():
    userDataDir = f'{os.getcwd()}\\FIRE'
    if not os.path.exists(path = userDataDir):
        os.mkdir(path = userDataDir)

    prefs = 'user_pref("media.peerconnection.enabled", false);\n'\
            'user_pref("media.navigator.enabled", false);\n'\
            'user_pref("privacy.resistFingerprinting", true);\n'\
            'user_pref("media.volume_scale", "0.0");\n'\
            'user_pref("webgl.disabled", true);\n'\
            'user_pref("gfx.direct2d.disabled", true);\n'\
            'user_pref("layers.acceleration.disabled", true);\n'\
            'user_pref("geo.enabled", true);\n'\
            'user_pref("network.trr.mode", 2);\n'\
            'user_pref("network.trr.uri", "1.1.1.1");\n'\
            'user_pref("network.trr.bootstrapAddress", "1.1.1.1");\n'\
            'user_pref("network.security.esni.enabled", true);\n'\
            'user_pref("network.dns.echconfig.enabled", true);\n'\
            'user_pref("privacy.donottrackheader.enabled", true);\n'\
            'user_pref("network.dns.use_https_rr_as_altsvc", true);\n'\

    with open(userDataDir+'\\user.js', 'w') as f:
        f.write(prefs)


    browser = await pyppeteer.launch({
        'defaultViewport': {'width': 1920, 'height': 1080},
        'args': ["--fast-start", '--start-maximized','--disable-infobars',"--disable-notifications",],
        'headless': False,
        'ignoreDefaultArgs': ["--enable-automation"],
        "ignoreHTTPSErrors": True,
        "userDataDir": userDataDir,
        'product': 'firefox'
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