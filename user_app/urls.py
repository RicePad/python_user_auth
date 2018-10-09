from django.conf.urls import url
from user_app import views

url_patterns = [
    url(r'^registration/$', views.register, name='register'),
    url(r'^user/$', views.user_login, name='user_login'),

]
