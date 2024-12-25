<h1>Footprinting Lab - Hard</h1>

![image](https://github.com/user-attachments/assets/91a20a2f-8c3d-433c-989d-4fb82c0591f0)

Mở đầu tôi sử dụng `nmap -A 10.129.208.16` để check các port và version của nó:

![image](https://github.com/user-attachments/assets/3fea1798-07d6-4de3-b91e-b0d040f9407a)

Tóm tắt lại là:<br>
`PORT    STATE SERVICE`<br>
`22/tcp  open  ssh`<br>
`110/tcp open  pop3`<br>
`143/tcp open  imap`<br>
`993/tcp open  imaps`<br>
`995/tcp open  pop3s`<br>

Kiểm tra qua các port này thì không kiếm được gì nhiều, tôi đi tìm kiếm hint trên các forum thì thấy `nmap -A 10.129.208.16` là chưa đủ, tôi quét thêm cả UDP bằng `sudo nmap -sV -sC -F -T5 -sU 10.129.208.16`:

![image](https://github.com/user-attachments/assets/ca29a00a-804b-4fb9-84a7-6c2a1a3efe42)

Tôi thấy `SNMP` là đang mở nên sẽ đi khai thác thử bằng `onesixtyone -c /opt/useful/seclists/Discovery/SNMP/snmp.txt 10.129.208.16` thì có `backup`:

![image](https://github.com/user-attachments/assets/7cfafc58-d4fa-4b93-bcb7-26bd97df44da)

Tiếp tục sử dụng `snmpwalk -v2c -c backup 10.129.208.16`:

![image](https://github.com/user-attachments/assets/00680b08-b85d-48e7-9e22-6164d0e78964)

Nhưng ngoài những thông tin này tôi còn tìm thêm được user\:password:

![image](https://github.com/user-attachments/assets/1b305374-91ce-4e86-b5de-892edbc5932a)

Có được `tom NMds732Js2761` là đã thành công phần nào rồi, dùng `openssl s_client -connect 10.129.208.16:imaps` để vào imaps:

![image](https://github.com/user-attachments/assets/94e53487-8de0-4f1e-b0e1-a5a66e55f7bc)

Nhờ chatgpt nên tôi có thể dùng 1 số commands trong imaps, list ra thì thấy các thư mục, kiểm tra qua các thư mục thì có INBOX là có giá trị, còn lại rỗng:

![image](https://github.com/user-attachments/assets/20a5b725-f245-4692-93e9-5c7a4f640149)

Trong thư mục INBOX cho tôi key, tôi liền nhớ lại có cổng ssh đang mở, tôi dùng luôn key này để thử kết nối vào:

![image](https://github.com/user-attachments/assets/115787d2-2ba9-40b8-a951-8f26c39c1e48)

Không ngoài mong đợi, tôi đã kết nối được vào, tôi bắt đầu đi lục lọi:

![image](https://github.com/user-attachments/assets/1fb39a55-4dda-4fcd-8458-68cb0e691f92)

Sau khi không tìm kiếm được gì, tôi nhớ ra là đề bài yêu cầu tìm pass của user HTB, tôi nghĩ là liên quan gì đó đến sql, tôi thấy trong máy này có mysql, tôi liền vào mysql với user là tom:

![image](https://github.com/user-attachments/assets/7dfe81c9-4daf-4084-b6bd-a804075625b7)

![image](https://github.com/user-attachments/assets/57741bf3-90c4-4426-b529-0d8e8009c7e4)

Tìm kiếm trong bảng users là sẽ thấy username HTB và password ở số 150

