#! /usr/bin/env python3
#-*- coding:utf-8 -*-
def test():
	temp = [lambda x: i*x for i in range(4)]
	return temp

for every in test():
	print(every(2))