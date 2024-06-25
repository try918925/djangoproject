import asyncio
from pyppeteer import launch
import time

async def main():
    # 使用本地安装的 Chrome 浏览器
    browser = await launch(headless=False, executablePath='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
    page = await browser.newPage()
    await page.goto('https://app.buildonhybrid.com/faucet')
    while True:
        account_address = "111111111111111111111111111111111111111"
        await page.waitForXPath("input[placeholder='Input your HYB address...']")
        input_box = await page.xpath("input[placeholder='Input your HYB address...']")
        await input_box[0].click()
        await input_box[0].type(account_address)
        page.reload()
        await time.sleep(20)


    # await page.type('#inputFieldSelector', 'Hello, world!')
    # await page.click('#buttonSelector')
    # await page.screenshot({'path': 'example.png'})
    # await browser.close()

asyncio.get_event_loop().run_until_complete(main())
