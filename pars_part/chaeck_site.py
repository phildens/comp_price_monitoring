import urllib.request
import re
from bs4 import BeautifulSoup

stoper = 'table_body report new_report sticky-th flex-list-tovar descr list list1 hid_tov_tab table_catalog'
models = ['X', '8', '7', '6', '6S', '11', '5S', 'XR', 'XS', '12', '13', '14']
diferences = ['Pro', 'Plus', 'Pro Max', 'mini', 'Max', 'Mini']


class site_checker:
    price_list = []
    unique_list = []

    def __init__(self):
        self.get_prices_from_site()
        self.get_unique_models()

    def get_prices_from_site(self):
        j = 0
        self.price_list.clear()
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

                namemodel = i.find('div', {'class': 'catalog_list_left_block'}).text
                if len(namemodel) == 0:
                    continue
                price_num = re.findall(r'\d+', str(priceobj))[0]
                phonemodel = re.search(r'iPhone ', namemodel)
                if phonemodel is None:
                    continue
                phonemodel = 'iPhone '

                for model in models:
                    if model in namemodel:
                        for diferen in diferences:
                            if diferen in namemodel:
                                self.price_list.append([phonemodel + model + ' ' + diferen, int(price_num)])
                                continue

                        self.price_list.append([phonemodel + model, int(price_num)])

            j += 1
        return self.price_list
    def get_unique_models(self):
        self.unique_list.clear()
        for i in self.price_list:
            if not(i[0] in self.unique_list):
                self.unique_list.append(i[0])
        return self.unique_list

#test = site_checker()
#print(test.price_list[0][0])