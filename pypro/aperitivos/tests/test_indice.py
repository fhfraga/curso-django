import pytest
from django.urls import reverse
from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code==200

@pytest.mark.parametrize(
    'titulo',
    [
        'Video Aperitivo: Motivação',
        'Instalação Python no Windows'
    ]
)
def test_titulo_video(resp, titulo):
    assert_contains(resp, titulo)


# def test_conteudo_video(resp):
#     assert_contains(resp, '<iframe width="560" height="315" src="https://www.youtube.com/embed/2aYplgJrPDU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')