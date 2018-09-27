from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pdf/$', views.pdf_list, name='pdf_list'),
    url(r'^pdf/(?P<pk>\d+)/$', views.pdf_detail, name='pdf_detail'),
    url(r'^pdf/(?P<pk>\d+)/edit/$', views.pdf_edit, name='pdf_edit'),
    url(r'^pdf/(?P<pk>\d+)/pdf_get_file/$', views.pdf_get_file, name='pdf_get_file'),
]