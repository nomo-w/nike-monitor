#!/usr/bin/python3
import product
import wechat
import os
import time


IMG_PATH = '/home/yzh/nike/myself_nike_bot/'
class MainApiTool:
    @staticmethod
    def get_product(country):
        #country_list = ['cn', 'de', 'us', 'jp']
        shoe_list = product.ProductApiTool.run(country)
        return shoe_list

    @staticmethod
    def _delete_img(filePath):
        '''
        删除文件
        delete file
        :param imgPath: 图片文件路径
        :return: None
        '''
        os.remove(filePath)

    @staticmethod
    def get_different_shoe(new_list, old_list):
        '''
        获取最新的球鞋信息,使用yield每次返回一个单独的球鞋
        :param new_list: 最新获取的球鞋列表
        :param old_list: 之前获取的球鞋列表
        :return: 单独球鞋信息 or None
        '''
        for n_dic in new_list:
            for o_dic in old_list:
                # 检测球鞋的id信息,如果一样就结束循环继续检测下一个球鞋
                if n_dic['id'] == o_dic['id']:
                    break
            else:
                # 如果for循环正常结束代表没有找到该球鞋id,证明该球鞋是新出的,返回该球鞋信息
                yield n_dic

    def __str_dictValue(func):
        '''
        将字典的所有值都转换成str
        :return:
        '''
        def inner(dic):
            for i in dic:
                dic[i] = str(dic[i])
            return func(dic)
        return inner

    @staticmethod
    @__str_dictValue
    def _custom_message(shoe_info):
        '''
        发售名称: AJ1
        发售价格: 1299
        发售库存: 37~42
        发售引擎: (DAN)常规抽签发售
        发售时间: 2019-05-13 9:00:00
        :param shoe_info:
        :return:
        '''
        message = '发售名称: {name}\n{price}{size}{se}{desc}\n发售时间: {time}' if str(shoe_info['type']) == '999999' \
            else '发售名称: {name}\n{price}{size}{se}发售时间: {time}'
        new_shoe_info = {'name': shoe_info['name'], 'time': shoe_info['time']}
        new_shoe_info['price'] = ['发售价格: ' + shoe_info['price'] + '\n', ''][shoe_info['price'] == 'None']
        new_shoe_info['size'] = ['发售库存: ' + shoe_info['size'] + '\n', ''][shoe_info['size'] == 'None']
        new_shoe_info['se'] = ['发售引擎: ' + shoe_info['se'] + '\n', ''][shoe_info['se'] == 'None']
        if str(shoe_info['type']) == '999999':
            new_shoe_info['desc'] = shoe_info['desc']
        return message.format(**new_shoe_info)

    @classmethod
    def send_shoes_message(cls, shoes_list, name):
        # 获取微信好友UserName
        UserName = wechat.WechatApiTool.get_UserName(name)
        for shoe in shoes_list:
            # 下载鞋子图片并返回新的列表
            new_shoe = product.ProductApiTool.download_shoe_img([shoe], IMG_PATH)
            # 整理鞋子尺码信息将原来的列表改为 36~42.5 格式
            new_shoe = product.ProductApiTool.handle_shoe_size(new_shoe)
            # 整理要发送的信息 'AJ1 (LEO)迷你抽签发售 1499 38~47'
            message = cls._custom_message(new_shoe[0])
            # 发送鞋子图片,0代表发送的是图片格式
            wechat.WechatApiTool.send_message_to_friend(UserName, new_shoe[0]['img'], 1)
            # 发送鞋子具体信息,1代表发送的是信息
            wechat.WechatApiTool.send_message_to_friend(UserName, message, 0)
            # 删除图片
            cls._delete_img(new_shoe[0]['img'])


if __name__ == '__main__':
    # 获取中国所有球鞋信息列表
    shoeInfo = MainApiTool.get_product('cn')
    # 过滤掉已经发售完的球鞋
    oldShoeL = product.ProductApiTool.handle_newShoe(shoeInfo)
    # 登录微信
    wechat.WechatApiTool.login()
    # 循环检测球鞋
    while True:
        shoeInfo = MainApiTool.get_product('cn')
        # 如果shoeInfo的内容是None代表请求失败
        if shoeInfo:
            newShoeL = product.ProductApiTool.handle_newShoe(shoeInfo)
            # 循环检测是否出现新鞋
            for i in MainApiTool.get_different_shoe(newShoeL, oldShoeL):
                # 如果检测到新鞋就将新鞋信息发送微信
                MainApiTool.send_shoes_message([i], '阿仁')
            # 将新的球鞋列表赋给旧的球鞋列表
            oldShoeL = newShoeL
            time.sleep(30)
        else:
            time.sleep(30)