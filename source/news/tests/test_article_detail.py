from django.contrib.auth.models import Permission
from news.factories import ArticleFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory


class ArticleDetailTestCase(TestCase):

    def setUp(self):
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.url = reverse('news:article_detail', kwargs={'pk': self.article.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_article_detail(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.check_redirect(response, redirect_url)

    def test_authorized_get_article_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')

