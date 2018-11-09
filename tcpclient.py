from socket import *
from time import ctime
HOST='127.0.0.1'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)


while True:
  data=input(">")
  if not data:
   break
  tcpCliSock.sendall(data.encode('utf-8'))
  data=tcpCliSock.recv(BUFSIZ)
  if not data:
   break
  print(bytes(ctime(),'utf-8')," ",data.decode('utf-8'))
tcpCliSock.close()

