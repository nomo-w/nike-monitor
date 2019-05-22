#!/usr/bin/python3
import itchat
import time


class WechatApiTool:
    @staticmethod
    def login():
        '''
        登录微信
        '''
        itchat.auto_login(hotReload=True)

    @staticmethod
    def get_friends():
        '''
        返回所有好友列表
        '''
        return itchat.get_friends()

    @staticmethod
    def search_friend(name):
        '''
        返回单个好友的具体信息列表
        '''
        return itchat.search_friends(name)

    @classmethod
    def get_UserName(cls, name):
        '''
        返回微信朋友对应的UserName
        '''
        wechatO = cls.search_friend(name)
        return wechatO[0]['UserName']

    @staticmethod
    def send_message_to_friend(friend, message, message_type):
        '''
        发送信息给微信好友
        :param friend: 微信好友的UserName
        :param message: 发送的信息
        :param message_type: 信息类型
        '''
        m_t = {
            '0': 'msg',
            '1': 'img',
            '2': 'file'
        }
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message_type = m_t[str(message_type)]
        if message_type == 'msg':
            itchat.send_msg(message, friend)
            print('Send message to "%s" %s' % (friend, now))
        elif message_type == 'img':
            itchat.send_image(message, friend)
            print('Send image to "%s" %s' % (friend, now))
        elif message_type == 'file':
            itchat.send_file(message, friend)
            print('Send file to "%s" %s' % (friend, now))

    @staticmethod
    def send_message_to_group(group, message):
        itchat.send(message, group)