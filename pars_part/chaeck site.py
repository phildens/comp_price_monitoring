import urllib.request
import re
from bs4 import BeautifulSoup
request = urllib.request.urlopen('https://perm.gsm-opt.ru/zapchasti-dlya-apple/displei/?nalichie_n=0&sortirovka=sales&num_on_page=200&page=0&vid=0')
page = request.read()
bsobject = BeautifulSoup(page, 'html.parser')
get_displays = bsobject.findAll('div', {'class' : 'cat_list_el'})
for i in get_displays:
    priceobj = i.find('div', {'class' : 'table_rozn_price price_td_t active-price_warp'}).find('span', {'class' : 'active-price'}).text
    price_num = re.findall(r'\d+',str(priceobj))[0]
    print(price_num)
