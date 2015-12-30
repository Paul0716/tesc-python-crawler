# -*- coding: utf-8 -*-
import csv
import urllib

from functions import *

# 從 stocknumber.csv 中讀出要爬的股票清單
stock_list = []
stock_list = get_stock_list('stocknumber.csv')

get_single_page('0050','2015','12')




