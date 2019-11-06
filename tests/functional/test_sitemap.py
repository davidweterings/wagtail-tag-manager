import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_sitemap(client, site):
    response = client.get(site.root_page.url)
    assert response.status_code == 200

    url = reverse("sitemap")
    response = client.get(site.root_url + url)
    assert response.status_code == 200
