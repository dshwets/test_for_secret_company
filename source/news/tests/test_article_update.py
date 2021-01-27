from django.contrib.auth.models import Permission
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from news.factories import ArticleFactory
from news.models import Article


class ArticleUpdateTestCase(TestCase):
    def setUp(self) -> None:
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_change_article')
        self.url = reverse('news:article_update', kwargs={'pk': self.article.pk})
        self.data = {
            'category_id': self.article.category_id.pk,
            'title': 'test_title',
            'description': 'test_description',
        }

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_update_article(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_unauthorized_post_update_article(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_authorized_without_permission_get_update_article(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 403)

    def test_authorized_without_permission_post_update_article(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_update_article(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        request = self.client.get(self.url)
        self.assertTemplateUsed(request, 'article_update.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_with_permission_post_update_article(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, 302)
        article = Article.objects.get(pk=self.article.pk)
        self.assertEqual(article.category_id.pk, self.data['category_id'])
        self.assertEqual(article.title, self.data['title'])
        self.assertEqual(article.description, self.data['description'])
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('news:article_detail', kwargs={'pk': self.article.pk})
        self.assertEqual(response.url, redirect_url)

    def test_authorized_with_permission_post_update_product_with_empty_title(self):
        data = self.data
        data['title'] = ''
        self.user.user_permissions.add(self.permission)
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