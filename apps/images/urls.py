from django.conf.urls import url
from . import views

app_name = 'images'

urlpatterns = [
    url(r'^create/', views.image_create, name='create'),
    url(r'^detail/(?P<id>[0-9]+)/(?P<slug>[-\w]+)/',views.image_detail,name='detail'),
    url(r'^like/', views.image_like, name='like'),
]