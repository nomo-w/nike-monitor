from lxml import etree
import requests
import random


class Proxy:
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'host': "www.xicidaili.com",
        'if-none-match': "W/\"61f3e567b1a5028acee7804fa878a5ba\"",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36"
    }

    @classmethod
    def get_proxy(cls, proxy_url):
        # 请求代理ip网站
        resp = requests.get(proxy_url, headers=cls.headers)
        # 对获取的页面进行解析
        selector = etree.HTML(resp.text)
        # print(selector.xpath("//title/text()"))
        proxies = []
        # 信息提取
        for each in selector.xpath("//tr[@class='odd']"):
            # ip.append(each[0])
            ip = each.xpath("./td[2]/text()")[0]
            port = each.xpath("./td[3]/text()")[0]
            http_type = each.xpath("./td[6]/text()")[0]
            proxies.append(
                {'http': '://'.join((http_type.lower(), ':'.join((ip, port)))),
                 'https': '://'.join((http_type.lower(), ':'.join((ip, port))))}
            )
        return proxies

    @staticmethod
    def check_proxy(proxies_list):
        new_proxies_list = []
        for i in proxies_list:
            try:
                resp = requests.get('http://icanhazip.com', proxies=i)
            except Exception:
                continue
            else:
                if i['http'].split('/')[-1].split(':')[0] in resp.text:
                    new_proxies_list.append(i)
        return new_proxies_list

    @classmethod
    def return_random_proxy(cls, proxy_url):
        proxies_list = cls.get_proxy(proxy_url)
        proxies_list = cls.check_proxy(proxies_list)
        return random.choice(proxies_list)


w = Proxy.get_proxy('https://www.xicidaili.com/nt')
w1 = Proxy.check_proxy(w)
print(w1)