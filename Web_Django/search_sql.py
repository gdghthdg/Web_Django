from TestModel.models import Test, Tag, Contact, thing_info
from django.shortcuts import render
from funcation_py.common import *


# def search_show(request):
#     return render_to_response('search_form.html')
#

def insert_data_choice():
    sql_order = "select WUPIN_NAME from mysql_thing_lh"
    result = mysql_execute(sql_order)

    wupin_name_list = []
    for i in result:
        wupin_name_list.append(i[0])

    return wupin_name_list


def search_mysql(thing_txm):
    sql_order = "select Location_OK,Location_NG from mysql_thing_lh where TXM='%s'" % thing_txm

    result = mysql_execute(sql_order)

    print(result)

    return result


def search_info(request):
    ctx = {}
    print("头", request, ctx)
    print('post', request.POST)

    try:
        txm = request.POST['q']

        result = search_mysql(txm)

        ctx['thing_okaddress'] = result[0][0]
        ctx['thing_ngaddress'] = result[0][1]

        print("thing_address", result)

        obj = thing_info.objects.get(TXM=txm)
        print('22222', obj)
        ctx['txm'] = obj.TXM
        ctx['typeof'] = obj.TYPEOF
        ctx['wupin_name'] = obj.WUPIN_NAME
        # message = '你搜索的内容为: ' + request.POST['q']



    except Exception:
        print_exc()
        # message = '没有此结果'
        ctx['result'] = '查询无结果'
        # return HttpResponse(message)

    ctx['list'] = insert_data_choice()
    print("request", request, ctx)

    return render(request, "search_form.html", ctx)

    # return HttpResponse(obj.TYPEOF)


def search_address(request):
    try:
        ctx = {}
        list_choise = request.POST['list_choice']
        print('选择的东西', list_choise)
        sql_order = "select TXM,TYPEOF,WUPIN_NAME,Location_OK,Location_NG from mysql_thing_lh where WUPIN_NAME='%s'" % list_choise
        result = mysql_execute(sql_order)

        print('选择得到的详细的地址', result)
        if len(result)!=0:
            ctx['txm'] = result[0][0]
            ctx['typeof'] = result[0][1]
            ctx['wupin_name'] = result[0][2]
            ctx['thing_okaddress'] = result[0][3]
            ctx['thing_ngaddress'] = result[0][4]





    except Exception:
        print_exc()

    ctx['list'] = insert_data_choice()
    return render(request, "search_form.html", ctx)
