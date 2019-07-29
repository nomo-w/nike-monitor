#!/usr/bin/python3
import requests
import random
import time
from proxy import Proxy
requests.packages.urllib3.disable_warnings()


class ProductApiUrl:
    # 获取nike近期发售的50个商品的信息,返回json数据
    cn = 'https://api.nike.com/snkrs/content/v1/?&country=CN&language=zh-Hans&offset=0&orderBy=published'
    de = 'https://api.nike.com/snkrs/content/v1/?country=DE&language=de&offset=0&orderBy=published'
    us = 'https://api.nike.com/snkrs/content/v1/?country=US&language=en&offset=0&orderBy=published'
    jp = 'https://api.nike.com/snkrs/content/v1/?country=JP&language=ja&offset=0&orderBy=published'

    User_Agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "SNKRS/3.9.0 (iPhone; iOS 12.1; Scale/2.00)"
    ]

    def __init__(self):
        self.url = {'cn': self.cn, 'de': self.de, 'us': self.us, 'jp': self.jp}

    def get_url(self, country):
        return self.url[country]


class ProductApiTool:
    @staticmethod
    def request_get(url, header, verify=False, isjson=False, proxy=None):
        resp = requests.get(url, headers=header, verify=verify, proxies=proxy) if \
            proxy else requests.get(url, headers=header, verify=verify)
        result = resp.json() if isjson else resp.text
        return result

    @staticmethod
    def generate_header(userAgents_list):
        return {
            'User-Agent': random.choice(userAgents_list),
            'Upgrade-Insecure-Requests': '1',
            'Host': 'api.nike.com',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        }

    @staticmethod
    def handle_selectionEngine(se):
        seD = {'FLOW': '(FLOW)先到先得发售',
               'LEO': '(LEO)迷你抽签发售',
               'DAN': '(DAN)常规抽签发售',
               'other': '(%s)未知的发售方式' % se}
        return seD[se] if seD.get(se) else seD['other']

    @staticmethod
    def handle_startSellDate(sd, ct):
        """
        根据不同时区转换发售时间
        :param sd: 发售时间
        :param ct: 时区
        :return: 转换后的发售时间
        """
        sd = sd[:19].replace('T', ' ')
        timeArray = time.strptime(sd, "%Y-%m-%d %H:%M:%S")
        timestamp = int(time.mktime(timeArray))  # 转换成时间戳
        if ct in ['cn', 'us']:
            timeArray = time.localtime(timestamp + 28800)
        elif ct == 'jp':
            timeArray = time.localtime(timestamp + 32400)
        elif ct == 'de':
            timeArray = time.localtime(timestamp + 21600)
        # resulttime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    @classmethod
    def handle_nike_param(cls, shoe_json, country):
        '''
        返回单个鞋子的具体信息
        :param shoe_json: 单个鞋子的json数据
        :param country: 国家, 用来转换发售时间用的
        :return: 鞋子的数据字典(名字, 价钱, 货量, ...)
        '''
        id = shoe_json['id']
        threadId = shoe_json['threadId']
        interestId = shoe_json['interestId']
        name = shoe_json['name']
        publishedDate = cls.handle_startSellDate(shoe_json['publishedDate'], country)
        restricted = shoe_json['restricted'] # 限制?
        feed = shoe_json['feed']
        title = shoe_json['title']
        seoSlug = shoe_json['seoSlug']
        seoTitle = shoe_json['seoTitle']
        seoDescription = shoe_json['seoDescription']
        imageUrl = shoe_json['imageUrl']

        p = shoe_json['product']
        productStyle = p['style']  # 发售代码 999999代表不是鞋子
        # 不是999999代表是鞋子
        if productStyle != '999999':
            productId = p['id']
            productInterestId = p['interestId']
            productColorCode = p['colorCode']
            productGlobalPid = p['globalPid']
            productTitle = p['title']
            productSubtitle = p['subtitle']
            productImageUrl = p['imageUrl']
            productgenders = p['genders']
            productQuantityLimit = p['quantityLimit']  # 购买限制?
            productMerchStatus = p['merchStatus']  # 鞋子状态 'HOLD'
            productColorDescription = p['colorDescription']
            productAvailable = p['available']
            productPublishType = p['publishType']
            productType = p['productType']  # FOOTWEAR
            productUpcoming = p['upcoming']
            msrp = p['price']['msrp']  # 建议零售价
            fullRetailPrice = p['price']['fullRetailPrice']  # 应该是最高售价
            currentRetailPrice = p['price']['currentRetailPrice']  # 当前售价
            onSale = p['price']['onSale']  # 是否发售false
            # 发售引擎
            selectionEngine = cls.handle_selectionEngine(p['selectionEngine']) if productPublishType != 'FLOW' \
                              else cls.handle_selectionEngine(productPublishType)

            # 发售日期
            productStartSellDate = cls.handle_startSellDate(p['startSellDate'], country)

            # 库存列表
            productSkus = p['skus']
            skusIdL = [i['id'] for i in productSkus]
            skusSizeL = [s['localizedSize'] for s in productSkus]
        else:
            selectionEngine = None
            productImageUrl = imageUrl
            currentRetailPrice = None
            skusSizeL = None
            productStartSellDate = publishedDate

        # 购物车?? 暂时不处理这个字段
        cards = shoe_json['cards']

        return {'id': id,  # 产品id,用来比对商品的
                'type': productStyle,  # 发售类型如果是999999代表不是球鞋
                'name': name,  # 鞋名字
                'img': productImageUrl,  # 鞋图片
                'time': productStartSellDate,  # 发售日期
                'se': selectionEngine,  # 发售方式
                'price': currentRetailPrice,  # 发售价
                'size': skusSizeL,  # 库存列表
                'desc': seoDescription  # 商品描述
                }

    @staticmethod
    def download_shoe_img(shoes_list, img_dir):
        '''
        下载球鞋图片到img_dir,并将列表中的图片的值改为图片路径
        :param shoes_list: 球鞋列表
        :param img_dir: 下载图片的文件
        :return: 新的球鞋列表
        '''
        for i in shoes_list:
            imgname = [i['img'].split('/')[-1] + '.jpg', i['img'].split('/')[-1]][i['img'].split('/')[-1][-4:] == '.jpg']
            img = requests.get(i['img'])
            with open(img_dir + imgname, 'wb') as f:
                f.write(img.content)
                i['img'] = img_dir + imgname
        return shoes_list

    @staticmethod
    def handle_shoe_size(shoes_list):
        '''
        将球鞋尺码列表变成字符串 36.5~45
        :param shoes_list: 球鞋列表
        :return: 新的球鞋列表
        '''
        for i in shoes_list:
            if i['size']:
                i['size'] = '~'.join((i['size'][0], i['size'][-1]))
        return shoes_list

    @staticmethod
    def _unix_time(dt):
        # 转换成时间数组
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = int(time.mktime(timeArray))
        return timestamp

    @classmethod
    def handle_newShoe(cls, shoes_list):
        '''
        将发售日期已经过了的球鞋过滤掉
        :param shoes_list: 球鞋列表
        :return: 还未发售的球鞋列表
        '''
        new_shoe_list = []
        for i in shoes_list:
            if cls._unix_time(i['time']) >= int(time.time()):
                new_shoe_list.append(i)
        return new_shoe_list

    @classmethod
    def run(cls, country):
        apiurl = ProductApiUrl()
        header = cls.generate_header(apiurl.User_Agents)  # 获取请求头
        url = apiurl.get_url(country)  # 根据传入的城市代码获取url
        shoe_api = cls.request_get(url, header=header, isjson=True, proxy=Proxy.return_random_proxy())  # 访问nike的api得到鞋子的信息
        try:
            shoe_list = [cls.handle_nike_param(i, country) for i in shoe_api['threads']]  # 获取鞋子的精简信息
        except KeyError:
            shoe_list = None
            # print('请求nike的api时出现问题')
            print('request nikeApi ERROR')
        return shoe_list


if __name__ == '__main__':
    apiurl = ProductApiUrl()
    header = ProductApiTool.generate_header(apiurl.User_Agents)
    url = apiurl.get_url('cn')
    shoe_list = ProductApiTool.request_get(url, header=header, isjson=True)
    for i in shoe_list['threads']:
        shoe = ProductApiTool.handle_nike_param(i, 'cn')
        print(shoe['name'], shoe['time'], shoe['se'], shoe['price'], shoe['size'], shoe['img'])