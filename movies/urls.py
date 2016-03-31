from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^year/(\d{4})$', views.year, name='year'),
    url(r'^ratings$', views.ratings, name='ratings'),
]
