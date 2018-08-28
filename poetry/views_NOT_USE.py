# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
import models
import os


# Create your views here.


def index(request):
    for i in xrange(1, 3200):
        json_file = "poet/poet_" + str(i) + ".json"
        print "当前解析文件: ", json_file
        if os.path.isfile(json_file):
            with open(json_file) as f:
                file_dict = json.load(f)
                try:
                    name = file_dict.get('name', '')
                    author_id = file_dict.get('id')
                    dynasty = file_dict.get('dynasty')
                    content = file_dict.get('content', '')
                    desc = file_dict.get('desc', '')
                    image = file_dict.get('image', '').split('/')[-1]
                    models.Author.objects.create(name=name,
                                                 author_id=author_id,
                                                 dynasty=dynasty,
                                                 context=content,
                                                 desc=desc,
                                                 image=image
                                                 )
                except Exception as e:
                    print str(e)
                    return HttpResponse(str(e) + json_file)
        else:
            print "文件不存在: ", json_file
    return HttpResponse("OK")


def poet(request):
    for i in xrange(1, 80000):
        json_file = "poe/poetry_" + str(i) + ".json"
        print "当前文件----> ", json_file
        if os.path.isfile(json_file):
            with open(json_file) as f:
                file_dict = json.load(f)
                try:
                    about = file_dict.get('about', '')
                    name = file_dict.get('name', '')
                    fanyi = file_dict.get('fanyi', '')
                    content = file_dict.get('content', '')
                    dynasty = file_dict.get('dynasty', '')
                    shangxi = file_dict.get('shangxi', '')
                    tags = ','.join(file_dict.get('tags'))
                    author_id = int(file_dict.get('poet').get('id'))
                    models.Poetry.objects.create(author_id_id=author_id,
                                                 name=name,
                                                 dynasty=dynasty,
                                                 content=content,
                                                 about=about,
                                                 fanyi=fanyi,
                                                 shangxi=shangxi,
                                                 tags=tags
                                                 )
                except Exception as e:
                    print str(e)
                    return HttpResponse(str(e) + json_file)
        else:
            print "文件不存在: ", json_file
    return HttpResponse("OK")


def poetry_type(request):
    t = [
        "写景",
        "咏物",
        "春天",
        "夏天",
        "秋天",
        "冬天",
        "写雨",
        "写雪",
        "写风",
        "写花",
        "梅花",
        "荷花",
        "菊花",
        "柳树",
        "月亮",
        "山水",
        "写山",
        "写水",
        "长江",
        "黄河",
        "儿童",
        "写鸟",
        "写马",
        "田园",
        "边塞",
        "地名",
        "抒情",
        "爱国",
        "离别",
        "送别",
        "思乡",
        "思念",
        "爱情",
        "励志",
        "哲理",
        "闺怨",
        "悼亡",
        "写人",
        "老师",
        "母亲",
        "友情",
        "战争",
        "读书",
        "惜时",
        "婉约",
        "豪放",
        "诗经",
        "民谣",
        "节日",
        "春节",
        "元宵节",
        "寒食节",
        "清明节",
        "端午节",
        "七夕节",
        "中秋节",
        "重阳节",
        "忧国忧民",
        "咏史怀古",
        "宋词精选",
        "词牌大全",
        "古文观止",
        "小学古诗",
        "初中古诗",
        "高中古诗",
        "小学文言文",
        "初中文言文",
        "高中文言文",
        "古诗十九首",
        "唐诗三百首",
        "古诗三百首",
        "宋词三百首"
    ]
    for ty in t:
        models.PoetryType.objects.create(type=ty)

    return HttpResponse("Type")
