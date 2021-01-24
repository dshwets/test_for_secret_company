import factory
from factory.fuzzy import FuzzyText

from accounts.factories import UserFactory
from news.models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    category_id = None

    user_id = factory.SubFactory(
        UserFactory,
        username=FuzzyText(length=50)
    )

    title = factory.Sequence(
        lambda n: f'Title-{n}'
    )

    description = FuzzyText(
        length=150
    )

    image = factory.django.ImageField()
