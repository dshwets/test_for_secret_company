from django.test import TestCase
from django.urls import reverse

from accounts.factories import UserFactory
from newscategories.factories import CategoriesFactory


class CategoryListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.category = CategoriesFactory()
        self.user = UserFactory(username='some_admin')
        self.url = reverse('newscategories:list_newscategory')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_category_list(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_get_request_category_list(self):
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('news_category_list.html')
        self.assert_response_status(self.url, 'get', 200)

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)