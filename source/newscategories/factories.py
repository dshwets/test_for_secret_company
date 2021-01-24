import factory

from newscategories.models import Category


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    title = factory.Sequence(
        lambda n: f'Title-{n}'
    )

    parent_id = factory.SubFactory(
        'source.newscategories.factories.CategoriesFactory',
        parent_id=None
    )
