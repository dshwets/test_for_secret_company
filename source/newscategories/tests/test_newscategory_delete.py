from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory
from newscategories.factories import CategoriesFactory


class CategoryDeleteTestCase(TestCase):
    def setUp(self) -> None:
        self.category = CategoriesFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_delete_category')

    def tearDown(self) -> None:
        self.client.logout()

    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)

    def test_category_delete_unauthorized_get_request(self):
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(self.category.id,)), 'get', 302)

    def test_category_delete_unauthorized_post_request(self):
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(self.category.id,)),
                                    'post', 302)

    def test_category_delete_authorized_request_no_perm(self):
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(self.category.id,)), 'get', 403)

    def test_category_delete_authorized_get_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('news_category_delete.html')
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(self.category.id,)), 'get', 200)

    def test_category_delete_authorized_post_request_has_perm(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(self.category.id,)), 'post', 302)

    def test_category_delete_authorized_post_request_has_perm_employee_not_found(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        employee_wrong_id = self.category.id+10
        self.assert_response_status(reverse('newscategories:delete_newscategory', args=(employee_wrong_id,)), 'get', 404)
