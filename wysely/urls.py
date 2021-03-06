"""Wysely URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from companies.views import NavMenuView
from users.views import ProfileView, HomeView
# from wysely.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/', ProfileView.as_view(), name='profile'),
    url(r'^$', NavMenuView.as_view(), name='index'),
    url(r'^about-us/', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
    url(r'^home/', HomeView.as_view(), name='home'),
    url(r'^customers/',include('customers.urls')),
    url(r'^users/',include('users.urls')),
    url(r'^products/',include('products.urls')),
    url(r'^companies/',include('companies.urls')),
    url(r'^invoices/',include('invoices.urls')),
    url(r'^templates/',include('invoicetemplates.urls'))
]

urlpatterns += staticfiles_urlpatterns()

#handle errors
handler404 = 'wysely.views.not_found'

handler500 = 'wysely.views.server_error'

handler403 = 'wysely.views.permission_denied'

handler400 = 'wysely.views.bad_request'

handler405 = 'wysely.views.not_allowed'