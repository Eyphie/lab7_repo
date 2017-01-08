from django.conf.urls import url
from . import views
from shop.views import NewView, BasicView, SaleView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.navig, name='navigate'),
    url(r'^show_new/', login_required(redirect_field_name='', login_url='/login')(NewView.as_view())),
    url(r'^show_all/', login_required(redirect_field_name='', login_url='/login')(BasicView.as_view())),
    url(r'^show_sweet/', login_required(redirect_field_name='', login_url='/login')(SaleView.as_view())),
    url(r'^reg/', views.registration, name='registration'),
    url(r'^login/', views.log, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^login/$', auth_views.login),
]
