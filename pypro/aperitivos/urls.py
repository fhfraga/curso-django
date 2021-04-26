from django.urls import path

from pypro.aperitivos.views import video, indice

app_name = 'aperitivos' # serve para emcapsular melhor as urls para saber de qual app é
urlpatterns =[
    path('<slug:slug>', video, name='video'), # slug é um identificador para os vídeos
    path('', indice, name='indice'),
]