from django.conf.urls import url
from .views import (PostListView,PostCreateView,PostDetailView)
from . import views

app_name = 'gram'

urlpatterns=[
    url('^$',PostListView.as_view(),name='post_list'),
    url('^signUp/$',views.signUp,name='signUp'),
    url('^login/$',views.login,name='login'),
    url('^profile/$',views.profile,name='profile'),
    url('^new',PostCreateView.as_view(),name='post_create'),
    url('<int:id>',PostDetailView.as_view(),name='post_details'),
    url(r'^search/', views.search_results, name='search_results')
] 