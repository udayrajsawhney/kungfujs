from django.conf.urls import url
from . import views

urlpatterns = [
    #/sensors/
    url(r'^$', views.index, name='index'),

    #/sensors/macro/
    url(r'^macro/$', views.detailMacro,name='detailMacro'),

    url(r'^macrolatest/$', views.detailMacrosingle ),

    #/sensors/micro/
    url(r'^micro/$', views.detailMicro,name='detailMicro'),

    url(r'^addsensorreading/$', views.add_reading),
]