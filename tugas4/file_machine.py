import json
import logging
import base64
from file import File

'''
------ PROTOCOL FORMAT ------

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

------ FITUR ------

a. Meletakkan File
   Untuk meletakkan/upload file ke folder 'memory'
   Request : upload
   Parameter : nama-file-upload *spasi* file-yang-diupload
   Response : jika berhasil -> Uploaded
              jika gagal -> Error

b. Mengambil File
   Untuk mengambil/download file dari dalam folder 'memory'
   Request : download
   Parameter: nama-file-yang-didownload
   Response: file yang terdownload akan muncul di direktori script berada

c. Melihat List File
   Untuk melihat list file yang berada dalam folder 'memory'
   Request : list
   Parameter : -
   Response: menampilkan nama-nama file dalam folder 'memory'

d. Jika command tidak dikenali akan merespon dengan ERROR COMMAND

'''

p = File()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama_asal = cstring[1].strip()
                nama_tujuan = cstring[2].strip()
                #print(nama_asal)
                #print(nama_tujuan.encode())
                p.upload_file(nama_asal,nama_tujuan.encode())
                return "Uploaded"

            elif (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                hasil = p.download_file(nama)
                return hasil[0]

            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_file()
                dict = {"status":"succes","data": hasil}
                return json.dumps(dict)

            else:
                return "ERROR COMMAND"

        except:
            return "ERROR"

if __name__=='__main__':
    machine = FileMachine()
    #run = machine.proses("upload up.txt up.txt")
    #run = machine.proses("download down.txt")
    run = machine.proses("list")
    print(run)