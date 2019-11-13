import requests
from bs4 import BeautifulSoup
# Input your watches here, model number is the most accurate
# Input like this ['watch1','watch2','watch3','etc']
watchList = ['114060', '31130423001006', '114200']


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}


def watchTracker():
    # Loops through watchList to create URLs for each and pass them into getInfo
    for i in watchList:
        URL = f'https://www.watchfinder.co.uk/search?q={i}&orderby=AgeNewToOld'
        getInfo(URL)

# This grabs and parses the info that gets printed


def getInfo(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    brand = soup.find(class_=('prods_brand')).get_text()
    model = soup.find(class_=('prods_series')).get_text()
    price = soup.find_all(class_=('prods_price'), limit=5)
    # Loops through all the products and formats pricing
    for price in price:
        price = price.text
        price = " ".join(price.split())
        print(f"{brand}: {model} - {price}")


print('Watchfinder Collection Tracker by Matt Casey')
print('Currently Searching for Models:')
print(watchList)
print('')
watchTracker()
