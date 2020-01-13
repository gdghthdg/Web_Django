from TestModel.models import Test,Tag,Contact,thing_info
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
from django.shortcuts import render
from funcation_py.mysql_py import *


# def search_show(request):
#     return render_to_response('search_form.html')
#

def search_mysql(thing_txm):
    sql_order= "select Location_OK,Location_NG from mysql_thing_lh where TXM='%s'"%thing_txm

    result=mysql_execute(sql_order)

    print(result)

    return result


def search_info(request):
    ctx={}
    print("头", request, ctx)
    print('post', request.POST)

    try:
        txm = request.POST['q']

        result=search_mysql(txm)
        ctx['thing_okaddress'] = result[0][0]
        ctx['thing_ngaddress'] = result[0][1]

        print("thing_address",result)

        obj = thing_info.objects.get(TXM=txm)
        print('22222',obj)
        ctx['txm']=obj.TXM
        ctx['typeof'] = obj.TYPEOF
        ctx['wupin_name'] = obj.WUPIN_NAME
        #message = '你搜索的内容为: ' + request.POST['q']

    except Exception:
        #message = '没有此结果'
        ctx['result'] = '查询无结果'
        #return HttpResponse(message)

    print("request",request,ctx)
    return render(request, "search_form.html", ctx)


    #return HttpResponse(obj.TYPEOF)
