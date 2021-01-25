from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from accounts.models import User


class AccountUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.user_for_change = UserFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_user')
        self.url = reverse('accounts:account_update', kwargs={'pk': self.user_for_change.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def common_data(self):
        data = {
            'username': 'test_username',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@gmail.com',
        }
        return data

    def test_unauthorized_get_update_account(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_account(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_account(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_account(self):
        data = self.common_data()
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_account(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('account_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_product(self):
        data = self.common_data()
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(pk=self.user_for_change.pk)
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('accounts:account_detail', kwargs={'pk': self.user_for_change.pk})
        self.assertEqual(response.url, redirect_url)

    def test_authorized_with_permission_post_update_product_with_empty_title(self):
        data = {
            'username': '',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@gmail.com',
        }
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'username'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)