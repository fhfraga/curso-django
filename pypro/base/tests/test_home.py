from django.test import Client

# Client serve para emular requisições http
def test_status_code(client:Client):
    resp = client.get('/')
    assert resp.status_code == 200