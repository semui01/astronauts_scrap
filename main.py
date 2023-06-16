# import library
import requests
from bs4 import BeautifulSoup
import lxml
import pandas as pd

# use requests to ask permission to fetch data from the website
url = 'https://www.faa.gov/space/human_spaceflight/recognition'
response = requests.get(url)
web_page = response.text

# make soup
# soup = BeautifulSoup(web_page, 'lxml')
soup=BeautifulSoup(web_page,'html.parser')
# print(soup)

table1 = soup.find('table')
# print(table1)

# Create headers for the dataframe
headers=[]
for i in table1.find_all('th'):
    title=i.text
    headers.append(title)

print(headers)


# Create a dataframe
mydata=pd.DataFrame(columns=headers)
for j in table1.find_all('tr')[1:]:
    row_data=j.find_all('td')
    row=[i.text for i in row_data]
    length=len(mydata)
    mydata.loc[length]=row

print(mydata)

# Export to csv
mydata.to_csv('astronauts.csv',index=False)
