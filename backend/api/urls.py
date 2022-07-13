from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.shortUrl, name='URL SHORTENER'),
    path('<str:short_url_id>', views.redirect_short, name='Long URL')
]
