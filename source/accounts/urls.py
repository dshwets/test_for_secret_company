from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from accounts.views.account_create import RegisterView
from accounts.views.account_delete import AccountDeleteView
from accounts.views.account_detail import AccountDetailView
from accounts.views.account_list import AccountListView
from accounts.views.account_update import AccountUpdateView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('list/', AccountListView.as_view(), name='account_list'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),
    path('<int:pk>/update/', AccountUpdateView.as_view(), name='account_update'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='account_change_password.html',
        success_url=reverse_lazy('accounts:account_password_change_done')),
        name='account_change_password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(
        template_name='account_change_password_done.html'),
         name='account_password_change_done'),
]
