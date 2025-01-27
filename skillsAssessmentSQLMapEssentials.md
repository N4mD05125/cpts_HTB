<h1>Skills Assessment</h1>

![image](https://github.com/user-attachments/assets/5cc99861-56ec-4055-80b6-bbc2b6fac550)

![image](https://github.com/user-attachments/assets/89ef1407-a629-4862-9f2e-5baa9ae11c62)

Sau khi đi xem qua qua thì thấy đường dẫn nào cũng có giao diện như thế, kiểm tra các request thì không thấy có tham số gì cả:

![image](https://github.com/user-attachments/assets/aacdac4e-8b1a-4157-9dfd-7109df242405)

Tưởng có đường dẫn ẩn nào nên tôi treo ffuf, trong lúc rảnh thì để ý sao cái trang chả có hình gì mà cái tập tin nhìn to thế, mở ra mới phát hiện ra:

![image](https://github.com/user-attachments/assets/6eaffe6b-40db-4d97-a605-4181a180d809)

Thế quái nào chuyển sang trình duyệt không phải của burp thì lại hiện ra?

![image](https://github.com/user-attachments/assets/b05ad3a3-0eec-46b1-9db5-70001ab0b9c0)

Đọc phần src của nó còn nhiều thứ hơn:

![image](https://github.com/user-attachments/assets/3d89c260-6740-4a00-abff-40cc917b8ddc)

Tôi để ý là mỗi lần ấn "add to cart" là có 1 cái request POST được gửi đi chạy file action.php và json {"id" : 1}:

![image](https://github.com/user-attachments/assets/72203f2a-a161-45c2-b174-96c67f2464bc)

![image](https://github.com/user-attachments/assets/c9f26364-6780-4ce3-9b38-4d96f5f743a2)

Thử mang sang burp để gửi cái request:

![image](https://github.com/user-attachments/assets/8911ca66-fe43-46ce-98f6-291addd3f0b1)

Dùng lệnh `sqlmap -r req.txt -T final_flag --dump-all --batch --level=5 --risk=3 --no-cast --list-tampers` để chạy thì ra 1 lỗi:

![image](https://github.com/user-attachments/assets/88148466-2f96-4309-bd8a-f48cb641449e)

Thôi thì chơi theo kiểu time-based blind thôi:

![image](https://github.com/user-attachments/assets/f7378d16-c289-49cf-931e-f6ac598cf805)

HTB bảo sai flag mặc dù tôi có để htb hay HTB:

![image](https://github.com/user-attachments/assets/53c030cd-8c53-4745-a503-c928dda91f42)

![image](https://github.com/user-attachments/assets/6f18f1bf-7b3c-4da2-802d-c1f8b52dfc11)

Về sau bảo chatgpt check code thì chatgpt bảo dùng full các kí tự từ 32 đến 127 cho chắc cú:

![image](https://github.com/user-attachments/assets/e58213dd-cd77-4ff0-96c1-190d0797efb7)

![image](https://github.com/user-attachments/assets/62b2a5d8-9aa4-4456-b36f-4f21336d7757)

Flag có thêm ?! mới đau
