import factory
from apps.models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    blogger = factory.SubFactory("factories.BloggerFactory")
    title = factory.Sequence(lambda n: f"Blog Title {n}")
    content = factory.Sequence(lambda n: f"Blog Content {n}")

    class Meta:
        model = Blog
