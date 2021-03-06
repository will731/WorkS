# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-25 01:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='quanxian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shuoming', models.CharField(max_length=100)),
            ],
            options={
                'permissions': (('shenpi', '\u5ba1\u6279\u6743\u9650'),),
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('work_id', models.AutoField(primary_key=True, serialize=False)),
                ('biaoti', models.CharField(max_length=255, verbose_name='\u5de5\u5355\u6807\u9898')),
                ('gd_type', models.CharField(max_length=255, verbose_name='\u5de5\u5355\u7c7b\u578b')),
                ('auth', models.CharField(max_length=255, verbose_name='\u521b\u5efa\u4eba')),
                ('auth_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.CharField(default='\u5ba1\u6838\u5f85', max_length=255, verbose_name='\u5f85\u5ba1\u6838')),
                ('chuliren', models.CharField(max_length=255, verbose_name='\u5f53\u524d\u5904\u7406\u4eba')),
            ],
        ),
    ]
