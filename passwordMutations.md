<h1>Password Mutations</h1>

![image](https://github.com/user-attachments/assets/a47b0add-bb3b-4a7b-a9e6-6e11212fda47)

![image](https://github.com/user-attachments/assets/08d04bcc-7e46-4080-a492-2bb27e92383e)

Theo lý thuyết thì ta chạy ssh bằng `hydra -L username.list -P mut_password.list ssh://10.129.57.51` nhưng mà sau khoảng 2 tiếng đồng hồ đợi, tôi đã kiếm hint trên forum thì họ có hint là tấn công dịch vụ khắc nhanh hơn ssh nhiều, sau đó tôi chạy `hydra -L username.list -P password.list ftp://10.129.57.51` và nó thực sự nhanh hơn khi tiêu tốn đến hơn 1 tiếng với sam:B@tm@n2022!
<br>
Do lỡ tay tắt terminal nên không có chụp lại kết quả nhưng mà đây là sau khi ssh vào:

![image](https://github.com/user-attachments/assets/a094846d-a1b2-4ba5-b456-d11958a484d7)
