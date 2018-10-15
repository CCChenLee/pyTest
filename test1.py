#!/usr/bin/env python3
#-*-coding:utf-8-*-

import asyncio
#用asyncio的异步网络连接来获取sina、sohu和163的网站首页
#@asyncio.coroutine、 await取代yield from
async def wget(host):
	print('wget %s...' % host)
	connect=asyncio.open_connection(host,80)
	reader,writer= await connect
	header='GET / HTTP/1.0\r\nHost:%s\r\n\r\n' % host
	writer.write(header.encode('utf-8'))
	await writer.drain()
	while True:
		line= await reader.readline()
		if line== b'\r\n':
			break
		print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
		writer.close()

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.baidu.com','www.mi.com','www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()