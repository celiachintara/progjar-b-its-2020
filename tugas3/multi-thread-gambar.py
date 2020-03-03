import logging
import requests
import os
import threading

def download_gambar(nomor):
    
    if (nomor is None):
        return False
    ff = requests.get(nomor)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(nomor)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


for i in range(3):
    url = {}
    url[0] = 'https://www.ecdc.europa.eu/profiles/custom/ecdc/themes/anthrax/images/logo-ecdc.png'
    url[1] = 'https://s.yimg.com/nq/nr/img/yahoo_mail_global_english_white_1x.png'
    url[2] = 'https://www.its.ac.id/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-12-at-16.02.13-1024x683.jpeg'
    #print(i)
    t = threading.Thread(target=download_gambar,args=(url[i],))

    t.start()

#kalau url di dalam main, berarti ada 3 proses thread berbeda yg jalan bareng.
#kalau url di dalam def function download gambar, berarti itu ada 1 proses yg jalanin 3 thread
