import pytest
from factories import BlogFactory


@pytest.mark.django_db
def test_blog(blog):
    assert blog.title == f"Blog Title {blog.id}"
    assert blog.content == f"Blog Content {blog.id}"
