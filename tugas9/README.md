# Tugas 9
<br>
1. Jalankan file server_async_http.py dengan port 45000 , kemudian jalankan perintah apache benchmarking pada terminal untuk setiap level concurrency nya.
<br>
Atur jumlah request untuk semua level concurrency dengan 1000.<br>
1.1 Level concurrency 1 <br>
```
ab -n 1000 -c 1 http://127.0.0.1:45000/
```
