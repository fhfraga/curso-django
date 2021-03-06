import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains
from pypro.aperitivos.views import video


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


def test_status_code(resp):
    assert resp.status_code==200


def test_titulo_video(resp, video):
    assert_contains(resp, '<h1 class="mt-4 mb-3">Vídeo Aperitivo: Motivação</h1>')



def test_conteudo_video(resp, video):
    assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/2aYplgJrPDU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')