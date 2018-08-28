# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    author_id = models.IntegerField(verbose_name="作者ID", null=False, blank=False, primary_key=True)
    name = models.CharField(verbose_name="作者姓名", max_length=128, null=True, blank=True)
    dynasty = models.CharField(verbose_name="作者年代", max_length=128, null=True, blank=True)
    context = models.TextField(verbose_name="作者简介", null=True, blank=True)
    desc = models.TextField(verbose_name="作者介绍", null=True, blank=True)
    image = models.CharField(max_length=128, null=True, blank=True)


class PoetryType(models.Model):
    type = models.CharField(max_length=28, null=True, blank=True)


class Poetry(models.Model):
    author_id = models.ForeignKey(Author)
    name = models.CharField(verbose_name="诗词名称", max_length=512, null=True, blank=True)
    dynasty = models.CharField(verbose_name="诗词年代", max_length=128, null=True, blank=True)
    content = models.TextField(verbose_name="诗词内容", null=True, blank=True)
    about = models.TextField(verbose_name="写作背景", null=True, blank=True)
    fanyi = models.TextField(verbose_name="译文", null=True, blank=True)
    shangxi = models.TextField(verbose_name="赏析", null=True, blank=True)
    tags = models.CharField(max_length=512, null=True, blank=True)


class HostSearch(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    count = models.IntegerField()
    ctime = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Love(models.Model):
    poetry_id = models.ForeignKey(Poetry)
    user_id = models.ForeignKey(User)
    ctime = models.DateTimeField(auto_now_add=True)


