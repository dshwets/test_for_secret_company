from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory


class AccountListViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory(username='some_admin', first_name='', last_name='', email='')
        self.permission_add = Permission.objects.get(codename='can_view_user')
        self.url = reverse('accounts:account_list')

    def tearDown(self) -> None:
        self.client.logout()

    def test_unauthorized_get_account_list(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.assertRedirects(response, redirect_url, status_code=302)

    def test_authorized_without_permission_get_account_list(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_get_request_has_perm_account_list(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')
        self.assertTemplateUsed('account_list.html')
        self.assert_response_status(self.url, 'get', 200)

    def test_authorized_get_request_has_perm_account_list_existed_search(self):
        self.user.user_permissions.add(self.permission_add)
        self.client.login(username='some_admin', password='pass')

        response = self.client.get(self.url)
        response_empty_search = self.client.get(self.url + '?search=')
        response_succes_search = self.client.get(self.url + '?search=some_admin')
        response_failed_search = self.client.get(self.url + '?search=y')

        self.assertEqual(response.context_data['accounts'][0], response_empty_search.context_data['accounts'][0])
        self.assertEqual(response.context_data['accounts'].count(), response_empty_search.context_data['accounts'].count())

        self.assertEqual(response.context_data['accounts'][0], response_succes_search.context_data['accounts'][0])
        self.assertEqual(response.context_data['accounts'].count(), response_succes_search.context_data['accounts'].count())

        self.assertNotEqual(response.context_data['accounts'], response_failed_search.context_data['accounts'])
        self.assertNotEqual(response.context_data['accounts'].count(), response_failed_search.context_data['accounts'].count())


    def assert_response_status(self, url, method, code):
        if method == "get":
            response = self.client.get(url)
            self.assertEqual(response.status_code, code)
        elif method == "post":
            response = self.client.post(url)
            self.assertEqual(response.status_code, code)