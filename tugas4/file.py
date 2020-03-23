import shelve
import uuid
import socket
import os
import base64

class File:
    def __init__(self):
        #buat folder
        if not os.path.exists('memory'):
            os.makedirs('memory')

    def upload_file(self,nama=None,file=None):
       # check file name
        data_file = file
        print(base64.decodestring(data_file))
        f = open("memory/"+nama,"wb")
        f.write(base64.decodestring(data_file))
        return True

    def download_file(self,nama=None):
        temp = []
        f = open("memory/" + nama,"rb")
        baca = f.read()
        f.close()
        #print(baca)

        hasil = base64.encodestring(baca)
        temp.append(hasil.decode())
        return temp

    def list_file(self):
        file_list = os.listdir("memory")
        temp = []
        for filename in file_list:
            temp.append(filename)
        return temp

if __name__=='__main__':
    files = File()
    print(files.list_file())
