import pandas as pd
from cgitb import html
from ctypes.wintypes import tagMSG
import requests
from bs4 import BeautifulSoup

url="https://iitk.ac.in/new/iitk-faculty"
r=requests.get(url)
htmlContent=r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
tds = soup.body.find_all('p')

names=list()
emails=list()
phones=list()
departments=list()
research_int=list()
education=list()
for item in tds:
    emailid=item.find('a')
    if(emailid!=None):
        if(emailid.get('href')!='#'):
            i=0
            for child in item.children:
                if i==0:
                    if child.get_text():
                        names.append(child.get_text())
                    else:
                        names.append(" ")
                elif i==1:
                    if child.get_text():
                        emails.append(child.get_text())
                    else:
                        emails.append(" ")
                elif i==3:
                    if child.get_text():
                        education.append(child.get_text())
                    else:
                        education.append(" ")
                elif i==5:
                    if child.get_text():
                        phones.append(child.get_text())
                    else:
                        phones.append(" ")
                elif i==7:
                    if child.get_text():
                        research_int.append(child.get_text())
                    else:
                        research_int.append(" ")
                i=i+1
l= min(len(names), len(emails), len(phones), len(education), len(research_int))
names=names[0:l:]
emails=emails[0:l:]
phones=phones[0:l:]
education=education[0:l:]
research_int=research_int[0:l:]
data = {'Names': names, 'Email Id': emails, 'Contact': phones, 'Education': education, 'Research Interests': research_int};
df = pd.DataFrame(data) 
df.to_csv('output.csv')
# name, email, contact, education , Research
