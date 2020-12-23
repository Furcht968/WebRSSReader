from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

urlpatterns = [
    path('rss', cache_page(60 * 15)(views.rss)),
    path('', views.index)
]