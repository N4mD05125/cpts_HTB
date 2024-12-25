<h1>Footprinting Lab - Easy</h1>

![image](https://github.com/user-attachments/assets/295bcc9c-ec10-4f50-9187-df3c0e943dd4)

![image](https://github.com/user-attachments/assets/bb7bf428-658a-465b-bc79-70d9d23cb299)

Tôi có địa chỉ IP và username:password là ceil:qwer1234, mục tiêu là capture the flag
Đầu tiên tôi recon nằng nmap với lệnh: `nmap -A 10.129.220.245`, vì -A nên mất kha khá thời gian, kết quả là:


Có các cổng 21,22,53,2121 tương ứng với các dịch vụ là ftp, ssh, domain, ftp. Tôi sẽ thử với ssh (port 22) trước:

![image](https://github.com/user-attachments/assets/8b793c54-20f2-4d20-a8e6-843b75781f5c)

Không kết nối được, nó cần key mà tôi không có, tôi chuyển sang port 53 nhưng không có gì để khai thác, chuyển hướng tiếp sang 21 và 2121 vì nó đều là ftp, 2 cái khác ở chỗ: port 21 là `220 ProFTPD Server (ftp.int.inlanefreight.htb) [10.129.220.245]` và 2121 là `220 ProFTPD Server (Ceil's FTP) [10.129.220.245]`
Sử dụng `ftp 10.129.220.245` để dùng ftp ở port 21:

![image](https://github.com/user-attachments/assets/aaa59aa1-39c0-45ee-b331-ecfa990cbbab)

Vào thành công nhưng đi lanh quanh không tìm thấy gì hữu ích, sang port 2121 bằng `ftp 10.129.220.245 2121`:

![image](https://github.com/user-attachments/assets/73a847ab-9dca-469a-8577-e2a9a93eb145)

Tôi thấy có nhiều thứ để nghịch hơn, khi tôi vào `,ssh` thì có key, nhanh chóng dùng `get` để tải các file này về:

![image](https://github.com/user-attachments/assets/861727ac-96c9-4902-b601-e956e8172bed)

Lưu folder `.ssh` về máy, cd vào và dùng `ssh -v ceil@10.129.220.245`:

![image](https://github.com/user-attachments/assets/1402fd29-2aa3-4e78-aad5-509d7e2a90a2)

Và ta tìm được flag.txt
