import factory
from factory.fuzzy import FuzzyText

from accounts.factories import UserFactory
from news.models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    category_id = None
    user_id = factory.SubFactory(UserFactory)
    title = FuzzyText(length=50)
    description = FuzzyText(length=50)
    image = None
