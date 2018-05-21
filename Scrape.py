# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#example results page to test scraping 
results_page = 'https://www.kijiji.ca/b-oakville-halton-region/3ds/k0l1700277?dc=true'

#parse using beautiful soup
def scrape(results):
    page = urlopen(results)
    parsed_page = BeautifulSoup(page, 'html.parser')

    kijiji_ads = parsed_page.find_all('div',{'class': 'regular-ad'})

    prices = []
    ad_id = []
    url_list = []

    for ad in kijiji_ads:
    
        price_box = ad.find('div',{'class': 'price'})
        ad_url = ad.find('a',{'class': 'title'})
        link = 'https://www.kijiji.ca' + ad_url['href']
        price = price_box.text.strip()

        if "Please Contact" in price:
            continue

        removed_currency = price[1:]
        prices.append(removed_currency)
        url_list.append(link)

    print(prices)
    print(url_list)

scrape(results_page)

