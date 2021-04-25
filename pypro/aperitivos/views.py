from django.shortcuts import render



def video(request, slug):
    videos={
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'youtube_id': '2aYplgJrPDU'},
        'instalacao-windows': {'titulo': 'Instalação Python no Windows', 'youtube_id': 'ScmQ4I5Qr5s'}
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})