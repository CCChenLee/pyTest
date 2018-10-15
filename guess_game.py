#! /usr/bin/python3
#-*- coding:UTF-8 -*-


import random


number = random.randint(1,100)
guess = 0
while True:
	num_input = input("请输入一个1~100的数字...")
	guess += 1
	if not num_input.isdigit():
		print("请输入数字...")
	elif int(num_input)<0 or int(num_input)>=100:
		print("输入的数字不符合要求！")

	else:
		if number == int(num_input):
			print("您总共猜了 %d 次猜对" %guess)
			break
		elif number>int(num_input):
			print("您输入的数字偏小了~")
		elif number<int(num_input):
			print("您输入的数字偏大了~")
		else:
			print("Error!")