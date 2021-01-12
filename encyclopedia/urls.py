from django.urls import path
from . import views
from .util import list_entries


app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:article>/', views.article, name='article')
]
