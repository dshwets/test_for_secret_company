from rest_framework.serializers import ModelSerializer

from accounts.models import User
from news.models import Article
from newscategories.models import Category


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategorySerializer(ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(ModelSerializer):
    category_id = CategorySerializer()
    user_id = UserSerializer()

    class Meta:
        model = Article
        fields = '__all__'
