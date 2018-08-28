# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-20 03:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poetry', '0005_auto_20180619_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('poetry_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poetry.Poetry')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
