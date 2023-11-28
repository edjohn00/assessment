import pytest
from factories import BloggerFactory


@pytest.mark.django_db
def test_blogger(blogger):
    assert blogger.get_full_name() == "first_name1 last_name1"
    assert blogger.is_staff == False
    assert blogger.is_superuser == False
