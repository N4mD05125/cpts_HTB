<h1>Skills Assessment - Web Fuzzing</h1>

![image](https://github.com/user-attachments/assets/3095dc35-d929-4624-a6e7-499c21e8531a)

![image](https://github.com/user-attachments/assets/5aca0975-f1d9-479d-a971-32fb4f5db823)

Đầu tiên tôi cần nhập vào /etc/hosts để dùng:

![image](https://github.com/user-attachments/assets/255eb7e2-f58b-440c-aced-84e1a14e3f67)

Sau khi dùng `ffuf -w subdomains-top1million-110000.txt:FUZZ -u http://academy.htb:35624/ -H 'Host: FUZZ.academy.htb'`:

![image](https://github.com/user-attachments/assets/a1b8e90f-8822-47dc-bfdc-33fc7bf7bfc0)

Thêm cả mấy cái tên của subdomain vừa tìm ra vào /etc/hosts luôn:

![image](https://github.com/user-attachments/assets/654251f1-149e-4718-87e1-75c587077736)

Check các extension bằng lệnh `ffuf -w web-extensions.txt:FUZZ -u http://academy.htb:35384/indexFUZZ`, nhớ chạy cả 3 subdomain kia nữa và có được 3 cái extensions:

![image](https://github.com/user-attachments/assets/1580c600-b748-4d1a-8adc-e1a556287a2e)

câu tiếp theo thì tôi chạy 3 lệnh này:

![image](https://github.com/user-attachments/assets/8b18637d-4dae-4a0e-9f6a-4d392b0e122a)


