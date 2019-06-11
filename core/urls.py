from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('cryptocurrencies/', views.CryptoListView.as_view(), name='crypto-list'),
    path('cryptocurrencies/<int:pk>', views.CryptoListView.as_view(), name='crypto-detail'),
    path('websites/', views.WebSiteListView.as_view(), name='website-list'),
]
