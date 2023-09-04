from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

bright_star_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

#procurar o executavel do browser depois

page = requests.get(bright_star_url)
print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

 
for row in table_rows:
    table_cols = row.find_all('td')
    row = [i.text.restrip() for i in td]
    temp_list.append(row)
        

time.sleep(10)

scarped_data=[]

Star_name = []
Distance = []
Mass = []
Radius = []
Lum = []
for i in range(0,len(scarped_data)):

    Star_name = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]


headers = ['Star_name','Distance', 'Mass', 'Radius', 'Luminosity']

df2 = pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius,Lum)), columns = headers)
print(df2)
df2.to_csv('bright_strs.csv', index=True, index_label="id")

