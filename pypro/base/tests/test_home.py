from django.test import Client
from django.urls.base import reverse
from pypro.django_assertions import assert_contains
import pytest

# reverse serve para poder variar o nome sem precisar ficar alterando o código
# pois agora o parametro é o nome do path. agora a url é dependente apenas do 
# nome (name na url)
@pytest.fixture
def resp(client):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro Fernando</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')
