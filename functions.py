# -*- coding: utf-8 -*-
import csv 
import requests
from pyquery import PyQuery as pq
from lxml import etree


def get_stock_list(filename):
	stock_id_list = []
	f = open(filename, 'rb')
	for row in csv.reader(f, delimiter=','):
		stock_id_list.append(row[0])
	return stock_id_list

def get_single_page(stock_id, year, month):
	with open('data/%s.csv'%stock_id, 'a') as f:

		cw = csv.writer(f)
		page = requests.get('http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report'+year+month+'/'+year+month+'_F3_1_8_'+stock_id+'.php?STK_NO='+stock_id+'&myear='+year+'&mmon='+month)

		if page.status_code is 200:
			d = pq(page.text)
			row = d('tr.basic2')
			for key,value in enumerate(row):

				if key is not 0:
					data = d(value).text().split(' ')
					print key,d(value).text().replace(' ',',')
					cw.writerow(data)
			f.close();
		else:
			pass
# 錯誤輸出檔案

def record_error_log(msg):
	error_log = open('error.log', 'ab')










	



