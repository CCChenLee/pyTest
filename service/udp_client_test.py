#! /usr/bin/python3
#-*- coding:UTF-8 -*-

import socket

def socket_udp_client():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	for data in ['张三','李四']:
		host=socket.gethostname()
		port=9999
		s.sendto(data.encode('utf-8'),(host,port))
		print(s.recv(1024).decode('utf-8'))
	s.close()

def main():
	socket_udp_client()

if __name__ == '__main__':
	main()