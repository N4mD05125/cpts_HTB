<h1>Nessus Skills Assessment</h1>

![image](https://github.com/user-attachments/assets/c300cd4f-dc1d-4b4d-bb8b-ca4666450159)

![image](https://github.com/user-attachments/assets/298be13e-c60a-4f67-901c-03763c5f2ada)

![image](https://github.com/user-attachments/assets/32e6f619-2c32-4353-8493-2846ac6f1017)

<br>

Mục đích của bài lab này là làm quen với Nessus, sau khi tải Nessus thì tôi bắt tay vào làm, chọn New Scan và chọn Basic Network Scan:

![image](https://github.com/user-attachments/assets/77bc0d46-c488-46bc-9884-4d6a889af89e)

Đặt tên và thêm target vào:

![image](https://github.com/user-attachments/assets/b44f4118-fbaa-47b4-b319-85cf81ca8d29)

Đối với `user "htb-student" and password "HTB_@cademy_student!"` thì vào phần Credentials để thêm vào, chọn Windows:

![image](https://github.com/user-attachments/assets/14f2c689-b76c-4eab-94c1-f1ba58c2d318)

Còn lại thì để mặc định, ấn save và bấm chạy, đợi 1 lúc lâu thì có kết quả như sau:

![image](https://github.com/user-attachments/assets/d2ca12e9-4de7-4e99-976d-ba0c93473924)

Tập trung vào lỗi có điểm cao, các lỗi khác thì tôi chưa đủ trình để khai thác:

![image](https://github.com/user-attachments/assets/2763ecfb-c395-487c-a49c-bcced4172799)

Xem miêu tả thì lỗi này ở các bản Tenable Nessus 10.1 trở xuống, hiện tại thì tôi chỉ có thể đọc cho vui chứ khó có thể hiểu toàn bộ cve này, tôi thử vào địa chỉ `https://10.129.202.116:8834/` được để ở dưới, theo lý thuyết thì tôi sẽ vào được Nessus của máy mục tiêu:

![image](https://github.com/user-attachments/assets/092c5487-e346-481e-9310-c6b3d1f76e05)

Chỉ cần nhập user và pass đã cho trước là vào được:

![image](https://github.com/user-attachments/assets/b4bfbd44-2100-4336-a8f1-452d6eec4e5f)

Và đây là giao diện khi vào được Nessus:

![image](https://github.com/user-attachments/assets/a1afc989-1cfb-49c7-be78-0c7621c5aa0a)

Bắt đầu với `Windows_basic_authed`:

![image](https://github.com/user-attachments/assets/8f8131b3-5298-4c37-93b9-ae692b17c795)

Tôi có thể trả lời được câu hỏi số 3 với ngay cái vuln đầu:

![image](https://github.com/user-attachments/assets/b33da76b-f452-4b71-a1cb-be0be9731b86)

Còn câu hỏi 1 thì search SMB và tìm thấy cái này, truy cập vào nó là có đáp án:

![image](https://github.com/user-attachments/assets/248f93ae-5de6-4cd2-a92b-06f4c77c43b1)

![image](https://github.com/user-attachments/assets/48dc8d34-fdcd-4812-88b0-4c7834df0ccf)

Trong tấm ảnh có cả địa chỉ target luôn lên xong câu 2, câu 4 thì bật filter tìm thông qua plugin ID 26925 là ra:

![image](https://github.com/user-attachments/assets/9a7f74e3-03bb-4f93-9c45-ac2e2cb54526)

![image](https://github.com/user-attachments/assets/79f770a0-e403-4bf5-8728-d42224a30385)

Và port của nó là 5900














