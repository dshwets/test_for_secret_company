from rest_framework import viewsets

from api.serializers import CategorySerializer
from newscategories.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
