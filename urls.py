"""ChinaPoetry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from poetry import views
from django.views.generic.base import RedirectView


handler404 = views.page_not_found


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login/', views.user_login, name='login'),
    url(r'^poetry/content/(\w+)/$', views.poetry_content, name='poetry_content'),
    url(r'^search_home/$', views.search_home, name='search_home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^love/$', views.love, name='love'),
    url(r'^mine/$', views.mine, name='mine'),
    # url(r'^poe/', views.poet),
    # url(r'^type/', views.poetry_type)
]
