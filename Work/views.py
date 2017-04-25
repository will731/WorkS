# -*- coding: UTF-8 -*-
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
import json
from Work import models
from django import forms
from Work.models import (Userinfo,User)
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login  as loginuser
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required,login_required


"""
@获取当前登录用户
"""

from django.contrib import auth


# Create your views here.

def base(request):
    return render_to_response('base.html')
def index(request):
    return render_to_response('index.html')

def get_data(request):
    if request.method == "POST":

        bt=request.POST['bt']
        lx=request.POST['lx']
        cjr=request.POST['cjr']
        clr=request.POST['clr']

        d={
            'bt':bt,
            'lx':lx,
            'cjr':cjr,
            'clr':clr,

        }
        #print d
        bts=models.work.objects.create(biaoti=bt,gd_type=lx,auth=cjr,chuliren=clr)
        bts.save()
        return HttpResponseRedirect('/list/')

    else:
        return request.GET



def get_xqydatas(request,id_num):

    """

    :param request:
    :param id_num:
    :return:

    #data=models.work.objects.all()
    #print data


    #ids获取前端传过来的id
    """

    ids=models.work.objects.filter(work_id=id_num)



    return render_to_response('xqy.html',{'data':ids})




def updata(request):
    if request.method == "POST":

        xqy=request.POST['xqy']
        id=request.POST['id']
        if xqy == u"同意":
            datas=models.work.objects.get(work_id=id)
            datas.status = xqy
            datas.save()

            return HttpResponseRedirect('/list/')
        if xqy == u'不同意':

            #return HttpResponseRedirect('/index/')
            return HttpResponse(u'没按规定时间内申请')


    else:
        return HttpResponse(u'请使用post方式提交数据')





#@permission_required('Work.shenpi',raise_exception=True)

#@login_required(login_url="/")
#@permission_required('Work.shenpi',raise_exception=False,login_url="/login/")
def list(request):

    from Work.models import work


    user = request.user
    print ">"*20,user

    nowuser = auth.get_user(request)
    print nowuser
    is_add = True if nowuser.has_perm('Work.shenpi') else False
    print is_add

    """
    @打印登录用户是否具有审批权限，true为真，false为假
    """
    print "*"*30,request.user.has_perm('Work.shenpi')
    data = work.objects.all()
    return render_to_response('gd.html', {'data': data,'is_add':is_add,'nowuser':nowuser})



def shenpi(request):
    pass


class UserForm(forms.Form):
    username = forms.CharField(label="user",max_length=100)
    password = forms.CharField(label="passwd",widget=forms.PasswordInput())


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #print username, password, "[*******]"

            user1 = authenticate(username=username, password=password)
            is_add = True if user1.has_perm('Work.shenpi') else False
            #print 'user1--->', user1, user1.has_perm('Work.shenpi'), is_add
            if user1:
                loginuser(request,user1)
                return render_to_response('base.html', locals(), context_instance=RequestContext(request))
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf})