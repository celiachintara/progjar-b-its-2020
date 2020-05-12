# Tugas 9
<br>
1. Jalankan file server_async_http.py dengan port 45000 , kemudian jalankan perintah apache benchmarking pada terminal untuk setiap level concurrency nya.
<br>
Atur jumlah request untuk semua level concurrency dengan 1000.<br>
1.1 Level concurrency 1 <br>
ab -n 1000 -c 1 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level1" src="https://user-images.githubusercontent.com/36990542/81634930-2780fc00-943a-11ea-9fc3-856166dabf57.png">

1.2 Level concurrency 5 <br>
ab -n 1000 -c 5 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level5" src="https://user-images.githubusercontent.com/36990542/81635037-5dbe7b80-943a-11ea-8724-1e01e459c142.png">

1.3 Level concurrency 10 <br>
ab -n 1000 -c 10 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level10" src="https://user-images.githubusercontent.com/36990542/81635090-88103900-943a-11ea-8135-767303a23434.png">

1.4 Level concurrency 15 <br>
ab -n 1000 -c 15 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level15" src="https://user-images.githubusercontent.com/36990542/81635121-9e1df980-943a-11ea-94ad-a25a61a3e335.png">

1.5 Level concurrency 50 <br>
ab -n 1000 -c 50 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level50" src="https://user-images.githubusercontent.com/36990542/81635161-b7bf4100-943a-11ea-868f-0a9ef399108d.png">

1.6 Level concurrency 100 <br>
ab -n 1000 -c 100 http://127.0.0.1:45000/
<br>
<img width="960" alt="async level100" src="https://user-images.githubusercontent.com/36990542/81635182-c279d600-943a-11ea-8a1d-1c24d2de0cb0.png">
<br><br>

2. Jalankan file server_thread_http.py dengan port 46000 , kemudian jalankan perintah apache benchmarking pada terminal untuk setiap level concurrency nya.
<br>
Atur jumlah request untuk semua level concurrency dengan 1000.<br>
2.1 Level concurrency 1 <br>
ab -n 1000 -c 1 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level1" src="https://user-images.githubusercontent.com/36990542/81635287-18e71480-943b-11ea-9211-991518179d84.png">

2.2 Level concurrency 5 <br>
ab -n 1000 -c 5 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level5" src="https://user-images.githubusercontent.com/36990542/81635327-30260200-943b-11ea-8414-81c9d91aaaef.png">

2.3 Level concurrency 10 <br>
ab -n 1000 -c 10 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level10" src="https://user-images.githubusercontent.com/36990542/81635382-521f8480-943b-11ea-8162-671db9e09a0e.png">

2.4 Level concurrency 15 <br>
ab -n 1000 -c 15 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level15" src="https://user-images.githubusercontent.com/36990542/81635417-69f70880-943b-11ea-9231-491b2bd652be.png">

2.5 Level concurrency 50 <br>
ab -n 1000 -c 50 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level50" src="https://user-images.githubusercontent.com/36990542/81635456-75e2ca80-943b-11ea-9546-a835c3b0470e.png">

2.6 Level concurrency 100 <br>
ab -n 1000 -c 100 http://127.0.0.1:46000/
<br>
<img width="960" alt="thread level100" src="https://user-images.githubusercontent.com/36990542/81635473-81ce8c80-943b-11ea-93f7-e1fcf25cafe4.png">
<br>
## **Kesimpulan**
Dari hasil performance test pada server async dan server thread, dapat dilihat dari hasil yang tertera di kedua table diatas bahwa server async memiliki performa yang lebih baik dari pada server thread sehingga server async dapat bekerja lebih cepat dibandingkan server thread.
