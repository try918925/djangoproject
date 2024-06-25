import requests
# from hyper.contrib import HTTP20Adapter

unique_key = '6Lcpd6cpAAAAAEcR2vhGMyMK4R50xd5So3m9M5Kw'
url = f'https://www.google.com/recaptcha/api2/reload?k={unique_key}'

headers = {
    ':authority': 'www.google.com',
    ':method': 'POST',
    ':path': f'/recaptcha/api2/reload?k={unique_key}',
    ':scheme': 'https',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Content-Length': '8737',
    'Content-Type': 'application/x-protobuffer',
    # 'Cookie': '__Secure-3PSID=g.a000kQgXz5ZT-5ovjqt2n3u5B_suDV46H9xcJsnSrO_nUVEwGcGBgwrOJTGvM2f3RW86CAl7DQACgYKAeYSARASFQHGX2MiFWIHLJC3sXBvHZ83czO7IRoVAUF8yKqTzIRk3sAEsKSOhUkLRiEr0076; __Secure-3PAPISID=HHKEXj1EBlJiKkkj/A_o78tJ3nscO2uH06; NID=515=fijyj69Mhin2cTRAKVea8S88I7VDHef7jhp77YzKfc6dc4z9GoFodz1pHyDtMIOovyb-hc19lw9KgN3UkklwKj3hRCiJ1-7yESnAN64jefFJaph62-ME3b-fGx69kmYjjORgTTAKFhnNUX0C1Og_ASpxAvS--KdjK7wJfyBlQRpCXGkBe7S1AQGWSVkRTeU5l3389J47S2qFy2GWvgAaY5j5HvlhJB3wVmseajEhOe2knN_JRgJ5lh_ldD1oXa2bMOfnI3tNkK5P0K2kWFfZ6pRZXHh2wrADUzh_tWaC_aZ_VLldFGE636349butEI4ngCTqtjtyHTcTr-EKSkwr1NTN_VKYn30YormP4lsuVBPRZ5hZezlVD-sdxAbA7EulCW3qGQfSXZ1Dpx4; __Secure-3PSIDTS=sidts-CjEB3EgAEuw3xCgg0hU7mrDpEl36j6-CLplK3shqmP9vDla8tXDELq0DjteG3Ts0VEg8EAA; __Secure-3PSIDCC=AKEyXzWuLNFAs3K9x0TxViEtMrWQSPemkQVLCwCax5gdUVLulAPr9J44pAS5QFnN0xyAoC7vyA',
    'Origin': 'https://www.google.com',
    'Priority': 'u=1, i',
    'Referer': f'https://www.google.com/recaptcha/api2/anchor?ar=1&k={unique_key}&co=aHR0cHM6Ly9hcHAuYnVpbGRvbmh5YnJpZC5jb206NDQz&hl=zh-CN&v=KXX4ARWFlYTftefkdODAYWZh&size=invisible&cb=c44ah4ru2c7e',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

# sessions = requests.session()
# sessions.mount(url, HTTP20Adapter())
proxies = {
    'http': '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}

response = requests.post(url, proxies=proxies,headers=headers)


print(response.text)
