from django.contrib import admin
from django.urls import path
from article.views import *

app_name = "article"

urlpatterns = [
    path('dashboard/', dashboard, name = "dashboard"),
    path('addarticle/', addarticle, name = "addarticle"),
    path('detailarticle/<int:id>', detailarticle, name = "detailarticle"),
    path('updatearticle/<int:id>', updatearticle, name = "updatearticle"),
    path('deletearticle/<int:id>', deletearticle, name = "deletearticle"),
    path('', articles, name = "articles"),
    path('comment/<int:id>', addComment, name = "addComment"),
]
