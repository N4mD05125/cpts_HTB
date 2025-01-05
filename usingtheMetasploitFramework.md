![image](https://github.com/user-attachments/assets/08f9f396-ea5a-4771-a99e-6d39fad8e573)

![image](https://github.com/user-attachments/assets/3fcd2a87-4f84-4040-9ccd-bd95b16c5b1b)

Dùng `nmap -sV 10.129.175.109` để quét các ports và version của nó:

![image](https://github.com/user-attachments/assets/375c72b2-973a-4e37-bd99-aa8169a0e736)

Search trên msfconsole thì không đem lại gì:

![image](https://github.com/user-attachments/assets/799efbad-9b5f-41a8-bd06-9a0da4fdfcf6)

Search google cũng không thấy gì, đọc lại đề thì có yêu cầu khai thác Apache Druid, tôi thử search trên đó và khai thác (do trên máy tôi không có ip cho LHOST nên phải dùng máy của htb):

![image](https://github.com/user-attachments/assets/1c970d4d-fcd5-4955-aac7-7a7b6e0ae14b)

Điền các thông tin như RHOSTS, LHOST và run:

![image](https://github.com/user-attachments/assets/5e0d5aa8-7c0f-497f-9f9b-7f021e89f1f5)

![image](https://github.com/user-attachments/assets/4ffe0bf0-f82b-4903-8d04-d7ab4cfdaad0)

Và theo chatgpt thì đây là mối quan hệ giữa 2 cái:

![image](https://github.com/user-attachments/assets/1d3c0066-71e3-4910-99e0-6070f19b8939)
