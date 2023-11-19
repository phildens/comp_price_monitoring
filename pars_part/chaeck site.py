import urllib.request
import re
from bs4 import BeautifulSoup

stoper = 'table_body report new_report sticky-th flex-list-tovar descr list list1 hid_tov_tab table_catalog'
'''request = urllib.request.urlopen(f'https://perm.gsm-opt.ru/zapchasti-dlya-apple/displei/?nalichie_n=0&sortirovka=sales&num_on_page=50&page=5&vid=0')
page = request.read()
bsobject = BeautifulSoup(page, 'html.parser')
getcontrol = bsobject.find('div', {'class' : stoper}).find('p').text
print(getcontrol == 'Ничего не найдено')'''
j = 0
while j < 50:
    request = urllib.request.urlopen(
        f'https://perm.gsm-opt.ru/zapchasti-dlya-apple/displei/?nalichie_n=0&sortirovka=sales&num_on_page=50&page={j}&vid=0')
    page = request.read()
    bsobject = BeautifulSoup(page, 'html.parser')
    getcontrol = bsobject.find('div', {'class': stoper}).find('p').text

    if getcontrol == 'Ничего не найдено':
        break
    get_displays = bsobject.findAll('div', {'class': 'cat_list_el'})
    for i in get_displays:
        priceobj = i.find('div', {'class': 'table_rozn_price price_td_t active-price_warp'}).find('span', {
            'class': 'active-price'}).text
        
        price_num = re.findall(r'\d+', str(priceobj))[0]
        print(price_num)
    j += 1
