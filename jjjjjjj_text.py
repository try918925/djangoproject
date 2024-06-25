from automation.task import Task, BrowserTask
import asyncio
import pyppeteer.launcher
import csv, time
import requests, math
from selenium import webdriver
from automation.tasks.exception import OpenReadTimeout
from automation.tasks.exception import OpenBrowserException
from web3 import Web3
import concurrent.futures


@Task.register("katla_territorial_waters_one")
class BerachainFaucetTask(BrowserTask):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ws_page_url = self.browser.ws_page_url
        self.url = 'http://6.6.6.6:54321/exchange?different=1'
        self.infura_url = "https://ethereum-holesky-rpc.publicnode.com"
        self.web3 = Web3(Web3.HTTPProvider(self.infura_url))
        self.waters_list = list()


    def process_row(self,row):
        balance = self.web3.eth.get_balance(row[1]) / math.pow(10, 18)
        if balance >= 0.1:
            print(f"账户地址为：{row[0]},领水成功，余额为：{balance}")
        else:
            self.waters_list.append(row[1].lower())

    def filed_etc(self,file_name):
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(self.process_row, csv_reader)

    def main(self):
        file_csv = [r"C:\Users\vmuser\Desktop\no_water.csv"]
        for file_name in file_csv:
            self.filed_etc(file_name)



    def execute(self):
        self.main()
        asyncio.run(self.getfaucet_start())

    async def main_task(self, rows, browser_id):
        try:
            await self.get_page_url(browser_id)
            print("self.get_page_url()")
            time.sleep(5)
            browser = await self.open_browser()
            time.sleep(10)
            page = await browser.newPage()
            time.sleep(5)
            await self.set_view_port(page)
            time.sleep(5)
            await self.requests_url(page)
            print("更新ip完成")
            time.sleep(10)
            try:
                await page.goto('https://holesky-faucet.pk910.de', {'timeout': 270000})
            except Exception:
                pass
            print("打開頁面完成")
            time.sleep(5)
            for row in rows:
                try:
                    await page.reload()
                    print("當前領水頁面")
                    await self.submit_reward(page, row)
                    print(f"領水成功地址：{row}")
                except Exception as error:
                    print(f'地址{row},結果：{error}')
                    await page.goto('https://holesky-faucet.pk910.de', {'timeout': 270000})
        except Exception as error:
            print(f"main_task:{error}")
            time.sleep(20)


    async def getfaucet_start(self):
        main_data = []
        with open(r'C:\Users\vmuser\Desktop\no_water.csv', 'r') as file:
            csv_reader = csv.reader(file)
            all_data = []
            len_csv = [i for i in csv_reader]
            row_data = set([a[1] for a in len_csv])
            for index, row in enumerate(row_data):
                all_data.append(row.lower())
                if len(all_data) == 20:
                    main_data.append(all_data)
                    all_data = []
                else:
                    if (index + 1) == len(len_csv):
                        main_data.append(all_data)
        browser_id = ["jeqtyrh", "jeqtyri", "jeqtyrf", "jeqtyre", "jeqtyrd", "jeqtyrb", "jeqtyra", "jeqtyr9", "jeqtyr8",
                      "jeqtyr7"]
        for index, data in enumerate(main_data):
            num = index % int(len(browser_id))
            try:
                await self.main_task(data, browser_id[num])
                self.close_ads(browser_id)
            except Exception as error:
                print(f"self.main_task(data,browser_id[num]):{error}")
                time.sleep(10)
            print("停止一定的時間，打開下個瀏覽器")
            time.sleep(10)
            print("等待結束，準備打開下個瀏覽器")

    async def submit_reward(self, page, account_address):
        # 等待页面加载完毕
        while True:
            try:
                await page.waitForXPath('//input[@placeholder="Please enter ETH address or ENS name"]')
                # 定位输入框，并输入账户地址
                input_box = await page.xpath('//input[@placeholder="Please enter ETH address or ENS name"]')
                await input_box[0].click()
                await input_box[0].type(account_address)
                break
            except Exception:
                await page.waitForXPath('//button[text()="Return to startpage"]')
                Return_button = await page.xpath('//button[text()="Return to startpage"]')
                await Return_button[0].click()
                time.sleep(1)

        time.sleep(30)

        await page.waitForXPath('//button[text()="Start Mining"]')
        start_button = await page.xpath('//button[text()="Start Mining"]')
        await start_button[0].click()

        await page.waitForXPath('//div[text()="Your Mining Reward:"]/ancestor::div[1]//div[@class="status-value"]')
        mining_value = await page.xpath(
            '//div[text()="Your Mining Reward:"]/ancestor::div[1]//div[@class="status-value"]')
        print('準備領水')
        while True:
            mining_text = await page.evaluate('(element) => element.textContent', mining_value[0])
            eth_data = mining_text.split(' ')[0]
            eth_data = float(eth_data)
            if eth_data >= 0.1:
                break
            time.sleep(0.2)
        print("陵水完成")

        await page.waitForXPath('//button[text()="Stop Mining & Claim Rewards"]')
        Claim_button = await page.xpath('//button[text()="Stop Mining & Claim Rewards"]')
        await Claim_button[0].click()

        await page.waitForXPath('//button[text()="Claim Rewards"]')
        Rewards_button = await page.xpath('//button[text()="Claim Rewards"]')
        await Rewards_button[0].click()
        time.sleep(2)
        while True:
            try:
                await page.waitForXPath('//span[text()="Tweet"]')
                print('推特出现完成')
                break
            except TimeoutError:
                print("元素未出现，继续等待...")
            time.sleep(0.5)

        await page.reload()

        await page.waitForXPath('//button[text()="Return to startpage"]')
        Return_button = await page.xpath('//button[text()="Return to startpage"]')
        await Return_button[0].click()

    async def set_view_port(self, page):
        await page.setViewport(
            {
                "width": 3046,
                "height": 1586,
            }
        )

    async def requests_url(self, page):
        try:
            request = await page.goto(self.url)
            print(request)
        except Exception as error:
            print(error)

    async def open_browser(self):
        browser = await pyppeteer.launcher.connect(
            {"browserWSEndpoint": self.ws_page_url}
        )
        return browser

    async def get_page_url(self, browser_id):
        try:

            params = {
                "user_id": browser_id,
                "open_tabs": self.browser.open_tabs,
                "ip_tab": self.browser.ip_tab,
                "clear_cache_after_closing": self.browser.clear_cache_after_closing,
                "launch_args": f'["--disable-csp","--disable-notifications","--window-position={self.browser.windows_position[0]},{self.browser.windows_position[1]}"]',
            }
            resp = requests.get(
                self.browser.browser_open_url,
                params=params,
                timeout=120,
            ).json()
            code = resp["code"]
            if code != 0:
                raise OpenBrowserException(resp["msg"])
            self.chrome_driver = resp["data"]["webdriver"]
            self.chrome_options = webdriver.ChromeOptions()
            ws_url = resp["data"]["ws"]["selenium"]
            self.ws_page_url = resp["data"]["ws"]["puppeteer"]
            self.chrome_options.add_experimental_option("debuggerAddress", ws_url)
            self.driver = webdriver.Chrome(
                self.chrome_driver,
                options=self.chrome_options,
            )

        except requests.exceptions.ReadTimeout as e:
            raise OpenReadTimeout("open browser timeout!", e)
        except Exception as e:
            raise OpenBrowserException("unknown exception ", e)
