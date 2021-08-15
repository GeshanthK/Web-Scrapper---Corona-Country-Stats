import requests
import bs4
import pandas as pd

country = input("Enter what country's coronavirus statistics(ie. Canada): ").strip().replace(" ","-").lower()
result = requests.get("https://www.worldometers.info/coronavirus/country/" + country)
soup = bs4.BeautifulSoup(result.text, 'lxml')

cases = soup.find_all('div', class_ = 'maincounter-number')

data = []
for i in cases:
    span = i .find('span')
    data.append(span.string)

df = pd.DataFrame({'CoronaData_India': data})
df.index = ['TotalCases', 'Deaths', 'Recovered']

df.to_csv('Corona_Data.csv')