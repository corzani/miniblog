from django.conf.urls import patterns, url

from blogmodule import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'^add_form/$', views.add_form, name='add_form'),
    url(r'^insert_post/$', views.insert_post, name='insert_post'),
)
