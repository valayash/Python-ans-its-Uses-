from fileinput import filename
from bs4 import BeautifulSoup
import requests
import csv

html_test= requests.get('https://iitk.ac.in/new/iitk-faculty').text

soup = BeautifulSoup(html_test, 'lxml')

prof=soup.find_all('p')
a=[]
with open('yoyo.csv', 'w', newline='',encoding="utf-8") as file:
    writer = csv.writer(file)
    for pro in prof: 
     print(pro.text)
     writer.writerow(pro.text)
