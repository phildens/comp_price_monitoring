import urllib.request
import re
from bs4 import BeautifulSoup

stoper = 'table_body report new_report sticky-th flex-list-tovar descr list list1 hid_tov_tab table_catalog'
models = ['X', '8', '7', '6', '6S', '11', '5S', 'XR', 'XS', '12', '13', '14']
diferences = ['Pro', 'Plus', 'Pro Max', 'mini', 'Max', 'Mini']
def get_prices_from_site():
    j = 0
    price_list = []
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
            availability_point = i.find('div', {'class': 'catalog_qty_block'}).text.split()
            if not (availability_point == ['в', 'наличии']):
                continue
            priceobj = i.find('div', {'class': 'table_rozn_price price_td_t active-price_warp'}).find('span', {
                'class': 'active-price'}).text

            namemodel = i.find('div', {'class' : 'catalog_list_left_block'}).text
            if len(namemodel) == 0:
                continue
            price_num = re.findall(r'\d+', str(priceobj))[0]
            phonemodel = re.search(r'iPhone ', namemodel)
            if phonemodel is None:
                continue
            phonemodel = phonemodel.group()

            for model in models:
                if model in namemodel:
                    for diferen in diferences:
                        if diferen in namemodel:
                            price_list.append([phonemodel + model + ' ' + diferen, int(price_num)])
                            continue

                    price_list.append([phonemodel + model, int(price_num)])

        j += 1
    print(price_list)
    return price_list
