import pytest
from factories import BloggerFactory
from pytest_factoryboy import register
from apps.models import Blogger

register(BloggerFactory)
