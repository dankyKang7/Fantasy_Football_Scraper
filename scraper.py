#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:34:41 2019

@author: admin
"""

'''This python script will pull in the table data of the past 5 seasons of 
fantasy football stats. 
Questions to answer?
What is the distribution of scoring by position? 
by offensive strategy?'''

#Import the required packages
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

#base url
years = ['2018','2017','2016','2015','2014']
url_list =[]
#Create the list of years you want..
for year in years:
    url = 'https://www.pro-football-reference.com/years/'+year+'/fantasy.htm'
    url_list.append(url)

#Get the html data of this page..
html_2018 = urlopen(url_list[0])
bsobj_2018 = bs(html_2018.read())
bsobj_str = str(bsobj_2018)

#Let's find the table and the get the data
table_data_2018 = str(bsobj_2018.table)
table_data = pd.read_html(table_data_2018)

#Get teh reciever data
table_data.columns
