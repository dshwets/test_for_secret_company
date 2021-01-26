from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from news.factories import ArticleFactory


class ArticleDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_article')
        self.url = reverse('news:article_delete', kwargs={'pk': self.article.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_article_delete_unauthorized_get_request(self):
        self.assert_response_status(self.url, 'get', 302)

    def test_articl_delete_unauthorized_post_request(self):
        self.assert_response_status(self.url, 'post', 302)

    def test_article_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'get', 403)

    def test_article_delete_authorized_get_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'article_delete.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_article_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(self.url, 'post', 302)

    def test_article_delete_authorized_post_request_has_perm_article_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        article_wrong_id = self.article.id+10
        self.assert_response_status(reverse('news:article_delete', args=(article_wrong_id,)), 'get', 404)
