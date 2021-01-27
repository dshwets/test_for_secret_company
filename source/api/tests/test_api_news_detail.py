import json

from django.test import TestCase
from rest_framework.response import Response

from accounts.factories import UserFactory
from news.factories import ArticleFactory


class ApiArticlesTestCase(TestCase):

    def setUp(self) -> None:
        self.article = ArticleFactory()
        self.user = UserFactory(username='some_admin')
        self.maxDiff = None
        self.data = {
            'count': 1,
            'next': None,
            'previous': None,
            'results':
                [
                    {
                        'id': self.article.pk,
                        'category_id':
                            {
                                'id': self.article.category_id.pk,
                                'created_by': {
                                    'id': self.article.category_id.created_by.pk,
                                    'username': self.article.category_id.created_by.username
                                },
                                'title': self.article.category_id.title,
                                'image': self.article.category_id.image.path,
                                'parent_id': None
                            },
                        'user_id':
                            {
                                'id': self.article.user_id.pk,
                                'username': self.article.user_id.username
                            },
                        'title': self.article.title,
                        'description': self.article.description,
                        'image': self.article.image.path
                    }
                ]
        }

    def test_api_get_article_list(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), Response)
        json_data = json.loads(response.content)
        self.assertEqual(json_data['results'][0]['title'], self.data['results'][0]['title'])
        self.assertEqual(json_data['results'][0]['description'], self.data['results'][0]['description'])
        self.assertEqual(json_data['results'][0]['user_id']['id'], self.data['results'][0]['user_id']['id'])

    def test_api_get_article(self):
        response = self.client.get(f'/api/articles/{self.article.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), Response)
        json_data = json.loads(response.content)
        self.assertEqual(json_data['title'], self.data['results'][0]['title'])
        self.assertEqual(json_data['description'], self.data['results'][0]['description'])
        self.assertEqual(json_data['user_id']['id'], self.data['results'][0]['user_id']['id'])
