import factory
from factory.fuzzy import FuzzyText

from accounts.factories import UserFactory
from newscategories.models import Category


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(
        lambda n: f'Title-{n}'
    )

    parent_id = None

    image = factory.django.ImageField()

    created_by = factory.SubFactory(
        UserFactory,
        username=FuzzyText(length=50)
    )
