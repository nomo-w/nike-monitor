#!/usr/bin/python3
import requests

from bs4 import BeautifulSoup


class Producte:
    @staticmethod
    def request_get(url, auth=False, verify=False, isjson=False):
        resp = requests.get(url, auth=auth, verify=verify) if auth else requests.get(url, verify=verify)
        result = resp.json() if isjson else resp.text
        return result

    def __get_products_url_zsq(func):
        def inner(nike_url):
            resp = Producte.request_get(nike_url, verify=True)
            bs = BeautifulSoup(resp, 'html.parser')
            section_tag = bs.select('div .ncss-container > section')[0]
            # section_tag = bs.find('section', class_='upcoming-section bg-white ncss-row prl2-md prl5-lg pb4-md pb6-lg')
            product_list = section_tag.find_all('figure')
            return func(product_list)
        return inner

    @staticmethod
    @__get_products_url_zsq
    def get_products_url(nike_url):
        return [''.join(('https://www.nike.com', p.find('a')['href'])) for p in nike_url]

    def __get_product_info_zsq(func):
        def inner(product_url):
            resp = Producte.request_get(product_url, verify=True)
            bs = BeautifulSoup(resp, 'html.parser')
            product_img = bs.find('figure', class_='ncss-col-sm-12 ncss-col-lg-6 prl0-sm prl2-lg mt4-lg va-sm-t')
            product_info = bs.find('aside', class_='product-info-container ncss-row ta-sm-c pt6-sm prl7-md pb6-sm pt0-lg pb0-lg')
            product = {'img': product_img, 'info': product_info, 'product_url': product_url}
            return func(product)
        return inner

    @staticmethod
    @__get_product_info_zsq
    def get_product_info(product_url):
        try:
            product_img_url = product_url['img'].find('img')['src']
            product_name = product_url['info'].find('h5').text
            product_price = product_url['info'].find('div', class_='ncss-brand pb6-sm fs14-sm fs16-md').text
            product_des = product_url['info'].find('div', class_='description-text text-color-grey').find('p').text
        except:
            print(product_url['product_url'])
            return False
        return {'img': product_img_url, 'name': product_name, 'proce': product_price, 'des': product_des}


if __name__ == '__main__':
    product_url_list = Producte.get_products_url('https://www.nike.com/cn/launch/')
    # print(product_url_list)
    e = [Producte.get_product_info(i) for i in product_url_list]
    print(e)