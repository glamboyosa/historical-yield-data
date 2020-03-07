import pandas
from pandas import Series, DataFrame
import numpy as np
import requests
from bs4 import BeautifulSoup
URLS = [
    'http://www.factfish.com/statistic-country/nigeria/maize%2C%20total%2C%20%20production%20quantity'
]
dictionary = ''
year_name = []
year = []
value_name = []
value = []
results_3 = None
for url in URLS:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('th')
    results_3 = soup.find_all(
        'table', class_='table table-striped table-bordered factfish-drill-down-data-table')[0].text.split()[slice(2, 115)]
    # print(results_3)
    year_name.append(results[0].text)
    value_name.append(results[1].text)

    # if resultest == None:
    #     print('Okay this is how we will do itt')
    # print(year_name)
    # print(value_name)
# print(results_3)
year = results_3[slice(0, 115, 2)][slice(1, 57)]
print(year_name)
print(len(year))
value = results_3[slice(1, 115, 2)]
print(value_name)
print(len(value))
dictionary = {
    year_name[0]: year,
    value_name[0]: value
}
print(dictionary)
df = DataFrame(dictionary)
df.to_csv(r'C:\Users\Osa\Documents\Crop Yield\maize-yield.csv',
          index=None, header=True)
print(dictionary)
print(DataFrame(dictionary))
print(pandas.read_csv(r'C:\Users\Osa\Documents\Crop Yield\maize-yield.csv'))
