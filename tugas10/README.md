# Tugas 10
1. Jalankan async_server.py pada port 9002,9003,9004, dan 9005 dengan menjalankan file runserver.sh dengan command “bash runserver.sh”
<br>
<img width="512" alt="runserver" src="https://user-images.githubusercontent.com/36990542/81657453-15b34f00-9462-11ea-94f0-68a85350e5f0.png">

2. Jalankan file lb.py pada port 44444
<br>
<img width="960" alt="lb" src="https://user-images.githubusercontent.com/36990542/81657646-3b405880-9462-11ea-9c8a-7210de9eb2a6.png">

3. Akses halaman http://localhost:44444/page.html
<br>
<img width="960" alt="akses page" src="https://user-images.githubusercontent.com/36990542/81657721-4a270b00-9462-11ea-9ebf-45ae79ebe4b4.png">
<img width="960" alt="akses page 2" src="https://user-images.githubusercontent.com/36990542/81657757-53b07300-9462-11ea-82ba-f5c9a93e4894.png">

4. Lihat log program, bahwa setiap request akan dilayani oleh backend yang bergantian
<br>
<img width="960" alt="lb 2" src="https://user-images.githubusercontent.com/36990542/81657838-6a56ca00-9462-11ea-924b-cdcf498d7580.png">

5. Performance Test
Atur request sebesar 1000 request <br>
1.) server_async_http.py pada port 45000 <br>
1.1) Level concurrency 1
  <img width="960" alt="async level1" src="https://user-images.githubusercontent.com/36990542/81658342-df2a0400-9462-11ea-992f-6993c8fb93ea.png">
<br>
1.2) Level concurrency 5
  <img width="960" alt="async level5" src="https://user-images.githubusercontent.com/36990542/81658380-e9e49900-9462-11ea-98ad-c8ca988d085c.png">
<br>
1.3) Level concurrency 10
  <img width="960" alt="async level10" src="https://user-images.githubusercontent.com/36990542/81658456-fcf76900-9462-11ea-97f5-bc73e1341a84.png">
<br>
1.4) Level concurrency 15
  <img width="960" alt="async level15" src="https://user-images.githubusercontent.com/36990542/81658500-07b1fe00-9463-11ea-8470-a76de3356bc6.png">
<br>
1.5) Level concurrency 50
  <img width="960" alt="async level50" src="https://user-images.githubusercontent.com/36990542/81658540-10a2cf80-9463-11ea-88dd-c2bfa4df1406.png">
<br>
1.6) Level concurrency 100
  <img width="960" alt="async level100" src="https://user-images.githubusercontent.com/36990542/81658617-231d0900-9463-11ea-9bfb-e48bc45a37c6.png">
<br>
<br>
2.) server_thread_http.py pada port 46000 <br>
2.1) Level concurrency 1
  <img width="960" alt="thread level1" src="https://user-images.githubusercontent.com/36990542/81659055-8ad35400-9463-11ea-8921-82ab0cc9cab6.png">
<br>
2.2) Level concurrency 5
    <img width="960" alt="thread level5" src="https://user-images.githubusercontent.com/36990542/81659179-ab9ba980-9463-11ea-91e2-636819450fca.png">
<br>
2.3) Level concurrency 10
    <img width="960" alt="thread level10" src="https://user-images.githubusercontent.com/36990542/81659380-dbe34800-9463-11ea-962c-a46857d00797.png">
<br>
2.4) Level concurrency 15
    <img width="960" alt="thread level15" src="https://user-images.githubusercontent.com/36990542/81659485-f6b5bc80-9463-11ea-97c8-a51f7797663b.png">
<br>
2.5) Level concurrency 50
    <img width="960" alt="thread level50" src="https://user-images.githubusercontent.com/36990542/81659570-07663280-9464-11ea-8d7d-76440484fa7d.png">
<br>
2.6) Level concurrency 100
    <img width="960" alt="thread level100" src="https://user-images.githubusercontent.com/36990542/81659619-1351f480-9464-11ea-9d96-1dd8f9b52eee.png">
<br>
<br>
3.) lb.py pada port 44444<br>
3.1) Level concurrency 1<br>
    <img width="960" alt="lb level 1" src="https://user-images.githubusercontent.com/36990542/81659692-25339780-9464-11ea-962c-b03925e269f8.png">
<br>
3.2) Level concurrency 5
    <img width="960" alt="lb level 5" src="https://user-images.githubusercontent.com/36990542/81659738-311f5980-9464-11ea-95e0-340e8b98c0da.png">
<br>
3.3) Level concurrency 10
    <img width="960" alt="lb level 10" src="https://user-images.githubusercontent.com/36990542/81659785-3da3b200-9464-11ea-9af0-066e44016dcf.png">
<br>
3.4) Level concurrency 15
    <img width="960" alt="lb level 15" src="https://user-images.githubusercontent.com/36990542/81659827-48f6dd80-9464-11ea-98b3-80b757697b8d.png">
<br>
3.5) Level concurrency 50
    <img width="960" alt="lb level 50" src="https://user-images.githubusercontent.com/36990542/81659871-557b3600-9464-11ea-9763-65ccdc49673c.png">
<br>
3.6) Level concurrency 100
    <img width="960" alt="lb level 100" src="https://user-images.githubusercontent.com/36990542/81659927-61ff8e80-9464-11ea-9343-5f1144f0b4e7.png">
<br>

## Kesimpulan
Dari hasil performance test pada server async, server thread, dan dengan load balancer, dapat dilihat dari hasil yang tertera pada table-table diatas bahwa server dengan load balancer memiliki performa yang lebih baik dari pada server yang lainnya.
