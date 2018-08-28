# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-13 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u4f5c\u8005ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u4f5c\u8005\u59d3\u540d')),
                ('dynasty', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u4f5c\u8005\u5e74\u4ee3')),
                ('context', models.TextField(blank=True, null=True, verbose_name='\u4f5c\u8005\u7b80\u4ecb')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='\u4f5c\u8005\u4ecb\u7ecd')),
                ('image', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=512, null=True, verbose_name='\u8bd7\u8bcd\u540d\u79f0')),
                ('dynasty', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u8bd7\u8bcd\u5e74\u4ee3')),
                ('content', models.TextField(blank=True, null=True, verbose_name='\u8bd7\u8bcd\u5185\u5bb9')),
                ('about', models.TextField(blank=True, null=True, verbose_name='\u5199\u4f5c\u80cc\u666f')),
                ('fanyi', models.TextField(blank=True, null=True, verbose_name='\u8bd1\u6587')),
                ('shangxi', models.TextField(blank=True, null=True, verbose_name='\u8d4f\u6790')),
                ('tags', models.CharField(blank=True, max_length=512, null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poetry.Author')),
            ],
        ),
        migrations.CreateModel(
            name='PoetryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=28, null=True)),
            ],
        ),
    ]