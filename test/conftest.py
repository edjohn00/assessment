import pytest
from factories import BloggerFactory, BlogFactory
from pytest_factoryboy import register
from apps.models import Blogger

register(BloggerFactory)
register(BlogFactory)
