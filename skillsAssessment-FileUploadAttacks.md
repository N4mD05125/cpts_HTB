<h1>Skills Assessment - File Upload Attacks</h1>

![image](https://github.com/user-attachments/assets/2620c324-6466-4e07-ae00-21a24694b25d)

![image](https://github.com/user-attachments/assets/91421300-e1bd-46bf-83de-5ad5376c40d9)

Sau khi truy cập vào web, tôi chú ý đến phần contact us có chỗ để upload ảnh

![image](https://github.com/user-attachments/assets/74a5bd49-1717-4372-8a20-c4e3f7ae2a6b)

Tôi thay đổi nội dung của ảnh, để mỗi phần hex ở đầu là jpeg

![image](https://github.com/user-attachments/assets/d35d104c-f340-4811-ae80-2df3614b0154)

![image](https://github.com/user-attachments/assets/16af17d2-8c3e-4053-82d6-001a644b64e8)

Nội dung của tấm jpg đã được encode bằng base64, tôi code 1 đoạn python fuzz content type để xem những cái nào được dùng:

![image](https://github.com/user-attachments/assets/40462f47-c77c-4d0e-9501-5054bbe234d7)

Có 4 cái được thông qua, để ý cái svg+xml\, có thể sẽ có xxe trong đó

![image](https://github.com/user-attachments/assets/e3982f7b-e8c7-4978-93aa-5e014d77c5e5)

Và đây là code php sau khi decode từ chỗ base64 kia

![image](https://github.com/user-attachments/assets/aac1189c-f242-4466-b6bc-8d687d954a20)

![image](https://github.com/user-attachments/assets/0333e6e0-5333-48a5-801e-cdb94c8503a8)

Đại loại thì code sẽ lưu file ảnh ở user_feedback_submissions và đổi tên thành ymd_img.jpg (ví dụ 250205_test.jpg), ở dưới có 2 cái regex, regex thứ nhất là lọc các php, phtml, phps, không thấy lọc phar, bên dưới thì là lấy những file chỉ có tên là các kí tự từ a đến z và extension của nó là từ 2 đến 3 kí tự kẹp kí tự g ở cuối như svg, jpg, jpeg, png.

![image](https://github.com/user-attachments/assets/7bda0032-542d-44da-857a-997b15b23cd8)

Với đống tên có sẵn, tôi sẽ từ tìm tên










