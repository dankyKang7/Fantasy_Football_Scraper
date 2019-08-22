#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:40:44 2019

@author: admin
"""

'''This python script will grab the weekly data and compute the weekly score by
player and defense based on the Sub-assembly Showdown Scoring System'''

#Import the required packages
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
import numpy as np



#Create the unique urls based on this pattern
#Url -> https://www.pro-football-reference.com/years/<year>/<week_#>.htm
#years from 2014 to 2018
#weeks from 1 - 16 (Week 17 is not part of fantasy)

years = ['2014','2015','2016','2017','2018']
weeks = ['week_1','week_2','week_3','week_4','week_5','week_6','week_7',
         'week_8','week_9','week_10','week_11','week_12','week_13','week_14',
         'week_15','week_16']

#Create the URLs to get the anchor data
url = [] 
for year in years:
    url_year = 'https://www.pro-football-reference.com/years/'+year+'/'
    for week in weeks:
        url_week = url_year + week + '.htm'
        url.append(url_week)

#Create skeleton for function to pull html data from that page
#make it a bs4 object for further parsing
        
html_1 = urlopen(url[0])
bsobj_1 =bs(html_1)


#find the a references

#Result_Links = bsobj_1.findAll('td', {"class":"right gamelink"})
Result_Links =bsobj_1.find_all('td', {"class":"right gamelink"})
box_scores =[]
for links in Result_Links:
    reference=links.find('a')['href']
    box_scores.append('https://www.pro-football-reference.com'+reference)
       
#new link https://www.pro-football-reference.com/boxscores/201509100nwe.htm
#open the box_scores link  

'''html_2 = urlopen(box_scores[0])
html_3 = req.get(box_scores[0])
html_4 = html_3.json()
soup_2 = bs(html_3,'htm')'''

#Create a client to get the 
class Client(QWebEnginePage):
    
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.html = self.toHtml(self.Callable)
        self.app.quit()
    
    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

page = Client(box_scores[0])
soup = bs(page.html,'html.parser')

        
#pull the table data out
tables = soup_2.findAll('div',{'id':'wrap_player_offense'})


