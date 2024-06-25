from curl_cffi import requests as req





headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-protobuffer',
    'origin': 'https://www.google.com',
    'priority': 'u=1, i',
    'referer': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcpd6cpAAAAAEcR2vhGMyMK4R50xd5So3m9M5Kw&co=aHR0cHM6Ly9hcHAuYnVpbGRvbmh5YnJpZC5jb206NDQz&hl=en-US&v=KXX4ARWFlYTftefkdODAYWZh&size=invisible&cb=s6xoq7e9zw8z',
    # 'referer': 'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcpd6cpAAAAAEcR2vhGMyMK4R50xd5So3m9M5Kw&co=aHR0cHM6Ly9hcHAuYnVpbGRvbmh5YnJpZC5jb206NDQz&hl=en-US&v=KXX4ARWFlYTftefkdODAYWZh&size=invisible&cb=s6xoq7e9zw8z',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-client-data': 'CIi2yQEIprbJAQipncoBCO31ygEIlKHLAQiFoM0BCMaFzgEY9snNAQ==',
    # 'x-client-data': 'CIi2yQEIprbJAQipncoBCO31ygEIlKHLAQiFoM0BCMaFzgEY9snNAQ==',
}

params = {
    'k': '6Lcpd6cpAAAAAEcR2vhGMyMK4R50xd5So3m9M5Kw',
}


proxy = {
    'http':'127.0.0.1:7890',
    'https':'127.0.0.1:7890'
}
http = req.Session(timeout=50, headers=headers, proxies=proxy, impersonate="chrome120",
                                     verify=False)


response = http.post('https://www.google.com/recaptcha/api2/reload', params=params,headers=headers)

print(response)