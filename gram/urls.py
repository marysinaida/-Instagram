from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from .views import (PostListView)
from . import views

app_name = 'gram'

urlpatterns=[
    url('^$',PostListView.as_view(),name='post_list'),
    url('^signUp/$',views.signUp,name='signUp'),
    url('^login/$',views.login,name='login'),
    url(r'^search/', views.search_results, name='search_results')
] 