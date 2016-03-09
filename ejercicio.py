#!/usr/bin/python
# -*- coding: utf-8 -*-
#Lucia Villa Martinez


import socket
import random
import time

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)
try:
	
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'HTTP request received:' 
		peticion = recvSocket.recv(1301)
		print 'Answering back.. '	
		aleatorio = random.randint(0,1000000)
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n")
		recvSocket.send('<html><head><meta http-equiv="Refresh" content="5;url='+str(aleatorio)+'"></head>')
		recvSocket.send("<body><h1> Ha ocurrido un error y va a ser redirigido a la siguiente URL ")
		recvSocket.send("http://localhost:1234/")
		recvSocket.send(str(aleatorio))
		recvSocket.send("</h1></body></html>")
		recvSocket.send("\r\n")
		recvSocket.close()
		
		

except KeyboardInterrupt:
	print "Closing binded socket"
	mySocket.close()
