from django.conf.urls import include, url
from mobile_list import views


urlpatterns = [
    # url(r'^index$', views.index),
    # 一个
    # url(r'^index/$', views.index, name='index'),
    # url(r'^index/charts-1', views.charts_1, name='charts_1'),
    # url(r'^index/charts-2', views.charts_2, name='charts_2'),
    # url(r'^index/charts-3', views.charts_3, name='charts_3'),
    # url(r'^index/charts-4', views.charts_4, name='charts_4'),
    # url(r'^index/charts-5', views.charts_5, name='charts_5'),
    # url(r'^index/charts-6', views.charts_6, name='charts_6'),
    # url(r'^index/charts-7', views.charts_7, name='charts_7'),
    # url(r'^index/welcome', views.welcome, name='welcome'),
    # url(r'^table/', views.table_show, name='table_show'),
    # url(r'^search_result/$', views.search),
    # url(r'', views.login, name='login'),
    # url(r'^login/$', views.login),
    url(r'^index/$', views.index),
    url(r'^index/index$', views.index),
    url(r'^index/index_2$', views.index_2),
    url(r'^login_ajax_check$', views.login_ajax_check),
    url(r'', views.login),




]

