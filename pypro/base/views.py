from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# view é responsável por responder as requisições que nos fazemos pelo navegador


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')