from django.urls import reverse


def test_home_page_renders(client):
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert b"<h1>Rally</h1>" in response.content
