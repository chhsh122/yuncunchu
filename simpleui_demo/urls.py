"""simpleui_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

admin.site.site_title = '竹悦大规模分布式集群云存储软件'
admin.site.site_header = '竹悦大规模分布式集群云存储软件'

urlpatterns = [
    # 配置admindoc
    url(r'doc/', include('django.contrib.admindocs.urls'), name='doc'),
    path('', admin.site.urls),
]
