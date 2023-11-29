import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed
from rest_framework import status


@pytest.mark.django_db
def test_index_view(client, blogger):
    url = reverse("apps:accounts:profile:index")
    response = client.get(url, follow=True)
    assertTemplateUsed(response, "account/login.html")
    client.force_login(blogger)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assertTemplateUsed(response, "apps/accounts/profile/index.html")
