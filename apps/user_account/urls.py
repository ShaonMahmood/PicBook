from django.conf.urls import url, include
from django.contrib.auth.urls import views as auth_views
from . import views

urlpatterns = [
    # post views
    # Namespace : user_account

    # old login view
    # url(r'^login/', views.user_login, name='login'),

    url(r'^$',views.dashboard,name='dashboard'), # index page
    url(r'', include("django.contrib.auth.urls")), # include all the authentication urls
    url(r'^register/', views.register, name='register'),
    url(r'^edit/', views.edit, name='edit'),
]