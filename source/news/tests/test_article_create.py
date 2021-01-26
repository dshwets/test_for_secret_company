from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from news.factories import ArticleFactory
from news.models import Article


class ArticleCreateTestCase(TestCase):
    def setUp(self) -> None:
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.permission_add = Permission.objects.get(codename='can_add_article')
        self.url = reverse('news:article_create')
        self.data = {
            'category_id': self.article.category_id.pk,
            'title': 'test_title',
            'description': 'test_description',
        }

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_create_article(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_authorized_without_permission_get_create_article(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_get_request_has_perm_create_article(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'article_create.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_unauthorized_post_create_article(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_post_create_article(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_post_request_has_perm_create_article(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Article.objects.filter(title='test_title').exists())

    def test_authorized_with_permission_post_create_article_with_empty_name(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        data = {
            'category_id': self.article.category_id,
            'title': '',
            'description': 'test_description',
        }

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
