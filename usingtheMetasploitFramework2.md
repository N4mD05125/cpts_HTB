<h1>Using the Metasploit Framework: Meterpreter</h1>

![image](https://github.com/user-attachments/assets/fc420731-7d38-4832-8929-c2569d8d3edf)

![image](https://github.com/user-attachments/assets/20784fc9-2e37-42d9-a8df-9121f19cdd22)

![image](https://github.com/user-attachments/assets/929dfbd9-c24b-4b63-a73f-4dea5494ae7c)

Sau khi nmap thì thấy port 5000 có service http, dùng firefox để vào:

![image](https://github.com/user-attachments/assets/980f70f3-3139-481e-bf63-8bd77361127d)

Dùng admin:admin thì vào được:

![image](https://github.com/user-attachments/assets/7cfe0688-4368-4ea7-884c-41b7fb3121e9)

Xem trong đây không có gì để khai thác lắm, quay lại msfconsole để search lỗ hổng:

![image](https://github.com/user-attachments/assets/d97e3d85-22c2-4128-bab8-cb493465a13f)

Điền LHOST và RHOSTS và chạy:

![image](https://github.com/user-attachments/assets/264a303c-9f6d-46b3-88df-eaaefdc0c353)

Đáp án: nt authority\system, câu tiếp theo:

![image](https://github.com/user-attachments/assets/74d3bd2b-83ab-45f5-b61f-4d02537f1834)

Tôi không thể chạy được hashdump, yêu cầu bị từ chối, sau khi đi đọc hint trên forum 1 chút thì dùng ps để xem các tiến trình đang chạy:

![image](https://github.com/user-attachments/assets/e5a2285f-6876-4da4-98e0-c23a6da32d82)

![image](https://github.com/user-attachments/assets/0bac0665-aa8c-4795-87b9-94807099c5a0)

![image](https://github.com/user-attachments/assets/45347a0c-23fb-4329-93ac-2c0af73e8129)

Chúng ta để ý fortiloggerservice.exe và migrate sang nó (vì tôi cần sang cái tiến trình có nhiều quyền hơn), sau đó có thể chạy được hashdump
