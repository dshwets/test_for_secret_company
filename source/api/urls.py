from rest_framework.routers import DefaultRouter

from api.views.articles import ArticleViewSet
from api.views.categories import CategoryViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'categories', CategoryViewSet, basename='category')
urlpatterns = router.urls
