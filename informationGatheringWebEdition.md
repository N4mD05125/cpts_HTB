<h1>Information Gathering - Web Edition Skills Assessment</h1>

![image](https://github.com/user-attachments/assets/fe784e0d-f57a-4cab-9768-c2d6048ea2a5)

<h2>Câu hỏi 1:</h2>

![image](https://github.com/user-attachments/assets/f51ac49d-5cc7-417f-87ae-7be897af2b1a)

Với câu hỏi đầu tiên thì dùng `whois inlanefreight.com` và ra 468:

![image](https://github.com/user-attachments/assets/b1fda356-a96c-4810-ae76-633cb18db8a2)

<h2>Câu hỏi 2:</h2>

![image](https://github.com/user-attachments/assets/f38d3a4a-8b84-4b12-9548-02c65d65308a)

Vì cái hosts và ip tách riêng nên không thể nào cứ thế sử dụng ip hoặc host được, nên tôi đã phải config file /etc/host:

![image](https://github.com/user-attachments/assets/b1ac9627-2a47-45ab-9763-b9f76f64823e)

Bước đầu thì thêm `83.136.252.118 inlanefreight.htb` vào, mấy cái dưới là do làm xong rồi, tương lai sẽ dùng đến. Sau khi config xong thì có thể dùng được, có rất nhiều cách để check ví dụ như `whatweb http://inlanefreight.htb:43674` hoặc có thể dùng `curl -I http://inlanefreight.htb:43674`

![image](https://github.com/user-attachments/assets/87ff2e3e-9fa3-438c-bcfc-fe80b8050817)

<h2>Câu hỏi 3:</h2>

![image](https://github.com/user-attachments/assets/6e9a9164-5d89-453b-8ce3-6e2cd49f81a3)

Sau khi chạy ffuf để dò các dir của inlanefreight.htb:43674 nhưng không có tiến triển, tôi bắt đầu sử dụng `ffuf -u http://FUZZ.inlanefreight.htb:43674 -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 200 | grep -v "Size: 120"`, thêm cái grep do size trả về toàn 120, mà 120 đấy thì thấy không vào được

![image](https://github.com/user-attachments/assets/71d87323-6c06-46e1-919a-b367ea89428f)

Tôi đã tìm được thêm subdomain `web1337.inlanefreight.htb:43674`, tiếp tục dò dir của nó:

![image](https://github.com/user-attachments/assets/a8ed4fcf-cfec-4e8d-9f12-fedfee988018)

Được 2 cái, tôi chả biết cái đầu là như nào nên skip(không biết nữa):

![image](https://github.com/user-attachments/assets/c61f59bc-cc93-4aa5-a537-ebd99bc2ee89)

Ngoài cái admin_h1dd3n ra thì còn lại không có giá trị lắm, đọc kĩ lại câu hỏi thì tôi nghĩ nên tìm tiếp trong admin_h1dd3n:

![image](https://github.com/user-attachments/assets/f5047eae-662d-4c4f-9338-f0013fcc1d51)

<h2>Câu hỏi 4+5:</h2>

![image](https://github.com/user-attachments/assets/3c6c047b-f52c-46db-bced-c750176513ba)

Sau khi ngồi tìm kiếm không tìm thấy được gì, đi lang thang trên forum thì thấy hint vẫn còn subdomain, vậy là tôi quay lại tìm tiếp subdomain bằng ffuf:

![image](https://github.com/user-attachments/assets/8a0a40ba-4217-4ada-b38f-ecebf226959f)

![image](https://github.com/user-attachments/assets/f38cf4d1-55b2-4582-99d5-43421752d5cb)

Mặc dù thêm được cái subdomain nhưng chưa dò ra dir, lại lần nữa, đang làm thì nó lại mất:

![image](https://github.com/user-attachments/assets/4cc9cba2-d910-4e14-b969-eda056606766)

Bấm reset thì đổi port mới là 43211:

![image](https://github.com/user-attachments/assets/80d6a784-7232-4181-9afe-abc475551ecf)

Vì câu hỏi liên quan đến tìm mail nên tôi có sử dụng 1 tool là [reconspider](https://github.com/bhavsec/reconspider), do trong máy bên HTB chưa cài, cài xong lại tải lắm thư viện các thứ nên dùng luôn trong máy thật của tôi `python3 ReconSpider.py http://dev.web1337.inlanefreight.htb:43211 ` và đây là kết quả:

![image](https://github.com/user-attachments/assets/e3edaf0c-5a59-4ee7-89d8-9be387363aa7)

![image](https://github.com/user-attachments/assets/e9e9124a-38ba-47b2-93a9-d1bd5fbf4231)

