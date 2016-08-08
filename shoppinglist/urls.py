"""windjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.init,name='init' ),
    url(r'^new/$',views.createlist,name='createlist'),
    url(r'^myshoppinglists/$',views.myshoppinglists,name='myshoppinglists'),
    url(r'^myshoppinglists/detail/(?P<pk>\d+)/$',views.list_detail,name='listdetail'),
    url(r'^login/$',views.userlogin,name='userlogin'),
    url(r'^logout/$',views.userlogout,name='userlogout'),
    url(r'^registernew/$',views.newuser,name='newuser'),
    url(r'^welcome/$',views.welcome,name='welcome'),
]
