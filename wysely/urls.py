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
from invoices import urls as invoice_urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^invoices/', include(invoice_urls)),
    url(r'^accounts/profile/', TemplateView.as_view(template_name='registration/profile.html'), name='profile'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^about-us/', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
    # url(r'^invoices/', TemplateView.as_view(template_name='main_logged_in/invoices.html'), name='invoices'),
    url(r'^home/', TemplateView.as_view(template_name='main_logged_in/home.html'), name='home'),
    # url(r'^clients/', TemplateView.as_view(template_name='main_logged_in/clients.html'), name='clients'),
    # url(r'^products/', prod_views.ProductView.as_view(), name='products'),
    # url(r'^product_groups/', prod_views.ProductListView.as_view(), name='product_list'),
    # url(r'^client_groups/', prod_views.ClientListView.as_view(), name='client_list'),
    url(r'^customers/',include('customers.urls')),
    url(r'^users/',include('users.urls')),
    url(r'^products/',include('products.urls')),
    url(r'^companies/',include('companies.urls'))
]

urlpatterns += staticfiles_urlpatterns()
