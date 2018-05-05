# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

#example results page to test scraping 
results_page = 'https://www.kijiji.ca/b-oakville-halton-region/3ds/k0l1700277?dc=true'
page = urlopen(results_page)

#parse using beautiful soup
parsed_page = BeautifulSoup(page, 'html.parser')

kijiji_ads = parsed_page.find_all('div',{'class': 'regular-ad'})
# Take out the <div> of name and get its value

prices = []
ad_id = []
url_list = []
x = 0

for ad in kijiji_ads:
    price_box = ad.find('div',{'class': 'price'})
    ad_url = ad.find('a',{'class': 'title'})
    link = 'https://www.kijiji.ca' + ad_url['href']

    price = price_box.text.strip()
    if "Please Contact" in price:
      continue
    removed_currency = price[1:]

    if float(removed_currency) < 100:
         prices.append(removed_currency)
         url_list.append(link)

print(prices)
print(url_list)
