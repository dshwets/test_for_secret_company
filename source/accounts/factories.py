import factory
from factory import PostGenerationMethodCall
from factory.fuzzy import FuzzyText

from accounts.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = FuzzyText(length=50)
    password = PostGenerationMethodCall('set_password', 'pass')
