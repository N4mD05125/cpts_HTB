<h1>Broken Authentication</h1>

![image](https://github.com/user-attachments/assets/5a45c6a2-f3c7-40d6-9125-5d0bbef59371)

Khi truy cập vào web thì có chỗ để login và đây là giao diện của phần login

![image](https://github.com/user-attachments/assets/6cf9c0c0-9127-49bb-b395-c35851247f63)

![image](https://github.com/user-attachments/assets/ae18d7f2-b49b-4e2e-9c80-66c8b891da7c)

Có vẻ phần đăng kí chỉ để đó thôi chứ không có chức năng:

![image](https://github.com/user-attachments/assets/26b145c9-8d7f-4fc1-bd6a-d0560cb2c2a9)

Tôi dùng `ffuf -u http://94.237.54.116:47533/FUZZ.php -w directory-list-2.3-small.txt` để fuzz

![image](https://github.com/user-attachments/assets/e6d49ba2-4668-4971-b239-2809c98215e2)

Sau khi ngồi mò parameter ở config, db, profile, mò pass với user là admin không thành công thì tôi thử mò user ở login, mong nó ra kết quả 
<br>` ffuf -u http://94.237.54.116:47533/login.php -w xato-net-10-million-usernames.txt -X POST -H "Content-Type: application/x-www-form-urlencoded" -b "PHPSESSID=2f3kdf5nn2et2mhkhao6g0esiv" -d "username=FUZZ&password=lmao" | grep -v "Size: 4353"`
<br>Và nó ra thật, user là gladys

![image](https://github.com/user-attachments/assets/3f69ac50-4121-445f-a801-f093706e8e03)

![image](https://github.com/user-attachments/assets/5177e0e2-87de-445d-a00f-6a347e334456)

Nó ghi là sai mật khẩu, tiếp tục brute mật khẩu

`ffuf -u http://94.237.54.116:47533/login.php -w custom_wordlist.txt -X POST -H "Content-Type: application/x-www-form-urlencoded" -b "PHPSESSID=2f3kdf5nn2et2mhkhao6g0esiv" -d "username=gladys&password=FUZZ" | grep -v "Size: 4344"`
<br>

![image](https://github.com/user-attachments/assets/0b1e3050-6f52-46c7-9568-121c19e687cf)

![image](https://github.com/user-attachments/assets/1762c1ac-095a-4733-bf38-63c8395f4cdd)

Ra mật khẩu là dWinaldasD13

![image](https://github.com/user-attachments/assets/401edc15-e601-4a25-8307-ae90d47efac2)

Sau khi đăng nhập thì đến xác thực 2FA OTP

![image](https://github.com/user-attachments/assets/e8cd23f9-a0e1-432d-874b-0eb3b61ef0c1)

Tôi nghĩ chắc là OTP có 4 số nên ném vào intruder(do bài trước OTP cũng 4 số)

![image](https://github.com/user-attachments/assets/9489b7ad-c0fa-48ee-ba21-f2d18aa15e3f)

Tôi để ý khi tôi nhập otp thì ở web thì nó có status code là 200, sau khi dùng intruder thì nó lại thành 302, sau 1 lúc tìm hiểu thì là tôi nếu nhập sai quá nhiều thì nó sẽ chuyển hướng đến login.php

![image](https://github.com/user-attachments/assets/e1521428-fc20-4c10-9875-45133c73bd8f)

Việc brute otp có vẻ không ổn, tôi thử dùng cách khác:

![image](https://github.com/user-attachments/assets/bb68372f-9986-4981-ba87-1484d256f1e5)

Khi tôi cố tình bỏ qua 2fa.php để truy cập vào profile.php thì nó bị chuyển hướng quay lại 2fa.php

![image](https://github.com/user-attachments/assets/149b6eb0-b6e6-40cb-93a0-7168d5552305)

Nhưng và vẫn kịp xem flag

![image](https://github.com/user-attachments/assets/0ca9c830-2e53-4ab8-9314-b332dbb236fa)

Thực ra dễ hơn thì tôi chỉ cần bật intercept lên và truy cập vào profile.php

![image](https://github.com/user-attachments/assets/a056db30-ab1f-4cfa-ac1e-300e1cc8f855)

![image](https://github.com/user-attachments/assets/48f66010-0352-4a23-8f7c-e56c2a678e2f)

Thấy cái 302 kia không, sửa thành 200 

![image](https://github.com/user-attachments/assets/6b9f83f2-438c-4068-a0fd-aca1754c6a1e)

![image](https://github.com/user-attachments/assets/5af9c603-4a55-4743-9af5-a315548a21bf)





