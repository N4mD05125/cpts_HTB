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

![image](https://github.com/user-attachments/assets/cd3192c0-babc-4301-8548-a1228f21cbe0)

Sau 1 khoảng 2 tiếng rưỡi là ra http://faculty.academy.htb:37126/courses/linux-security.php7, cái ip cũ curl không ra nên đổi ip mới để dùng<br>

Câu tiếp theo tôi chạy `ffuf -w burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:37126/courses/linux-security.php7?FUZZ=key > output.txt` và `ffuf -w /mnt/d/wordlist/seclist_htb/seclists/Discovery/Web-Content/burp-parameter-names.txt:FUZZ -u http://faculty.academy.htb:37126/courses/linux-security.php7 -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded'`, 1 cái là GET, 1 cái POST để mò parameter:

![image](https://github.com/user-attachments/assets/d738d9bf-e1d6-417e-aade-4781afa4dbe7)

![image](https://github.com/user-attachments/assets/1d3398eb-b477-4adf-89cb-9eef5a44e9da)

Và tôi có có đến 2 loại, GET có 1 cái user và POST có user và username:

![image](https://github.com/user-attachments/assets/e2a4f4e9-7441-4ab7-9bf7-52505f8a1c5a)

Tiếp theo thì chạy `ffuf -w /home/namdt5125/ids.txt:FUZZ -u http://faculty.academy.htb:37126/courses/linux-security.php7?user=FUZZ > output.txt` và `ffuf -w ids.txt:FUZZ -u http://faculty.academy.htb:37126/courses/linux-security.php7 -X POST -d 'user=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' > output.txt` và `ffuf -w ids.txt:FUZZ -u http://faculty.academy.htb:37126/courses/linux-security.php7 -X POST -d 'username=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' > output.txt` để tìm:

![image](https://github.com/user-attachments/assets/41340b86-b162-4331-9dea-138ecd8f3b8c)

![image](https://github.com/user-attachments/assets/d1bec89e-5caa-4513-a348-e9c750f70c6d)

Sau khi check cả 3 file output.txt thì không có gì cả, nên tôi nghĩ có lẽ user sẽ đánh theo tên chứ không phải số:

![image](https://github.com/user-attachments/assets/e1cabc50-1a30-446a-bd78-36346a118e7a)

Tôi đổi sang file /mnt/d/wordlist/seclist_htb/seclists/Usernames/xato-net-10-million-usernames.txt để tìm user theo tên, thêm cái -fs 781 để tiện hơn trong ffuf:

![image](https://github.com/user-attachments/assets/d7b74e4d-0c74-4885-94c3-6a24c02ff387)

![image](https://github.com/user-attachments/assets/96f02a9f-cc64-449e-9c5b-3d150414e4ba)

