from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.signUp,name = 'signUp'),
    url('^login/$',views.login,name='login'),
    url('^home/$',views.home,name='home'),
    url('^profile/$',views.home,name='profile'),
    url(r'^search/', views.search_results, name='search_results')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
