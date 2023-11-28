import factory
from apps.models import Blogger


class BloggerFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f"test_email{n}@gmail.com")
    password = factory.Sequence(lambda n: f"test_password{n}")
    first_name = factory.Sequence(lambda n: f"first_name{n}")
    last_name = factory.Sequence(lambda n: f"last_name{n}")
    is_staff = False
    is_superuser = False

    class Meta:
        model = Blogger
