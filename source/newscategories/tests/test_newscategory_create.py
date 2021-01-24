from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from newscategories.factories import CategoriesFactory
from newscategories.models import Category


class CategoryCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.category = CategoriesFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_add_category')
        self.url = reverse('newscategories:create_newscategory')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_category(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_authorized_without_permission_get_create_category(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_create_category(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('news_category_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_unauthorized_post_create_category(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_post_create_category(self):
        data = {
            'title': 'random_title',
        }
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_post_request_has_perm_create_category(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        data = {
            'title': 'random_title',
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(title='random_title').exists())

    def test_authorized_with_permission_post_create_category_with_empty_title(self):
        data = {
            'title': ''
        }
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, data)
        field = 'title'
        self.assertFormError(response, 'form', field, 'Обязательное поле.')

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
