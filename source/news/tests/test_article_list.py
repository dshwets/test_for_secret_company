from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from news.factories import ArticleFactory


class ArticleListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.url = reverse('news:article_list')
        self.url_with_pk = reverse('news:article_category_list', kwargs={'pk': self.article.category_id.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_article_list(self):
        response = self.client.get(self.url)
        response_with_pk = self.client.get(self.url_with_pk)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        redirect_url_with_pk = reverse('accounts:login') + '?next=' + self.url_with_pk
        self.assertRedirects(response, redirect_url, status_code=302)
        self.assertRedirects(response_with_pk, redirect_url_with_pk, status_code=302)

    def test_authorized_get_request_article_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        response_with_pk = self.client.get(self.url_with_pk)
        self.assertTemplateUsed(response, 'article_list.html')
        self.assert_response_status(self.url, 'get', 200)
        self.assertTemplateUsed(response_with_pk, 'article_list.html')
        self.assert_response_status(self.url_with_pk, 'get', 200)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)
