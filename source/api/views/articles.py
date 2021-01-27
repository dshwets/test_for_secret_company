from rest_framework import viewsets

from api.serializers import ArticleSerializer
from news.models import Article


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
