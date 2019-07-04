#!/usr/bin/python3

import socket
import sys
import time

time.sleep(10)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ('192.168.8.166', 1337)
print('Startin up on %s : %s' % server_addr)
sock.bind(server_addr)
while True:
	print('waiting to receive message')
	data, addr = sock.recvfrom(4096)
	print('received %s bytes from %s' % (len(data), addr))
	print(data)
	if data:
		sent = sock.sendto(data, addr)
		print('sent %s bytes back to %s' % (sent, addr))
