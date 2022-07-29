import pandas as pd
import requests
from bs4 import BeautifulSoup

url="https://iitk.ac.in/new/iitk-faculty"
r=requests.get(url)
htmlContent=r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
data = soup.body.find_all('p')
# print(data)
names=list()
emails=list()
phones=list()
research_int=list()
education=list()
for item in data:
    # print(item)
    emailid=item.find('a')
    # print(emailid)
    if(emailid!=None):
        if(emailid.get('href')!='#'):
            i=0
            for it in item.children:
                # print(child)
                if i==0:
                    if it.get_text():
                        names.append(it.get_text())
                    else:
                        names.append(" ")
                elif i==1:
                    if it.get_text():
                        emails.append(it.get_text())
                    else:
                        emails.append(" ")
                elif i==3:
                    if it.get_text():
                        education.append(it.get_text())
                    else:
                        education.append(" ")
                elif i==5:
                    if it.get_text():
                        phones.append(it.get_text())
                    else:
                        phones.append(" ")
                elif i==7:
                    if it.get_text():
                        research_int.append(it.get_text())
                    else:
                        research_int.append(" ")
                i=i+1
l = min(len(names), len(emails), len(phones), len(education), len(research_int))
names=names[0:l:]
emails=emails[0:l:]
phones=phones[0:l:]
education=education[0:l:]
research_int=research_int[0:l:]
datafinal = {'Names': names, 'Email Id': emails, 'Contact': phones, 'Education': education, 'Research Interests': research_int};
df = pd.DataFrame(datafinal) 
df.to_csv('output.csv',index=False)