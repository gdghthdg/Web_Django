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

from . import views,testdb,search,post,search_sql

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

    url(r'^login/', admin.site.urls),#admin登录



    url(r'^search$', search.search),

    url(r'^search-post$', post.search_post),

    url(r'^search_post1$', post.search_post1),

    #url(r'^search_info$', search_sql.search_show),
    url(r'^search_sql$', search_sql.search_info),
]
