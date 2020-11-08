"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from article.views import *
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles, name = "articles"), #isim vermek çok önemli sakına unutma.
    path('about/', about, name = "about"), #isim vermek çok önemli sakına unutma.
    path('detail/<int:id>', detail, name = "detail"),
    path('articles/',  include('article.urls')), #articles i görürsen git article.urls ye bak ona göre getir.
    path('users/',include('user.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)