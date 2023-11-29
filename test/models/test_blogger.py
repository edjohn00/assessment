import pytest
from factories import BloggerFactory


@pytest.mark.django_db
def test_blogger():
    blogger = BloggerFactory(
        email="test_email@gmail.com",
        password="test_password",
        first_name="test_first_name",
        last_name="test_last_name",
        is_staff=False,
        is_superuser=False,
    )
    assert blogger.get_full_name() == "test_first_name test_last_name"
    assert blogger.is_staff == False
    assert blogger.is_superuser == False
