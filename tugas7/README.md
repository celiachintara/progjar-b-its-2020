# TUGAS 7. Performance Test

Jalankan file server_thread_http.py<br><br>
Menggunakan Ubuntu, Pertama jalankan command **" ab -n 10 -c 1,5,10 http://127.0.0.1:10001/ "**<br>
<img width="960" alt="nomor 1" src="https://user-images.githubusercontent.com/36990542/79086719-399e4a80-7d67-11ea-958b-8879630b0a60.png">
<br><br>
Kedua, jalankan command **" ab -n 50 -c 1,10,30,50 http://127.0.0.1:10001/ "**<br>
<img width="960" alt="nomor 2" src="https://user-images.githubusercontent.com/36990542/79086755-68b4bc00-7d67-11ea-9bb4-3cb778307a4f.png">
<br><br>
Ketiga, jalankan command **" ab -n 100 -c 1,10,50,100 http://127.0.0.1:10001/ "**<br>
<img width="960" alt="nomor 3" src="https://user-images.githubusercontent.com/36990542/79086806-9568d380-7d67-11ea-9e12-2da1f3f6dd74.png">
<br><br>
Tabulasi hasil yang didapatkan dari ketiga test di atas<br>
<img width="646" alt="tabulasi" src="https://user-images.githubusercontent.com/36990542/79086881-d9f46f00-7d67-11ea-853b-0bd1fb02c25d.png">
<br><br>
