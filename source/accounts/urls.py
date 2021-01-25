from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views.account_create import RegisterView
from accounts.views.account_delete import AccountDeleteView
from accounts.views.account_detail import AccountDetailView
from accounts.views.account_list import AccountListView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('accounts/list/', AccountListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
]
