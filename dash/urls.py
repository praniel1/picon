from django.conf.urls import url
from . import views
app_name = 'dash'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout_user', views.logout_user, name='logout_user'),
    url(r'^pic$', views.upload_pic, name='pic'),
]