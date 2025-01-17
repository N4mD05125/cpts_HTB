<h1>Credential Hunting in Linux</h1>

![image](https://github.com/user-attachments/assets/dde075d0-7321-4c72-8636-5f63fa0ddef0)

![image](https://github.com/user-attachments/assets/b78b6047-e7e6-46ed-9009-789da6393e16)

Dùng `nmap -sV 10.129.231.129` để kiểm tra các port:

![image](https://github.com/user-attachments/assets/9aca6bf1-36f9-431e-8d17-b850506df584)

Đọc hint thì có vẻ là user là kira, còn pass thì chắc là biến tấu của LoveYou1 vì tôi thử dùng kira:LoveYou1 nhưng không vào được:

![image](https://github.com/user-attachments/assets/91a54ce5-f651-400b-bfa9-2fff37dcf27d)

Dùng `hashcat --force passKira.txt -r custom.rule --stdout | sort -u > mut_password.list` để tạo các biến thể:

![image](https://github.com/user-attachments/assets/88d87618-1726-4505-8d7a-4a06eb608e1c)

Thực ra cũng có thể dùng hydra để brute nữa, nhưng mà tôi thích msfconsole:

![image](https://github.com/user-attachments/assets/682c36c1-f5df-4191-a0fd-6b05a4b773be)

Có kira:L0vey0u1! thì vào ssh thôi:

![image](https://github.com/user-attachments/assets/efc79079-ca72-48f2-b21a-2d30c50257e9)

Bật http bằng `python3 -m http.server 8888` lên và tải 1 số tool về, khi tải dùng wget nhớ thêm -r vào để tải folder:

![image](https://github.com/user-attachments/assets/496a0bb9-6b29-4230-8cca-c9b85f4d896e)

![image](https://github.com/user-attachments/assets/9cb7f0c6-717d-4267-b101-72bf9417f361)

Chạy LaZagne thì ra được will@inlanefreight.htb:TUqr7QfLTLhruhVbCP

![image](https://github.com/user-attachments/assets/f9935610-14ec-4e44-b72d-ee257ba0048b)

![image](https://github.com/user-attachments/assets/5d6260be-e011-48d3-98b8-52724c0437ee)

