# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-06 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrendLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122, verbose_name='名称描述')),
                ('url', models.CharField(max_length=122, verbose_name='链接')),
            ],
            options={
                'verbose_name': '友链',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(verbose_name='发表时间'),
        ),
    ]
