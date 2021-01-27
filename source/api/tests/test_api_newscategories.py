import json

from django.test import TestCase
from rest_framework.response import Response

from accounts.factories import UserFactory
from newscategories.factories import CategoriesFactory


class ApiArticlesTestCase(TestCase):

    def setUp(self) -> None:
        self.category = CategoriesFactory()
        self.user = UserFactory(username='some_admin')
        self.maxDiff = None
        self.data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.category.pk,
                        'created_by':
                            {
                                'id': self.category.created_by.pk,
                                'username': self.category.created_by.username
                            },
                        'created_at': self.category.created_at,
                        'updated_at': self.category.updated_at,
                        'title': self.category.title,
                        'image': self.category.image,
                        'parent_id': self.category.parent_id
                    }
                ]
        }

    def test_api_get_category_list(self):
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), Response)
        json_data = json.loads(response.content)
        self.assertEqual(json_data['results'][0]['title'], self.data['results'][0]['title'])
        self.assertEqual(json_data['results'][0]['parent_id'], self.data['results'][0]['parent_id'])
        self.assertEqual(json_data['results'][0]['id'], self.data['results'][0]['id'])

    def test_api_get_category(self):
        response = self.client.get(f'/api/categories/{self.category.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), Response)
        json_data = json.loads(response.content)
        self.assertEqual(json_data['title'], self.data['results'][0]['title'])
        self.assertEqual(json_data['parent_id'], self.data['results'][0]['parent_id'])
        self.assertEqual(json_data['id'], self.data['results'][0]['id'])
