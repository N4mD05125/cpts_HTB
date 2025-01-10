<h1>Password Reuse Default Passwords</h1>

![image](https://github.com/user-attachments/assets/2771f14a-9252-4f56-bb4a-6aca7416b2c1)

![image](https://github.com/user-attachments/assets/c25f189a-cd00-4b4f-8864-df150af72324)

![image](https://github.com/user-attachments/assets/2caddb48-53d9-418b-a8cc-986cdfc1eedf)

Do là liên quan đến bài trước nên tôi vào ssh thông qua user:pass của bài trước là sam:B@tm@n2022! và trong đó có mysql:

![image](https://github.com/user-attachments/assets/ea6b267c-d99a-4103-bfc9-17f8da1583c8)

Tôi nghĩ search mysql trong metasploit chắc là không ra đâu vì bài đang bảo dùng default pass nên tôi search trên google thêm chữ github và ra cái này [here](https://github.com/gauravnarwani97/MySQL-default-credentials/blob/master/default_db_credentials1.txt):

![image](https://github.com/user-attachments/assets/733dc005-11e9-4952-9161-13298a6cc11e)

Dùng chay `mysql -u "username" -p` 1 lúc thì ra được user:pass default:

![image](https://github.com/user-attachments/assets/987ec469-fc65-4518-a686-fbeb0c991544)

![image](https://github.com/user-attachments/assets/43e80c08-bb8c-4dab-8c66-58e8147303d6)
