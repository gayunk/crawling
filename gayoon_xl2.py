from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW
serv=Service()
serv.creation_flags = CREATE_NO_WINDOW   
driver = webdriver.Chrome(service = serv)


import time, datetime, os
import openpyxl

now=str(datetime.datetime.now())[:16]#
folderName= now.replace(":","_")#
os.mkdir(folderName)#


key_word=["대만민국 저출산"]#
wb=openpyxl.Workbook()#


for i in range(len(key_word)):
    ws = wb.create_sheet()
    ws.title=key_word[i]#
url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=" + key_word[i]
driver.get(url)
time.sleep(2)
