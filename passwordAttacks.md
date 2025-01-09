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

![image](https://github.com/user-attachments/assets/e37b4403-0b97-4095-97b8-0019950f4561)

Chạy `hydra -L username.list -P password.list rdp://10.129.167.69` để vét cạn dịch vụ rdp:

![image](https://github.com/user-attachments/assets/a114d8b8-39a9-4f76-830e-c2d386483e6e)

Do lâu quá nên tôi tiện thể làm luôn smb `hydra -L user.list -P password.list smb://10.129.167.69`:

![image](https://github.com/user-attachments/assets/30442210-f5b2-4653-91fa-60f50fb122bb)

Cơ mà nó bị invalid và tra google thì ra như này [here](https://bugs.kali.org/view.php?id=6709):

![image](https://github.com/user-attachments/assets/ec4ebe92-1c3a-452a-9e1d-a5a5824d4b27)

Vậy nên tôi sử dụng msfconsole

![image](https://github.com/user-attachments/assets/522162d8-0f80-4aa1-8a1a-622123d2d8c3)

![image](https://github.com/user-attachments/assets/8bf8b30b-ca0e-4c16-b74a-2303c4883de3)

Có đến hẳn 2 cái luôn cassie:12345678910 và chris:789456123, thử với cassie:12345678910 thì ra flag:

![image](https://github.com/user-attachments/assets/ea6f50d0-7a32-4e1e-94ee-873caab957b9)

Với chris:789456123 thì vẫn như cái kia:

![image](https://github.com/user-attachments/assets/babb705d-4c63-4f46-9eb4-2b374083f66c)

Trong lúc đợi rdp thì tôi thử chris:789456123 vào rdp bằng `xfreerdp /u:'chris' /p:'789456123' /v:10.129.167.69` và ngạc nhiên chưa, nó hoạt động:

![image](https://github.com/user-attachments/assets/01670950-2b50-4f40-b864-4cd138de5e0e)

Không biết tại sao nhưng mà cái hydra nó không dính, hmm chắc kệ thôi:

![image](https://github.com/user-attachments/assets/2e0a6f6a-2037-47fa-8b62-ba0df1e42007)

