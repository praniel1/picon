from . import views
from django.conf.urls import url, include
app_name = 'home_page'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'login', views.login_user, name='login_user' )
]