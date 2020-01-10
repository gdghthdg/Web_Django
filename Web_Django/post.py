# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    print('9999',request,request.POST)

    ctx = {}

    if request.POST:
        ctx['rlt'] = request.POST['q']
        ctx['name'] = request.POST['username']
        ctx['pawd'] = request.POST['password']

    print('ctx', ctx)
    return render(request, "post.html", ctx)

def search_post1(request):
    print('888888',request,request.POST)


    ctx = {}



    print('ctx', ctx)
    return render(request, "search_form.html", ctx)


