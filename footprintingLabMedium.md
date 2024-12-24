<h1>Footprinting Lab - Medium</h1>

![image](https://github.com/user-attachments/assets/0ae46051-eaa0-42c7-b0d7-3b9d04dcea81)

Bắt đầu bằng cách `nmap -A 10.129.9.44` để kiểm tra các port đang mở

![image](https://github.com/user-attachments/assets/5204e9f0-df66-427b-b453-8e6a8ab15fba)


Tóm gọn lại tôi có các port sau:<br>
`PORT     STATE SERVICE`<br>
`111/tcp  open  rpcbind`<br>
`135/tcp  open  msrpc`<br>
`139/tcp  open  netbios-ssn`<br>
`445/tcp  open  microsoft-ds`<br>
`2049/tcp open  nfs`<br>
`3389/tcp open  ms-wbt-server`<br>
Tóm gọn tôi tìm thấy có các dịch vụ RPC, SMB, NFS, tôi sẽ thử bắt đầu bằng NFS với `showmount -e 10.129.9.44`

![image](https://github.com/user-attachments/assets/043629ff-2f1d-443b-9068-e450d02bc340)

Tôi tìm được `/TechSupport (everyone)`, kéo luôn folder này về máy `udo mount -t nfs 10.129.9.44:/TechSupport /mnt/techsupport`:

![image](https://github.com/user-attachments/assets/2ec1697f-b950-4cb3-81de-f2ebab374c3c)

![image](https://github.com/user-attachments/assets/73535a1d-8e8c-463a-b1c3-a178f5bfc4ec)

Tất cả file txt đều rỗng trừ `ticket4238791283782.txt` ra, mở thì tôi có được đoạn hội thoại giữa 2 nhân viên:

![image](https://github.com/user-attachments/assets/38ada15b-b000-4925-9ea9-6d1fb823b0db)

Tôi có được username `alex`, pass `lol123!mD`, mail `alex.g@web.dev.inlanefreight.htb` và 1 số thông tin khác,..
Đang làm bỗng dưng không kết nối được nên phải đổi ip:

![image](https://github.com/user-attachments/assets/5fee3cb9-f46a-4f3c-91d4-2e9fbe6408d9)

![image](https://github.com/user-attachments/assets/8f7b6b33-1505-47a5-9629-7a3918e6781f)

Dùng `crackmapexec smb 10.129.95.177 --shares -u 'alex' -p 'lol123!mD'` thì ra:

![image](https://github.com/user-attachments/assets/09e664da-af83-4f66-8324-c520c79608a1)

Alex không có quyền admin nhưng có `devshare`, `IPC$` và `Users`, tôi sẽ bắt đầu với `devshare` bằng `smbclient //10.129.95.177/devshare -U alex`

![image](https://github.com/user-attachments/assets/597c30c0-b23b-4c12-a8a5-ce4a84164fd3)

Mở file có `sa:87N1ns@slls83`, vậy là có thêm user:pass nữa, cuối cùng là đến RPC, dùng `xfreerdp /u:'alex' /p:'lol123!mD' /v:10.129.95.177` để remote:

![image](https://github.com/user-attachments/assets/7c44c2be-68f0-4128-be32-cfdada08f123)

Sau vài lần thử thì tôi nhận ra phải chạy SQL bằng admin, sử dụng `sa:87N1ns@slls83` để vào:

![image](https://github.com/user-attachments/assets/b2394c05-7eed-4508-83c2-36a57eaff37c)

![image](https://github.com/user-attachments/assets/fafd31d1-5097-4166-8890-9b41cb4bf80c)

![image](https://github.com/user-attachments/assets/87bc5d3e-c0c9-4d89-ba8a-48141497cfaf)

Và tôi đã tìm thấy user HTB!


