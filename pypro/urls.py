"""pypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

#import base

# fazer mapeamento do que está na view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pypro.base.urls')), # serve para mostrar o caminho da urls
# de base, pois se incluir algo na frente terá que colocar antes do caminho das
# urls de base. Por exemplo colocamos 'pypro' as url de base serão pypro/urls_base
]

# se DEBUG for verdadeiro, import o debug_toolbar e adicione a lista urlpatterns
# o padrão do caminho abaixo
if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
    path('__debug__/', include(debug_toolbar.urls))
    )
