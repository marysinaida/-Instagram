from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.signUp,name = 'signUp'),
    url('^login/$',views.login,name='login'),
    url('^home/$',views.home,name='home')
]