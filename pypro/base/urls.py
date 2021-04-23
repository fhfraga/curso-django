from django.urls import path
from . import views

app_name = 'base' # serve para emcapsular melhor as urls para saber de qual app é
urlpatterns =[
    path('', views.home, name='home')
]