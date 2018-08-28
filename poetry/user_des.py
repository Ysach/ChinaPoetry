# -*- coding:utf-8 -*-
# __author:    "Farmer"
# date:   2018/6/15
from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import DES


def user_crypt(num):
    key = '12345678'  # 长度必须是8位的
    text = str(num) + ' ' * (32 - len(str(num)))  # 长度必须是8的倍数,我用空格补的
    # 实例化
    obj = DES.new(key)
    # 加密
    cryp = obj.encrypt(text)
    pass_hex = b2a_hex(cryp)
    return pass_hex


def user_encrypt(pass_hex):
    key = '12345678'
    obj = DES.new(key)
    # 解密
    get_cryp = a2b_hex(pass_hex)
    after_text = obj.decrypt(get_cryp)
    return after_text.strip()
