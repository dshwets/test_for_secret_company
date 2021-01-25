from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from accounts.models import User


class AccountCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory(username='some_admin')
        self.url = reverse('accounts:register')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_request_create_account(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), TemplateResponse)
        self.assertTemplateUsed(response, 'account_create.html')

    def test_unauthorized_post_request_create_account(self):
        data = {
            'username': 'test_username',
            'password1': 'TestPassword255',
            'password2': 'TestPassword255',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'exampleme@gmail.com'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='test_username').exists())
        self.assertTrue(User.objects.filter(first_name='test_first_name').exists())
        self.assertTrue(User.objects.filter(last_name='test_last_name').exists())
        self.assertTrue(User.objects.filter(email='exampleme@gmail.com').exists())

    def test_unauthorized_post_create_account_with_empty_username(self):
        data = {
            'username': '',
            'password1': 'TestPassword255',
            'password2': 'TestPassword255',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'exampleme@gmail.com'
        }
        response = self.client.post(self.url, data)
        field = 'username'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def test_unauthorized_post_create_account_with_empty_password(self):
        data = {
            'username': 'test_username',
            'password1': '',
            'password2': '',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'exampleme@gmail.com'
        }
        response = self.client.post(self.url, data)
        field = 'password1'
        field2 = 'password2'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')
        self.assertFormError(response, 'form', field2, 'Обязательное поле.')

    def test_unauthorized_post_create_account_with_not_equal_passwords(self):
        data = {
            'username': 'test_username',
            'password1': 'TestPassword255',
            'password2': 'TestPassword254',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'exampleme@gmail.com'
        }
        response = self.client.post(self.url, data)
        field = 'password2'
        self.assertFormError(response, 'form', field, 'Два поля с паролями не совпадают.')

    def test_unauthorized_post_create_account_with_weak_password(self):
        data = {
            'username': 'test_username',
            'password1': 'test',
            'password2': 'test',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'exampleme@gmail.com'
        }
        response = self.client.post(self.url, data)
        field = 'password2'
        self.assertFormError(response, 'form', field,
                             'Введённый пароль слишком короткий. Он должен содержать как минимум 8 символов.')
        self.assertFormError(response, 'form', field,
                             'Введённый пароль слишком широко распространён.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
