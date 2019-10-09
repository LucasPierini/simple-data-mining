from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.Main.as_view(), name='main'),  
]

urlpatterns += staticfiles_urlpatterns()