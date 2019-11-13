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
#     Grabs all prices on page - change "limit" to set how many prices you grab.
    prices = soup.find_all(class_=('prods_price'), limit=5)

    try:
        #     This formats the prices to numbers in order to use them as values
        price_list = [int((price.text).replace('£', '').replace(',', ''))
                      for price in prices]
        print(f'{brand}: {model} - Price List: {(price_list)}')
# This gives us our average market value based on watchfinder

        def Average(lst):
            average = sum(lst) / len(lst)
            return int(average)
        print(f'Average Market Price: £{Average(price_list)}')
        print('')
#     This checks errors on oos or presale watches
    except:
        print(f'{brand}: {model} - Is not in stock/wrong model.')
        print('')


print('Watchfinder Collection Tracker by Matt Casey')
print(f'You currently have {len(watchList)} watches in your collection.')
print('')
watchTracker()
