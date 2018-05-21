import requests
KIJIJI_URL = 'https://www.kijiji.ca'
KIJIJI_SEARCH_URL = KIJIJI_URL + '/b-search.html'

search_criteria = {'categoryId': '0', 'locationId': '1700212', 'keywords' : '3ds', 'minPrice' :'', 'maxPrice': ''}

def searchResults(search_Param):
    specific_search = '?'
    for key, value in search_Param.items():
        if not value == '':
            specific_search += (key +'=' + value +'&') 
    specific_search[:-1]

    r = requests.get(KIJIJI_SEARCH_URL+specific_search)
    print(r)


#def searchResults(categoryId, locationId, keywords, minPrice, maxPrice):
  #  r = requests.get(KIJIJI_SEARCH_URL+"?categoryId="+categoryId+"&locationId="+locationId+"&keywords="+keywords+"&minPrice="+minPrice+"&maxPrice="+maxPrice)
   # print(r)

#r= requests.get('https://www.kijiji.ca/b-search.html?formSubmit=true&adIdRemoved=&adPriceType=&brand=&carproofOnly=false&categoryId=0&categoryName=Nintendo+DS&cpoOnly=false&dc=true&gpTopAd=false&highlightOnly=false&ll=&locationId=1700212&minPrice=&maxPrice=&origin=&pageNumber=1&searchView=LIST&sortByName=dateDesc&userId=&urgentOnly=false&keywords=3ds&SearchCategory=0&SearchLocationPicker=Kitchener+/+Waterloo&SearchSubmit=')
#r= requests.get('https://www.kijiji.ca/b-search.html?categoryId=0&categoryName=Nintendo+DS&locationId=1700212&minPrice=&maxPrice=&pageNumber=1&keywords=3ds')
searchResults(search_criteria)

#r= requests.get('https://www.kijiji.ca/b-oakville-halton-region')
