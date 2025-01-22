<h1>Skills Assessment - Web Fuzzing</h1>

![image](https://github.com/user-attachments/assets/3095dc35-d929-4624-a6e7-499c21e8531a)

![image](https://github.com/user-attachments/assets/5aca0975-f1d9-479d-a971-32fb4f5db823)

Đầu tiên tôi cần nhập vào /etc/hosts để dùng:

![image](https://github.com/user-attachments/assets/255eb7e2-f58b-440c-aced-84e1a14e3f67)

Sau khi dùng `ffuf -w subdomains-top1million-110000.txt:FUZZ -u http://academy.htb:35624/ -H 'Host: FUZZ.academy.htb'`:

![image](https://github.com/user-attachments/assets/a1b8e90f-8822-47dc-bfdc-33fc7bf7bfc0)
