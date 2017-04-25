# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

#工单表
class work(models.Model):
    work_id=models.AutoField(primary_key = True)
    biaoti=models.CharField(max_length=255,verbose_name=u'工单标题')
    gd_type=models.CharField(max_length=255,verbose_name=u'工单类型')
    auth=models.CharField(max_length=255,verbose_name=u'创建人')
    auth_time=models.DateTimeField(u'创建时间', auto_now = True)
    status = models.CharField(max_length=255, default=u'审核待', verbose_name=u'待审核')
    chuliren=models.CharField(max_length=255,verbose_name=u'当前处理人')

    def __unicode__(self):
        return u'%s %s %s %s %s %s' % (self.biaoti,self.gd_type,self.auth,self.auth_time,self.status,self.chuliren)
"""

#状态表
class zhuangtaibiao(models.Model):


    def __unicode__(self):
        return self.status
"""
#自定义的用户表
class Userinfo(models.Model):
    user = models.OneToOneField(User) #关联django user表
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __unicode__(self):
        return self.username



#自定义权限表

class quanxian(models.Model):
    shuoming=models.CharField(max_length=100)
    def __unicode__(self):
        return self.shuoming
    class Meta:
        permissions = (
            ('shenpi',u'审批权限'),
            #('edit', u'编辑权限'),
            #('add', u'添加权限'),
            #('DEL',u'删除权限'),
            #('list',u'查看权限'),
        )
"""

#状态表（包含3个状态，同意，不同意，已审核）
class Work_status(models.Model):
    pass

#工作日志表，用于前端展示流步骤情况
class work_logs(models.Model):
    Operation_name=models.CharField(max_length=255,verbose_name=u'操作名称')
    Operation_time=models.DateTimeField(u'操作时间',)

"""
