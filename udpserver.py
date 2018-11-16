from socket import *
from time import ctime
HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

udpServsock =socket(AF_INET,SOCK_DGRAM)
udpServsock.bind(ADDR)

while True:
  print("waiting for connection ")
  data,addr=udpServsock.recvfrom(BUFSIZ)
  udpServsock.sendto('[%s] %s'%bytes(ctime(),'utf-8'),addr)
  print("......recived from and returend ",addr)
udpServsock.close()
