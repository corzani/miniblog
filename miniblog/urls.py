from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^blog/', include('blogmodule.urls')), 
    url(r'^$',  RedirectView.as_view(url='/blog/')),
)
