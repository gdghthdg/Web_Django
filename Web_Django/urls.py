"""Web_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url

from . import views,testdb,search,post,search_sql,login

from django.contrib import admin
from django.urls import path

# urls.py
from django.conf.urls import url

from django.contrib import admin#admin登录



#一些url的规则映射
urlpatterns = [
    #path(route, view, kwargs=None, name=None)
    url(r'^$', views.hello),

    url(r'^testdb$', testdb.testdb),

    url(r'^admin/', admin.site.urls),#admin登录



    url(r'^search$', search.search),

    url(r'^search-post$', post.search_post),

    url(r'^search_post1$', post.search_post1),



    #查找物品的详细信息
    url(r'^search_info$', search_sql.search_info),

    #url(r'^search_info$', search_sql.search_show),
    url(r'^search_mysql$', search_sql.search_info),

    #登录账号
    url(r'^login$', login.login_funcation),

    #注册账号与忘记密码
    url(r'^login_register$', login.register),

    #选择一个物品,显示出它的信息
    url(r'^search_address$', search_sql.search_address),


]
