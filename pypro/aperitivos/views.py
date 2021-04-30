from pypro.aperitivos.models import Video
from django.shortcuts import render

videos=[
       Video(slug='motivacao', titulo='Video Aperitivo: Motivação', youtube_id='2aYplgJrPDU'),
       Video(slug='instalacao-windows', titulo='Instalação Python no Windows', youtube_id='ScmQ4I5Qr5s')
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    # objects retorna um objeto do tipo QuerySet; o metodo get busca apenas um objeto no banco de dados
    # se ele encontrar nenhum ou mais de um ele dará um erro
    video = Video.objects.get(slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})
