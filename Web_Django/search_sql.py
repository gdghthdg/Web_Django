from TestModel.models import Test,Tag,Contact,thing_info
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators import csrf
from django.shortcuts import render

# def search_show(request):
#     return render_to_response('search_form.html')
#

def search_info(request):
    ctx={}
    print('post', request.POST)

    try:
        txm = request.POST['q']
        obj = thing_info.objects.get(TXM=txm)
        print('22222',obj)
        ctx['txm']=obj.TXM
        ctx['typeof'] = obj.TYPEOF
        ctx['wupin_name'] = obj.WUPIN_NAME
        #message = '你搜索的内容为: ' + request.POST['q']



    except Exception:
        #message = '没有此结果'
        ctx['result'] = '没有此结果'
        #return HttpResponse(message)



    print("request",request,ctx)
    return render(request, "search_form.html", ctx)


    #return HttpResponse(obj.TYPEOF)
