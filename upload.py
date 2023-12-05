import os
import time
import paramiko
#from download1 import var1
from info import USER, PASS, file
def uploadfile():
    print('start upload')
    host = '192.168.4.115'
    port = 22
    transport = paramiko.Transport((host, port))
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    transport.connect(username=USER, password=PASS)
    sftp = paramiko.SFTPClient.from_transport(transport)
    path = '/home/grandma/virtualbox/' + file[0]
    localpath = '/home/smith/goodies/' + file[0]
    sftp.put(localpath, path)
    sftp.close
    transport.close
    file.pop(0)
    print(file)
    print('close upload!')
def getintake():
    print('start intake')
    host = '192.168.4.115'
    port = 22
    transport = paramiko.Transport((host, port))
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    transport.connect(username=USER, password=PASS)
    sftp = paramiko.SFTPClient.from_transport(transport)
    path = '/home/grandma/virtualbox/intake.txt' 
    localpath = 'intake.txt'
    sftp.get(path, localpath)
    sftp.close
    transport.close
    print('close! intake')
