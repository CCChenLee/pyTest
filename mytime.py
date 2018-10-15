#!/usr/bin/python
#-*-coding:UTF-8-*-


import datetime,time
from datetime import datetime

now = datetime.now()

year = strftime("%Y",localtime())
month = strftime("%m",localtime())
day = strftime("%d",localtime())
hour = strftime("%H",localtime())
min = strftime("%M",localtime())
sec = strftime("%S",localtime())

def today():
	''''
	get today,date.format="YYYY-MM-DD"
	'''
	return date.today()

def todaystr():
	'''
	get date string,date format="YYYYMMDD"
	'''
	return year+month+day

def datetime():
	''''
	get datetime,format="YYYY-MM-DD HH:MM:SS"
	'''
	return strftime("%Y-%m-%d %H:%M:%S",localtime())

def datetimestr():
	''''
	get datetime string
	date format="YYYYMDDHHMMSS"
	'''
	return year+month+hour+min+sec

def get_day_of_day(n=0):
	''''
	if n>=0,date is larger than today
	if n<0,date is less than today
	date format="YYYY-MM-DD"
	'''
	if n<0:
		n=abs(n)
		return date.today()-timedelta(days=n)
	else:
		return date.today()+timedelta(days=n)

def get_days_of_month(year,mon):
	''''
	get days of month
	'''
	return calendar.monthrange(year,month)[1]

def get_firstday_of_month(year,month):
	''''
	get the first day of month
	date format="YYYY-MM-DD"
	'''
	days="01"
	if int(month)<10:
		month="0"+str(int(month))
	arr=(year,month,days)
	return "-".join("%s" %i for i in arr)

def get_lastday_of_month(year,month):
	''''
	get the last day of month
	date format="YYYY-MM-DD"
	'''
	days=calendar.monthrange(year,month)[1]
	month=addzero(month)
	arr=(year,month,days)
	return "-".join("%s" %i for i in arr)

def get_first_month(n=0):
	''''
	get the first day of month from today
	n is how many months
	'''
	(y,m,d)=getyearandmonth(n)
	d="01"
	arr=(y,m,d)
	return "-".join("%s" %i for i in arr)

def get_lastday_month(n=0):
	''''
	get the last day of month from day
	n is how many months
	'''
	return "-".join("%s" %i for i in getyearandmonth(n))

def getyearandmonth(n=0):
	''''get the year,month,days from today
	before or after n months
	'''
	thisyear=int(year)
	thismonth=int(month)
	totalmonth=thismonth+n
	if n>=0:
		if totalmonth<=12:
			days=str(get_days_of_month(thisyear,totalmonth))
			totalmonth=addzero(totalmonth)
			return year,totalmonth,days
		else:
			i=totalmonth//12
			j=totalmonth%12
			if j==0:
				i-=1
				j=12
			thisyear+=i
			days=str(get_days_of_month(thisyear,j))
			j=addzero(j)
			return str(thisyear),str(j),days
	else:
		if totalmonth>0 and totalmonth<12:
			days=str(get_days_of_month(thisyear,totalmonth))
			totalmonth=addzero(totalmonth)
			return year,totalmonth,days
		else:
			i=totalmonth//12
			j=totalmonth%12
			if(j==0):
				i-=1
				j=12
			thisyear+=i
			days=str(get_days_of_month(thisyear,j))
			j=addzero(j)
			return str(thisyear),str(j),days

def addzero(n):
	''''
	add 0 before 0-9
	return 01-09
	'''
	nabs=abs(int(n))
	if nabs<10:
		return "0"+str(nabs)
	else:
		return nabs

def get_today_month(n=0):
	''''获取当前日期前后N月的日期
	if n>0，获取当前日期前N月的日期
	if n<0，获取当前日期后N月的日期
	date format="YYYY-MM-DD"
	'''
	(y,m,d)=getyearandmonth(n)
	arr=(y,m,d)
	if int(day)<int(d):
		arr=(y,m,day)
	return "-".join("%s" %i for i in arr)

def get_firstday_month():
	(y,m,d)=getyearandmonth(n)
	arr=(y,m,'01')
	return "-".join("%s" %i for i in arr)

def main():
	print('today is:',today())
	print('today is:',todaystr())
	print('the date time is:',datetime())
	print('data time is:',datetimestr())
	print('2 days after today is:',get_day_of_day(2))
	print('2 days before today is:',get_day_of_day(-2))
	print('2 months after today is:',get_today_month(2))
	print('2 months before today is:',get_today_month(-2))
	print('2 months after this month is:',get_firstday_month(2))
	print('2 months before this month is:',get_first_month(-2))

if __name__ == '__main__':
	main()