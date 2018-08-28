# -*- coding:utf-8 -*-
# __author:    "Farmer"
# date:   2018/5/22
from django import template
from binascii import b2a_hex
from Crypto.Cipher import DES
import datetime
import time
from django.utils.translation import ugettext, ungettext_lazy
from django.utils.html import avoid_wrapping
from django.utils.timezone import is_aware, utc
import calendar
from django.template.defaultfilters import stringfilter


register = template.Library()


# template对queryset排序
@register.filter()
def order_by_id(queryset, args):
    args = args.split(',')
    return queryset.order_by('-id')[args[0]:args[1]]


@register.filter()
def user_des(num):
    key = '12345678'  # 长度必须是8位的
    # print "=======", num
    text = str(num) + ' ' * (16 - len(str(num)))  # 长度必须是8的倍数,我用空格补的
    # 实例化
    obj = DES.new(key)
    # 加密
    cryp = obj.encrypt(text)
    pass_hex = b2a_hex(cryp)
    return pass_hex


# 时间返回
TIMESINCE_CHUNKS = (
    (60 * 60 * 24 * 365, ungettext_lazy('%d'+u'年前', '%'+u'年前')),
    (60 * 60 * 24 * 30, ungettext_lazy('%d'+u'月前', '%d'+u'月前')),
    (60 * 60 * 24 * 7, ungettext_lazy('%d'+u'周前', '%d'+u'周前')),
    (60 * 60 * 24, ungettext_lazy('%d'+u'天前', '%d'+u'天前')),
    (60 * 60, ungettext_lazy('%d'+u'小时前', '%d'+u'小时前')),
    (60, ungettext_lazy('%d'+u'分钟前', '%d'+u'分钟前'))
)


def time_since(d, now=None):
    if not isinstance(d, datetime.datetime):
        d = datetime.datetime(d.year, d.month, d.day)
    if now and not isinstance(now, datetime.datetime):
        now = datetime.datetime(now.year, now.month, now.day)
    if not now:
        now = datetime.datetime.now(utc if is_aware(d) else None)
    delta = now - d
    leapdays = calendar.leapdays(d.year, now.year)
    if leapdays != 0:
        if calendar.isleap(d.year):
            leapdays -= 1
        elif calendar.isleap(now.year):
            leapdays += 1
    delta -= datetime.timedelta(leapdays)

    since = delta.days * 24 * 60 * 60 + delta.seconds
    if since <= 0:
        return avoid_wrapping(ugettext('0'+u'分钟前'))
    x = 0
    seconds = 0
    name = ""
    count = 1
    for x, (seconds, name) in enumerate(TIMESINCE_CHUNKS):
        count = since // seconds
        if count != 0:
            break
    result = avoid_wrapping(name % count)
    if x + 1 < len(TIMESINCE_CHUNKS):
        seconds2, name2 = TIMESINCE_CHUNKS[x + 1]
        count2 = (since - (seconds * count)) // seconds2
        if count2 != 0:
            result += ugettext(', ') + avoid_wrapping(name2 % count2)
    return result


@register.filter
def age(value):
    now = datetime.datetime.now()
    try:
        difference = now - value
    except Exception as e:
        return str(e)

    if difference <= datetime.timedelta(minutes=1):
        return '刚刚'
    if difference >= datetime.timedelta(minutes=60 * 24 * 30 * 2):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    return time_since(value).split(', ')[0]


@register.filter
@stringfilter
def trim(value):
    return value.strip()
