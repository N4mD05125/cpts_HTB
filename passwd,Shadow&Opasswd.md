<h1>Passwd, Shadow & Opasswd</h1>

![image](https://github.com/user-attachments/assets/8f9c6ec4-e133-4895-a290-2cd4f6d8a8b2)

![image](https://github.com/user-attachments/assets/0bb0310a-e568-4853-b1f1-416cb5420228)

TIếp nối từ bài Credential Hunting in Linux thì ta có kira:L0vey0u1! và ssh vào:

![image](https://github.com/user-attachments/assets/9d13fb16-8783-47f8-b1f0-c7b31707e774)

Sau khi lang thang 1 lúc thì không tìm thấy gì hữu ích trong kira:

![image](https://github.com/user-attachments/assets/2df69558-c53a-4bb1-bdfb-2566f0b20ce3)

Tôi chuyển sang user will:TUqr7QfLTLhruhVbCP từ bài trước để ssh vào và tiếp tục mày mò:

![image](https://github.com/user-attachments/assets/0054206b-b218-4ec0-ac40-d1664f5d9848)

Và tôi thấy trong .backups/ có hẳn passwd.bak và shadow.bak luôn:

![image](https://github.com/user-attachments/assets/b3dcd136-492a-4c8f-b762-b61d6981a8f0)

Dùng `python3 -m http.server 8888` bật lên để lấy .backups/ về máy thôi:

![image](https://github.com/user-attachments/assets/dc0b38e7-ac9b-4998-bc08-386c3765b47b)

`wget -r http://10.129.198.77:8888/.backups` để lấy folder .backups/ :

![image](https://github.com/user-attachments/assets/c951ca0c-1867-46ed-8b9f-0cf9113e9bef)

Và bắt đầu brute force thôi ` hashcat -m 1800 -a 0 ./unshadowed.hashes ../../rockyou.txt -o ./unshadowed.cracked`, nhớ dùng `unshadow ./passwd.bak ./shadow.bak > ./unshadowed.hashes` để kết hợp 2 file lại:

![image](https://github.com/user-attachments/assets/6404eedd-7a9a-4b55-a364-1b4d483c3143)

Mới được 6.81% sau 15p, lâu điênn

![image](https://github.com/user-attachments/assets/1708f769-1654-4cdf-b3c9-0a68dcf5572d)

100% cpu:

![image](https://github.com/user-attachments/assets/19332d2f-8d41-43be-8d50-072f0cd4e130)

Tôi thử lên mạng rồi dùng hashcat thông qua gpu thay vì cpu bằng cách tải cuda nvidia các thứ và chạy `hashcat.exe -d 2 -m 1800 -a 0 ../target/unshadowed.hashes ../target/rockyou.txt -o ../target/unshadowed.cracked`, check gpu bằng `hashcat -I` :

![image](https://github.com/user-attachments/assets/bc084912-25ac-41fd-b3fd-d2ec85681c65)

Và tôi cảm giác tốc độ vẫn vậy :(

![image](https://github.com/user-attachments/assets/727ede39-75af-418c-bc5b-b4685a4aa790)

Vãi, chạy gần 30p mà không có gì:

![image](https://github.com/user-attachments/assets/3d1c9bad-9a95-40a8-b74e-8ebaa6b1835e)

Đi đọc hint trên forum thì tôi thấy bảo là dùng cái biến thể của password.list kia `hashcat --force password.list -r custom.rule --stdout | sort -u > mut_password.list` và thu được 2 kết quả:

![image](https://github.com/user-attachments/assets/91a07f15-40c7-4246-bd59-ba5dead18457)

![image](https://github.com/user-attachments/assets/863c47a6-2f38-4fc5-b825-54adc669b133)

Và cái J0rd@n5 là của root:

![image](https://github.com/user-attachments/assets/0b430d56-6f0a-4098-ad1a-cb79f25be113)

