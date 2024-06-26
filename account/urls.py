from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.list_accounts),
    path('accounts/<str:pk>/', views.account_detail),
    path('deposit', views.deposit)
]
