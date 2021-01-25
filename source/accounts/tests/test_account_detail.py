from django.contrib.auth.models import Permission
from accounts.factories import UserFactory
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse


class AccountDetailViewTestCase(TestCase):

    def setUp(self):
        self.user_for_check = UserFactory()
        self.user = UserFactory(username='some_admin')
        self.permission = Permission.objects.get(codename='can_view_user')
        self.url = reverse('accounts:account_detail', kwargs={'pk':self.user_for_check.pk})

    def tearDown(self) -> None:
        self.client.logout()

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)

    def test_unauthorized_get_account_detail(self):
        response = self.client.get(self.url)
        redirect_url = reverse('accounts:login') + '?next=' + self.url
        self.check_redirect(response, redirect_url)

    def test_authorized_with_permission_get_account_detail(self):
        self.user.user_permissions.add(self.permission)
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account_detail.html')

    def test_authorized_without_permission_get_account_detail(self):
        self.client.login(username='some_admin', password='pass')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 403)
