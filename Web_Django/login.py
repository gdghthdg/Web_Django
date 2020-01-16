from django.shortcuts import render
from funcation_py.common import *


def login_funcation(request):




    try:
        print("request", request)
        ctx={}
        print('ok是什么',request.POST.get('admin'))

        ctx['admin']=request.POST.get('admin')
        ctx['password']=request.POST.get('password')


        print("request",request,ctx)

        sql_order="select * from user_admin where user_number='%s' and password='%s'"%(ctx['admin'],ctx['password'])
        print(sql_order)
        result=mysql_execute(sql_order)
        print("得到一个mysql的结果",result)

        if len(result)!=0:
            return render(request, "search_form.html", ctx)

        else:
            ctx['result']="没有账号,请注册"


    except Exception:
        print_exc()




    return render(request, "login.html", ctx)

def register(request):
    return HttpResponse("<p>" + " NO exploitation " + "</p>")